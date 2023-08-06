import itertools
import re
from icsr.structure import Icsr, Dataset


# helpers when using the FAERS dataset
def get_icsrs_from_report(report_patient):
    drugs = []
    for drug_report in report_patient["drug"]:
        if "activesubstance" in drug_report and drug_report["activesubstance"]:
            if "activesubstancename" in drug_report["activesubstance"]:
                drugs.append(drug_report["activesubstance"]["activesubstancename"])

    reactions = []
    for reaction_report in report_patient["reaction"]:
        if "reactionmeddrapt" in reaction_report:
            reactions.append(reaction_report["reactionmeddrapt"])

    icsrs = []
    for drug, reaction in itertools.product(drugs, reactions):
        if drug and reaction:
            icsrs.append(Icsr(subject="patient", drug=drug, reaction=reaction))

    return icsrs


# helper when dealing with seq2seq models
def get_icsrs_from_sequence_output(seq_output):
    regex = r"subject:(.*)drugs:(.*)reactions:(.*)"
    matches = re.match(regex, seq_output)

    subject = matches.groups()[0].strip()
    drugs = matches.groups()[1].strip().split(",")
    reactions = matches.groups()[2].strip().split(",")

    icsrs = []
    for drug, reaction in itertools.product(drugs, reactions):
        drug = drug.strip()
        reaction = reaction.strip()

        if drug and reaction:
            icsrs.append(Icsr(subject=subject, drug=drug, reaction=reaction))

    return icsrs


def get_dataset_intersect(ds1, ds2):
    keys1 = set(ds1.keys())
    keys2 = set(ds2.keys())
    intersection = keys1.intersection(keys2)

    new_ds1 = Dataset(
        documents=[doc for ident, doc in ds1.documents.items() if ident in intersection]
    )
    new_ds2 = Dataset(
        documents=[doc for ident, doc in ds2.documents.items() if ident in intersection]
    )

    return new_ds1, new_ds2
