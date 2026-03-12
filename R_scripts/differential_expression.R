library(limma)

# Load processed dataset
data <- read.csv("results/processed_gene_data.csv")

# First column contains gene IDs
gene_ids <- data[,1]

# Expression matrix
expr <- as.matrix(data[,-1])

# Example group assignment
# Adjust according to your dataset
group <- factor(c(rep("Control", 43), rep("Disease", 43)))

# Design matrix
design <- model.matrix(~group)

# Fit model
fit <- lmFit(expr, design)

# Apply empirical Bayes
fit <- eBayes(fit)

# Extract results
results <- topTable(fit, coef=2, number=Inf)

# Add gene IDs
results$gene_id <- gene_ids

# Move gene_id to first column
results <- results[, c("gene_id", setdiff(names(results), "gene_id"))]

# Save results
write.csv(
  results,
  "results/differential_gene_results.csv",
  row.names = FALSE
)

print("Differential expression results saved")