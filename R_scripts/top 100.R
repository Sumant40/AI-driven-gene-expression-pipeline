# Load differential expression results
data <- read.csv("results/differential_gene_results.csv")

# If gene_id is missing but stored as row names
if(!"gene_id" %in% colnames(data)){
    data$gene_id <- rownames(data)
}

# Sort by adjusted p-value
data <- data[order(data$adj.P.Val), ]

# Extract top 100 genes
top_genes <- head(data, 5)

# Move gene_id column to first position
top_genes <- top_genes[, c("gene_id", setdiff(names(top_genes), "gene_id"))]

# Save output
write.csv(
    top_genes,
    "results/top_genes.csv",
    row.names = FALSE
)

print("Top 100 genes saved successfully")