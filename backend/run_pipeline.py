import subprocess
import pandas as pd
import requests

def run_pipeline(input_file):

    # Step 1: Preprocess data
    subprocess.run(["python", "backend/preprocess.py", input_file])

    # Step 2: Differential expression
    subprocess.run(["C:/Program Files/R/R-4.5.1/bin/Rscript.exe", "R_scripts/differential_expression.R"])

    # Step 3: Extract top genes
    subprocess.run(["C:/Program Files/R/R-4.5.1/bin/Rscript.exe", "R_scripts/top 100.R"])

    # Step 4: Upload to SQL
    subprocess.run(["python", "backend/upload_sql.py"])

    # Step 5: Read top genes
    df = pd.read_csv("results/top_genes.csv")

    # Step 6: Send genes to n8n AI workflow
    requests.post(
        "http://localhost:5678/webhook/gene-analysis",
        json=df.to_dict(orient="records")
    )

    return df