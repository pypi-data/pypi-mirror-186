from pydantic import BaseModel, ValidationError, validator
from collections import OrderedDict
import icsr.utils as utils
from typing import Union, Optional

# Structure for the model outputs:
class Evidence(BaseModel):
    span_start: int
    span_end: int
    span_str: str

    @validator("span_str")
    def span_logic(cls, field_value, values, field, config):
        span_start = values["span_start"]
        span_end = values["span_end"]
        span_str = field_value

        if span_end <= span_start:
            raise ValueError(
                f"span_end ({span_end}) should be greater than span_start ({span_start})."
            )

        if len(span_str) != span_end - span_start:
            raise ValueError(
                f"Expected span_str to be of length {span_end - span_start}, got length {len(span_str)}."
            )
        return span_str

    def __str__(self):
        return f"""'{self.span_str}'({self.span_start}-{self.span_end})"""

    def __eq__(self, other):
        return (
            (self.span_start == other.span_start)
            & (self.span_end == other.span_end)
            & (self.span_str == other.span_str)
        )

    def __hash__(self):
        return hash(str(self))


class Icsr(BaseModel):
    subject: str
    drug: str
    reaction: str
    subject_evidence: Optional[list[Evidence]]
    drug_evidence: Optional[list[Evidence]]
    reaction_evidence: Optional[list[Evidence]]

    @validator("subject", "drug", "reaction")
    def str_valid(cls, v):
        v = utils.normalize_text(v)
        if v == "":
            raise ValueError("ICSR attribute may not be empty after normalization.")
        return v

    @validator("subject_evidence", "drug_evidence", "reaction_evidence")
    def no_duplicate_evidence(cls, v):
        # deduplicate list but keep order
        v = list(OrderedDict.fromkeys(v))
        return v

    def has_valid_evidence(self, ignore_subject=False):
        return (
            ((len(self.subject_evidence) > 0) or ignore_subject)
            & (len(self.drug_evidence) > 0)
            & (len(self.reaction_evidence) > 0)
        )

    def __str__(self):
        return f"""ICSR:
    subject: {self.subject}
    subject_evidence: {self.subject_evidence}
    drug: {self.drug}
    drug_evidence: {self.drug_evidence}
    reaction: {self.reaction}
    reaction_evidence: {self.reaction_evidence}"""

    def __eq__(self, other):
        return (
            (self.subject == other.subject)
            & (self.drug == other.drug)
            & (self.reaction == other.reaction)
            & (self.subject_evidence == other.subject_evidence)
            & (self.drug_evidence == other.drug_evidence)
            & (self.reaction_evidence == other.reaction_evidence)
        )

    def __hash__(self):
        return hash(str(self))


class Document(BaseModel):
    icsrs: list[Icsr]
    identifier: str

    @validator("icsrs")
    def no_duplicate_icsrs(cls, v):
        # deduplicate list but keep order
        v = list(OrderedDict.fromkeys(v))
        return v

    def __getitem__(self, key):
        return self.icsrs[key]

    def __len__(self):
        return len(self.icsrs)

    def get_valid_icsrs(self, ignore_subject=False):
        return Document(
            identifier=self.identifier,
            icsrs=[
                icsr
                for icsr in self.icsrs
                if icsr.has_valid_evidence(ignore_subject=ignore_subject)
            ],
        )


class Dataset(BaseModel):
    # NOTE: rethink this
    documents: Union[dict[str, Document], list[Document]]
    # documents: dict[str, Document]

    @validator("documents")
    def dataset_not_empty(cls, v):
        return utils.dataset_not_empty(cls, v)

    def __getitem__(self, key):
        return self.documents[key]

    def __len__(self):
        return len(self.documents)

    def keys(self):
        return self.documents.keys()

    def values(self):
        return self.documents.values()

    def items(self):
        return self.documents.items()

    def get_valid_icsrs(self, ignore_subject=False):
        return Dataset(
            documents={
                identifier: doc.get_valid_icsrs(ignore_subject=ignore_subject)
                for identifier, doc in self.items()
            }
        )


# Structure for the model inputs:
class TextDocument(BaseModel):
    text: str
    identifier: str

    @validator("text", "identifier")
    def str_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError("Empty string not allowed.")
        return v


class TextDataset(BaseModel):
    documents: Union[dict[str, TextDocument], list[TextDocument]]

    @validator("documents")
    def dataset_not_empty(cls, v):
        return utils.dataset_not_empty(cls, v)

    def __getitem__(self, key):
        return self.documents[key]

    def __len__(self):
        return len(self.documents)

    def keys(self):
        return self.documents.keys()

    def values(self):
        return self.documents.values()

    def items(self):
        return self.documents.items()
