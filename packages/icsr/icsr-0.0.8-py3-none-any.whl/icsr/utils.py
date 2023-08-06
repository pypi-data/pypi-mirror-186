import re
import string

# src: https://qa.fastforwardlabs.com/no%20answer/null%20threshold/bert/distilbert/exact%20match/f1/robust%20predictions/2020/06/09/Evaluating_BERT_on_SQuAD.html
def normalize_text(s):
    """Removing articles and punctuation, and standardizing whitespace are all typical text processing steps."""

    def remove_articles(text):
        regex = re.compile(r"\b(a|an|the)\b", re.UNICODE)
        return re.sub(regex, " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def f1(prec, rec):
    return (2 * (prec * rec) / (prec + rec)) if (prec + rec) > 0 else 0


def dataset_not_empty(cls, v):
    if len(v) == 0:
        raise ValueError("Dataset must not be empty.")
    if isinstance(v, list):
        dct_v = {}
        for doc in v:
            if doc.identifier in dct_v:
                raise ValueError(
                    f"Got duplicated document identifier: {doc.identifier}."
                )
            else:
                dct_v.update({doc.identifier: doc})
        v = dct_v
    return v