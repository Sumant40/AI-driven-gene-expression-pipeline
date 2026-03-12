from fastapi import FastAPI, UploadFile
import shutil
import pandas as pd
import plotly.express as px
import numpy as np
from backend.run_pipeline import run_pipeline

app = FastAPI()

@app.post("/upload")

async def upload_file(file: UploadFile):

    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = run_pipeline(path)

    df["NegLogP"] = -np.log10(df["P.Value"])

    fig = px.scatter(
        df,
        x="logFC",
        y="NegLogP",
        hover_data=["gene_id"],
        title="Volcano Plot"
    )

    return fig.to_json()