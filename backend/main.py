from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import pandas as pd
import plotly.express as px
import numpy as np
import requests

from backend.run_pipeline import run_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_file(file: UploadFile):

    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run pipeline
    run_pipeline(path)

    # Load results
    df = pd.read_csv("results/differential_gene_results.csv")
    top_genes = pd.read_csv("results/top_genes.csv")

    # Volcano plot
    df["NegLogP"] = -np.log10(df["P.Value"])

    fig = px.scatter(
        df,
        x="logFC",
        y="NegLogP",
        hover_data=["gene_id"],
        title="Volcano Plot"
    )

    gene_list = top_genes["gene_id"].tolist()

    # Send genes to n8n
    ai_response = requests.post(
        "http://localhost:5678/webhook/gene-analysis",
        json={"genes": gene_list}
    )

    if ai_response.status_code != 200:
        raise Exception(f"n8n workflow failed: {ai_response.text}")

    # Debug raw response
    raw_text = ai_response.text
    print("RAW AI RESPONSE:", raw_text)

    try:
        ai_data = ai_response.json()
    except:
        ai_data = None

    print("AI JSON:", ai_data)

    ai_outputs = []

    # Case 1: multiple outputs
    if isinstance(ai_data, list):
        for item in ai_data:
            if "output" in item:
                ai_outputs.append(item["output"])

    # Case 2: single output
    elif isinstance(ai_data, dict):
        if "analysis" in ai_data:
            ai_outputs.append(ai_data["analysis"])
        elif "output" in ai_data:
            ai_outputs.append(ai_data["output"])

    # Fallback if parsing fails
    if not ai_outputs:
        ai_outputs.append(raw_text)

    # Combine outputs
    ai_text = "\n\n============================\n\n".join(ai_outputs)

    return {
        "plot": fig.to_json(),
        "genes": top_genes.to_dict(orient="records"),
        "ai": ai_text
    }