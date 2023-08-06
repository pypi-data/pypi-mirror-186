from pydantic import BaseModel, validator
from collections import OrderedDict
import icsr.structure as structure
import icsr.utils as utils
import re
from typing import Union


class EvidenceStrategy(BaseModel):
    return_all_evidence: bool = True

    def get_evidence(
        self,
        candidate: Union[structure.Icsr, structure.Document, structure.Dataset],
        support: Union[str, structure.TextDocument, structure.TextDataset],
    ) -> Union[structure.Icsr, structure.Document, structure.Dataset]:
        if isinstance(candidate, structure.Icsr):
            if not isinstance(support, str):
                raise TypeError(
                    f'Wrong support type. Expected "str", got {type(support)}.'
                )
            copy_candidate = candidate.copy(deep=True)
            self._icsr_evidence(copy_candidate, support)
            return copy_candidate

        if isinstance(candidate, structure.Document):
            if not isinstance(support, structure.TextDocument):
                raise TypeError(
                    f'Wrong support type. Expected "structure.TextDocument", got {type(support)}.'
                )
            copy_candidate = candidate.copy(deep=True)
            self._document_evidence(copy_candidate, support)
            return copy_candidate

        if isinstance(candidate, structure.Dataset):
            if not isinstance(support, structure.TextDataset):
                raise TypeError(
                    f'Wrong support type. Expected "structure.TextDataset", got {type(support)}.'
                )
            copy_candidate = candidate.copy(deep=True)
            self._dataset_evidence(copy_candidate, support)
            return copy_candidate

    def _icsr_evidence(self, icsr: structure.Icsr, text: str) -> None:
        icsr.subject_evidence = self._get_subject_evidence(icsr.subject, text)
        icsr.drug_evidence = self._get_drug_evidence(icsr.drug, text)
        icsr.reaction_evidence = self._get_reaction_evidence(icsr.reaction, text)

    def _document_evidence(
        self, document: structure.Document, text_doc: structure.TextDocument
    ) -> None:
        # check validity of document
        if text_doc.identifier != document.identifier:
            raise ValueError(f"Document and TextDocument identifiers should be equal.")
        # get evidence for every icsr
        for icsr in document.icsrs:
            text = text_doc.text
            self._icsr_evidence(icsr, text)

    def _dataset_evidence(
        self, dataset: structure.Dataset, text_dataset: structure.TextDataset
    ) -> None:
        # check dataset validity
        if text_dataset.keys() != dataset.keys():
            raise ValueError(f"Dataset and TextDataset identifiers should be equal.")
        # get evidence for every document
        for iden, doc in dataset.items():
            text_doc = text_dataset[iden]
            self._document_evidence(doc, text_doc)

    # functions that need to be implemented by an inheritant
    def _get_subject_evidence(self, string: str, text: str) -> list[structure.Evidence]:
        raise NotImplementedError

    def _get_drug_evidence(self, string: str, text: str) -> list[structure.Evidence]:
        raise NotImplementedError

    def _get_reaction_evidence(
        self, string: str, text: str
    ) -> list[structure.Evidence]:
        raise NotImplementedError


class ExactEvidence(EvidenceStrategy):
    def _get_all_evidence(self, string: str, text: str) -> list[structure.Evidence]:
        matches = list(re.finditer(string, text))
        if not self.return_all_evidence:
            matches = matches[:1]
        return [
            structure.Evidence(
                span_start=m.span()[0], span_end=m.span()[1], span_str=m.group()
            )
            for m in matches
        ]

    def _get_subject_evidence(self, string: str, text: str) -> list[structure.Evidence]:
        return self._get_all_evidence(string, text)

    def _get_drug_evidence(self, string: str, text: str) -> list[structure.Evidence]:
        return self._get_all_evidence(string, text)

    def _get_reaction_evidence(
        self, string: str, text: str
    ) -> list[structure.Evidence]:
        return self._get_all_evidence(string, text)
