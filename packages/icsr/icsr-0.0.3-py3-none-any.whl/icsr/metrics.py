from pydantic import BaseModel, validator
from typing import Optional, Union
import numpy as np
from scipy.optimize import linear_sum_assignment

import src.icsr.structure as structure
import src.icsr.utils as utils

class SimilarityOutput(BaseModel):
    precision: float
    recall: float
    f1: float
    pred_support: Optional[int]
    gold_support: Optional[int]

    def to_array(self) -> np.array:
        return np.array(
            [
                self.precision,
                self.recall,
                self.f1,
            ]
        )

    @validator("precision", "recall", "f1")
    def format_metrics(v):
        return round(v, 4)


# TODO: implement a list of metrics and display them
class SimilarityOverview(BaseModel):
    pass


class Similarity(BaseModel):
    caefe_always_f1_alignment: Optional[bool] = True
    document_level_averaging: Optional[bool] = False
    count_zero_icsr: Optional[bool] = False
    string_similarity_method: str = "token"

    @validator("string_similarity_method")
    def check_string_similarity_method(cls, v):
        possible_values = ["token", "exact"]
        if v not in possible_values:
            raise ValueError(
                f"Expected 'string_similarity_method' to have a value in {possible_values}, but got value '{v}'."
            )
        return v

    def __call__(
        self,
        pred: Union[structure.Icsr, structure.Document, structure.Dataset],
        gold: Union[structure.Icsr, structure.Document, structure.Dataset],
    ) -> SimilarityOutput:
        if type(pred) is not type(gold):
            raise TypeError(
                f"Predicted and gold inputs should be the same type, got {type(pred)} and {type(gold)} respectively."
            )

        if not isinstance(
            pred, (structure.Icsr, structure.Document, structure.Dataset)
        ):
            raise TypeError(f"Invalid input type, got {type(pred)}.")

        if isinstance(pred, structure.Icsr):
            return self._icsr_similarity(pred, gold)

        if isinstance(pred, structure.Document):
            return self._document_similarity(pred, gold)

        if isinstance(pred, structure.Dataset):
            return self._dataset_similarity(pred, gold)

    def _string_similarity(self, pred_str: str, gold_str: str) -> SimilarityOutput:
        if self.string_similarity_method == "token":
            return self._string_token_similarity(pred_str, gold_str)
        elif self.string_similarity_method == "exact":
            return self._string_exact_similarity(pred_str, gold_str)

    def _string_token_similarity(
        self, pred_str: str, gold_str: str
    ) -> SimilarityOutput:
        # word tokenization
        # TODO: also split on '/'?
        pred_words = pred_str.split()
        gold_words = gold_str.split()

        # calculate word overlap metrics
        common_words = set(pred_words) & set(gold_words)

        # because of previous validation, we never have zero words
        prec = len(common_words) / len(pred_words)
        rec = len(common_words) / len(gold_words)
        f1 = utils.f1(prec, rec)

        return SimilarityOutput(precision=prec, recall=rec, f1=f1)

    def _string_exact_similarity(
        self, pred_str: str, gold_str: str
    ) -> SimilarityOutput:
        exact_match = pred_str == gold_str

        return SimilarityOutput(
            precision=exact_match, recall=exact_match, f1=exact_match
        )

    def _icsr_similarity(
        self, pred_icsr: structure.Icsr, gold_icsr: structure.Icsr
    ) -> SimilarityOutput:
        # subject
        subject_sim = self._string_similarity(pred_icsr.subject, gold_icsr.subject)

        # drug
        drug_sim = self._string_similarity(pred_icsr.drug, gold_icsr.drug)

        # reaction
        reaction_sim = self._string_similarity(pred_icsr.reaction, gold_icsr.reaction)

        # equal weighting of three similarities
        prec = (subject_sim.precision + drug_sim.precision + reaction_sim.precision) / 3
        rec = (subject_sim.recall + drug_sim.recall + reaction_sim.recall) / 3
        f1 = utils.f1(prec, rec)

        return SimilarityOutput(precision=prec, recall=rec, f1=f1)

    def _document_similarity(
        self, pred_document: structure.Document, gold_document: structure.Document
    ) -> SimilarityOutput:
        num_pred_icsrs = len(pred_document)
        num_gold_icsrs = len(gold_document)

        # both documents contain no icsrs
        if num_pred_icsrs == 0 and num_gold_icsrs == 0:
            if self.count_zero_icsr:
                return SimilarityOutput(
                    precision=1.0, recall=1.0, f1=1.0, pred_support=1, gold_support=1
                )
            else:
                return SimilarityOutput(
                    precision=1.0, recall=1.0, f1=1.0, pred_support=0, gold_support=0
                )
        # one document without icsrs
        elif num_pred_icsrs == 0 or num_gold_icsrs == 0:
            # for count_zero_icsr, we need to set the minimum num to 1
            if self.count_zero_icsr:
                return SimilarityOutput(
                    precision=0.0,
                    recall=0.0,
                    f1=0.0,
                    pred_support=max(1, num_pred_icsrs),
                    gold_support=max(1, num_gold_icsrs),
                )
            else:
                return SimilarityOutput(
                    precision=0.0,
                    recall=0.0,
                    f1=0.0,
                    pred_support=num_pred_icsrs,
                    gold_support=num_gold_icsrs,
                )

        # both documents contain icsrs
        # get unnormalized similarities for each alignment (prec / rec / f1 alignment)
        unnormalized_prec, unnormalized_rec = self._unnormalized_caefe_similarity(
            pred_document, gold_document
        )

        # normalize similarity scores
        prec = unnormalized_prec / num_pred_icsrs
        rec = unnormalized_rec / num_gold_icsrs
        f1 = utils.f1(prec, rec)

        return SimilarityOutput(
            precision=prec,
            recall=rec,
            f1=f1,
            pred_support=num_pred_icsrs,
            gold_support=num_gold_icsrs,
        )

    def _dataset_similarity(
        self, pred_dataset: structure.Dataset, gold_dataset: structure.Dataset
    ) -> SimilarityOutput:
        # check if the dataset contains the same documents
        if pred_dataset.keys() != gold_dataset.keys():
            raise ValueError(
                "Document identifiers in predicted and gold datasets should be equal."
            )

        # get similarity scores for each document
        document_similarities = {}
        for doc_id in pred_dataset.keys():
            document_similarities.update(
                {
                    doc_id: self._document_similarity(
                        pred_dataset[doc_id],
                        gold_dataset[doc_id],
                    )
                }
            )

        # average similarities per metric across the documents
        # TODO: this can be one code-block
        if self.document_level_averaging:
            prec_nom = sum([sim.precision for sim in document_similarities.values()])
            rec_nom = sum([sim.recall for sim in document_similarities.values()])
            prec_denom = len(document_similarities)
            rec_denom = len(document_similarities)
        # average similarities per metrics across ICSRs
        else:
            prec_nom = sum(
                [
                    sim.precision * sim.pred_support
                    for sim in document_similarities.values()
                ]
            )
            rec_nom = sum(
                [
                    sim.recall * sim.gold_support
                    for sim in document_similarities.values()
                ]
            )
            prec_denom = sum(
                [sim.pred_support for sim in document_similarities.values()]
            )
            rec_denom = sum(
                [sim.gold_support for sim in document_similarities.values()]
            )

        prec = prec_nom / prec_denom
        rec = rec_nom / rec_denom
        f1 = utils.f1(prec, rec)

        return SimilarityOutput(
            precision=prec,
            recall=rec,
            f1=f1,
            pred_support=prec_denom,
            gold_support=rec_denom,
        )

    def _unnormalized_caefe_similarity(
        self, pred_document: structure.Document, gold_document: structure.Document
    ) -> tuple[float, float]:
        """Computes the un-normalized Constrained Entity-Alignment F-Measure (CEAF) for evaluating coreference.

        Gold and predicted mentions are aligned into entityings which maximise a similarity metric
        https://www.semanticscholar.org/paper/On-Coreference-Resolution-Performance-Metrics-Luo/de133c1f22d0dfe12539e25dda70f28672459b99

        """
        # calcalate pairwise icsr similarities
        scores = np.zeros((len(pred_document), len(gold_document), 3))
        for i in range(len(pred_document)):
            for j in range(len(gold_document)):
                pred_icsr = pred_document[i]
                gold_icsr = gold_document[j]
                scores[i, j] = self._icsr_similarity(pred_icsr, gold_icsr).to_array()

        # if we are using the f1 alignment
        if self.caefe_always_f1_alignment:
            prec_alignment = linear_sum_assignment(scores[:, :, 2], maximize=True)
            rec_alignment = prec_alignment
        # use different prec and rec alignments
        else:
            prec_alignment = linear_sum_assignment(scores[:, :, 0], maximize=True)
            rec_alignment = linear_sum_assignment(scores[:, :, 1], maximize=True)

        # unnormalized prec and rec
        unnormalized_prec = sum(scores[prec_alignment[0], prec_alignment[1], 0])
        unnormalized_rec = sum(scores[rec_alignment[0], rec_alignment[1], 1])

        return unnormalized_prec, unnormalized_rec
