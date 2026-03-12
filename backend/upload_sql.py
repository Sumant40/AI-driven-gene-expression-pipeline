import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:sumant@localhost:5432/Bioinformatics")

data = pd.read_csv("results/differential_gene_results.csv")

data.to_sql("gene_results", engine, if_exists="replace")

print("Data uploaded to SQL database.")