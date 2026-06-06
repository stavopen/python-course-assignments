from fastapi import FastAPI
from protein_logic import get_protein_data, amino_acid_counts
from fastapi.responses import HTMLResponse
from protein_logic import create_composition_pie_chart

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Day 08 Protein Analyzer API"}


@app.get("/protein/{gene}")
def protein(gene: str):
    data = get_protein_data(gene)

    if data is None:
        return {"error": "Protein not found"}

    data["composition"] = amino_acid_counts(data["sequence"])

    return data

from protein_logic import get_protein_data, protein_summary


@app.get("/protein/{gene}")
def protein(gene: str):
    data = get_protein_data(gene)

    if data is None:
        return {"error": "Protein not found"}

    summary = protein_summary(data["sequence"])

    return {
        "gene": data["gene"],
        "protein_id": data["protein_id"],
        "analysis": summary
    }

@app.get("/protein/{gene}/stats")
def protein_stats(gene: str):
    data = get_protein_data(gene)

    if data is None:
        return {"error": "Protein not found"}

    return protein_summary(data["sequence"])

@app.get("/protein/{gene}/plot", response_class=HTMLResponse)
def protein_plot(gene: str):
    data = get_protein_data(gene)

    if data is None:
        return HTMLResponse("<h1>Protein not found</h1>")

    composition = amino_acid_counts(data["sequence"])
    img_base64 = create_composition_pie_chart(composition)

    html = f"""
    <html>
        <body>
            <h2>Protein: {gene}</h2>
            <img src="data:image/png;base64,{img_base64}" />
        </body>
    </html>
    """

    return HTMLResponse(html)