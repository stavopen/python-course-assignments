import matplotlib
matplotlib.use("Agg")

import requests
import matplotlib.pyplot as plt
import io
import base64

def get_protein_data(gene_name: str):
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query=gene:{gene_name}+AND+reviewed:true"
        "&format=json"
        "&size=1"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    protein = data["results"][0]
    sequence = protein["sequence"]["value"]

    return {
        "gene": gene_name,
        "protein_id": protein["primaryAccession"],
        "sequence": sequence,
        "length": len(sequence),
    }


def amino_acid_counts(sequence: str):
    counts = {}

    for aa in sequence:
        counts[aa] = counts.get(aa, 0) + 1

    return counts


def gc_content(sequence: str):
    if not sequence:
        return 0

    g = sequence.count("G")
    c = sequence.count("C")

    return round((g + c) / len(sequence) * 100, 2)

def protein_summary(sequence: str):
    return {
        "length": len(sequence),
        "gc_content": gc_content(sequence),
        "composition": amino_acid_counts(sequence)
    }

def create_composition_pie_chart(composition: dict):
    labels = list(composition.keys())
    values = list(composition.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Amino Acid Composition")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()

    buf.seek(0)

    return base64.b64encode(buf.read()).decode("utf-8")