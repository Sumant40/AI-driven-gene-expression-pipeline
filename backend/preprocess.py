import pandas as pd
import numpy as np
import sys

# Get input file path from command line
input_file = sys.argv[1]

# Load dataset
data = pd.read_csv(input_file, sep="\t", comment="!")

print("Dataset loaded")
print(data.head())

# Remove missing values
data = data.dropna()

# Log transformation
data_log = np.log2(data.iloc[:,1:] + 1)

# Add gene IDs column
data_log.insert(0, "GeneID", data.iloc[:,0])

# Save processed data
output_file = "results/processed_gene_data.csv"

data_log.to_csv(output_file, index=False)

print("Data preprocessing completed")
print("Saved to:", output_file)