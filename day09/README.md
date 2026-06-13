# Breast Cancer Gene Expression Analysis (Day 09 Assignment)

## Overview

This project analyzes gene expression data from breast cancer tumor and normal tissue samples.  
A machine learning model is built to classify samples as tumor or normal, and PCA is used to visualize the structure of the data.

---

## Dataset

- BC-TCGA-Tumor.txt  
- BC-TCGA-Normal.txt  

Each sample contains gene expression values for thousands of genes.

---

## Project Structure

day09/
│
├── data/
│   ├── BC-TCGA-Tumor.txt
│   └── BC-TCGA-Normal.txt
│
├── main.py
├── important_genes.png
├── pca_final.png
├── pca_downsampled.png
└── README.md

---

## Requirements

Install dependencies:

pip install pandas numpy matplotlib scikit-learn

---

## How to Run

From the day09 folder:

python3 main.py

---

## Workflow

### 1. Data Loading
Tumor and normal gene expression datasets are loaded and combined into one dataset.

### 2. Labeling
- Tumor samples → 1  
- Normal samples → 0  

### 3. Preprocessing
- Convert all values to numeric  
- Replace missing values with 0  
- Clip extreme values (99th percentile)  

### 4. Machine Learning Model
A Random Forest classifier is trained to predict tumor vs normal samples.

---

## Evaluation

The model is evaluated using:
- Accuracy score  
- Classification report  
- 5-fold cross-validation  

---

## Results

- Accuracy: ~1.0  
- Cross-validation accuracy: ~1.0  

This shows strong separation between tumor and normal samples.

---

## Feature Importance

The most important predictive genes are extracted from the model.

Output:
- important_genes.png

---

## PCA Analysis

PCA is applied to the top 50 high-variance genes.

Steps:
- Log transformation  
- Standard scaling  
- PCA to 2 components  

Output:
- pca_downsampled.png  

---

## Key Insight

Tumor and normal samples show strong separation in gene expression space, indicating clear biological differences.

---

## AI Usage

AI was used to assist with debugging, preprocessing, and improving the machine learning pipeline.
