# AI-Driven Gene Expression Analysis Pipeline for Disease Biomarker Discovery

## Project Overview

This project implements a complete **bioinformatics data pipeline**
designed to analyze gene expression datasets and identify potential
disease biomarkers. The system integrates multiple technologies
including **Python, R, SQL, n8n automation workflows, AI-based gene
interpretation, and interactive data visualization**.

The pipeline automates the full lifecycle of transcriptomic analysis:

1.  Dataset ingestion
2.  Data preprocessing
3.  Differential gene expression analysis
4.  Biomarker extraction
5.  Database storage
6.  AI-powered biological interpretation
7.  Visualization through an interactive dashboard
8.  Workflow automation using n8n

The system demonstrates an **end‑to‑end bioinformatics workflow
architecture**, which is valuable for applications in:

-   Bioinformatics
-   Computational biology
-   Biotechnology research
-   Biomedical data science
-   Precision medicine analytics

------------------------------------------------------------------------

# Biological Problem

Many complex diseases such as cancer, autoimmune disorders, and
neurological conditions arise due to **changes in gene expression
levels**.

Gene expression analysis helps identify:

• **Upregulated genes** -- genes whose expression increases in disease\
• **Downregulated genes** -- genes whose expression decreases in disease

These genes can serve as:

-   Diagnostic biomarkers
-   Therapeutic drug targets
-   Indicators of disease progression
-   Molecular signatures of biological pathways

Modern transcriptomic experiments measure the expression of **thousands
of genes simultaneously**, making computational analysis essential.

Public repositories such as:

-   NCBI GEO
-   TCGA

contain large collections of gene expression datasets that can be
analyzed to discover new biomarkers.

------------------------------------------------------------------------

# System Architecture

The project integrates several technologies across different layers.

Frontend\
HTML + JavaScript + Plotly

Backend API\
Python FastAPI

Data Processing\
Python (Pandas, NumPy)

Statistical Analysis\
R (limma package)

Automation Workflow\
n8n

Database\
PostgreSQL

AI Interpretation\
Ollama + LLM through n8n

Visualization\
Plotly dashboard

The architecture follows a **modern ETL bioinformatics pipeline
design**.

------------------------------------------------------------------------

# Pipeline Workflow

The system follows an automated sequence of operations.

## Step 1 --- Dataset Upload

Users upload a gene expression dataset through the web interface.

The frontend interface allows researchers to select a dataset and run
the analysis pipeline automatically.

Uploaded datasets are sent to the FastAPI backend.

------------------------------------------------------------------------

# Step 2 --- Data Preprocessing (Python)

The preprocessing script performs several critical data preparation
steps.

### Working Principle

Raw gene expression data often contains:

-   Missing values
-   Large dynamic ranges
-   Non‑numeric artifacts

To ensure reliable statistical analysis, the preprocessing stage
performs:

1.  Dataset loading
2.  Missing value removal
3.  Log2 transformation
4.  Gene identifier extraction
5.  Export of processed dataset

Log transformation stabilizes variance across genes and improves
statistical modeling.

Output file:

results/processed_gene_data.csv

------------------------------------------------------------------------

# Step 3 --- Differential Gene Expression Analysis (R)

Statistical analysis is performed using the **limma (Linear Models for
Microarray Data)** package in R.

### Working Principle

Limma applies linear modeling to detect genes that show statistically
significant differences between experimental groups.

The workflow includes:

1.  Expression matrix construction
2.  Experimental group assignment
3.  Linear model fitting
4.  Empirical Bayes variance moderation
5.  Multiple testing correction

The statistical model used is:

Expression = β0 + β1(Disease) + ε

Where

β0 = baseline gene expression\
β1 = effect of disease condition

Genes with significant β1 values represent differentially expressed
genes.

Output:

results/differential_gene_results.csv

------------------------------------------------------------------------

# Step 4 --- Top Biomarker Extraction

The next script ranks genes based on **adjusted p-values (False
Discovery Rate)**.

Genes with the lowest adjusted p-values are considered the most
statistically significant.

The pipeline extracts the **top biomarkers** and saves them to:

results/top_genes.csv

These genes represent the most promising candidates for disease
biomarkers.

------------------------------------------------------------------------

# Step 5 --- Database Storage

Results are stored in a PostgreSQL database using SQLAlchemy.

The database stores:

-   Gene identifiers
-   Fold change values
-   Statistical significance
-   Expression metrics

Database table:

gene_results

This allows downstream querying, reproducibility, and integration with
other analysis tools.

------------------------------------------------------------------------

# Step 6 --- AI-Based Gene Interpretation

The pipeline integrates **AI-driven biological interpretation** using an
automated workflow in n8n.

The top genes are sent to an AI model which generates biological
insights such as:

-   Gene function
-   Associated diseases
-   Involved biological pathways
-   Potential biomarker relevance

This step transforms raw statistical output into **biologically
meaningful explanations**.

------------------------------------------------------------------------

# n8n Workflow

The automation workflow is implemented using **n8n**, a visual workflow
automation platform.

### Workflow Components

1.  **Webhook Node**

Receives gene lists from the backend API.

2.  **Code Node (JavaScript)**

Extracts gene identifiers from the request payload.

3.  **Split Node**

Processes each gene individually.

4.  **AI Agent Node**

Sends gene identifiers to an LLM model for interpretation.

The AI prompt asks for:

-   Gene function
-   Disease associations
-   Biological pathways
-   Biomarker potential

5.  **Ollama Model Node**

Runs a local language model (Phi‑3).

6.  **Edit Fields Node**

Formats the AI output.

7.  **Respond to Webhook Node**

Returns interpretations back to the backend API.

This automation allows **batch biological annotation of genes**.

------------------------------------------------------------------------

# Step 7 --- Visualization Dashboard

The frontend dashboard displays analysis results interactively.

The interface includes:

• Dataset upload interface\
• Volcano plot visualization\
• Table of top genes\
• AI interpretation panel

### Volcano Plot

A volcano plot visualizes statistical significance versus fold change.

X‑axis\
log fold change

Y‑axis\
−log10(p‑value)

Interpretation:

Top right → significantly upregulated genes\
Top left → significantly downregulated genes

These genes represent potential biomarkers.

The visualization is implemented using **Plotly.js**.

------------------------------------------------------------------------

# Technology Stack

Frontend

HTML\
JavaScript\
Plotly

Backend

FastAPI\
Python

Data Processing

Pandas\
NumPy

Statistical Analysis

R\
limma package

Database

PostgreSQL\
SQLAlchemy

Automation

n8n

AI Integration

Ollama\
LLM agents

------------------------------------------------------------------------

# How to Run the Project

## 1 Install Python dependencies

pip install -r requirements.txt

## 2 Start the FastAPI server

uvicorn backend.main:app --reload

Server runs at

http://localhost:8000

## 3 Start n8n

n8n start

n8n webhook endpoint

http://localhost:5678/webhook/gene-analysis

## 4 Run Ollama model

ollama run phi3

## 5 Open frontend

Open index.html in the browser.

Upload a gene expression dataset and run the analysis.

------------------------------------------------------------------------

# Example Dataset

The project can analyze GEO datasets such as

GSE15852

Breast cancer gene expression dataset.

These datasets typically contain:

-   thousands of genes
-   multiple disease samples
-   multiple control samples

------------------------------------------------------------------------

# Key Features

Fully automated bioinformatics pipeline

AI-assisted biological interpretation

Statistical gene expression analysis

Interactive biomarker visualization

Workflow automation using n8n

Modular microservice architecture

------------------------------------------------------------------------

# Future Improvements

Potential extensions of the system include:

-   Multi‑dataset meta‑analysis
-   Pathway enrichment analysis
-   Gene ontology annotation
-   Cloud deployment
-   Deep learning based biomarker prediction
-   Integration with TCGA datasets

------------------------------------------------------------------------

# Applications

This system can be used for:

Biomedical research

Drug discovery

Precision medicine

Disease biomarker discovery

Computational biology education

------------------------------------------------------------------------

# Author

Sumant J

Bioengineering and Bioinformatics Projects
