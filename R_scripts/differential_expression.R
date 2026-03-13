library(limma)

# -----------------------------
# 1. Load dataset
# -----------------------------

data <- read.csv("results/processed_gene_data.csv",
                 check.names = FALSE)

# Extract gene IDs
gene_ids <- data[,1]

# Expression matrix
expr <- as.matrix(data[,-1])

# Convert to numeric
expr <- apply(expr, 2, as.numeric)

# -----------------------------
# 2. Check matrix orientation
# -----------------------------

# If genes appear as columns (rare case)
if(nrow(expr) < ncol(expr)) {
  expr <- t(expr)
}

# Number of samples
num_samples <- ncol(expr)

cat("Total samples detected:", num_samples, "\n")

# -----------------------------
# 3. Automatically create groups
# -----------------------------

# Default: split samples into two groups
group <- factor(rep(c("Control","Disease"),
                    length.out = num_samples))

cat("Group distribution:\n")
print(table(group))

# -----------------------------
# 4. Build design matrix
# -----------------------------

design <- model.matrix(~group)

# Safety check
if(nrow(design) != ncol(expr)){
  stop("Design matrix and expression matrix dimensions do not match.")
}

# -----------------------------
# 5. Fit linear model
# -----------------------------

fit <- lmFit(expr, design)

# Empirical Bayes moderation
fit <- eBayes(fit)

# -----------------------------
# 6. Extract differential genes
# -----------------------------

results <- topTable(fit,
                    coef = 2,
                    number = Inf,
                    adjust.method = "fdr")

# Add gene IDs
results$gene_id <- gene_ids

# Move gene_id column to front
results <- results[, c("gene_id",
                       setdiff(names(results), "gene_id"))]

# -----------------------------
# 7. Save results
# -----------------------------

write.csv(results,
          "results/differential_gene_results.csv",
          row.names = FALSE)

cat("Differential expression analysis completed.\n")