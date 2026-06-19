"""
generate_example_data.py

Generates realistic simulated RNA-seq expression data for the
Gallstone Transcriptomic Explorer examples folder.

Run from the project root:
    python generate_example_data.py

Produces:
  examples/expression_matrix.csv   - log2 normalized expression values
  examples/metadata.csv            - sample annotations with clinical fields
"""

import numpy as np
import pandas as pd
import os

np.random.seed(42)

N_GENES = 5000
N_UP = 150       # upregulated in Gallstone
N_DOWN = 150     # downregulated in Gallstone
N_CONTROL = 6
N_CASE = 6
N_SAMPLES = N_CONTROL + N_CASE

# --- Sample names and metadata ---
samples = [f"Sample{i+1}" for i in range(N_SAMPLES)]
groups = ["Control"] * N_CONTROL + ["Gallstone"] * N_CASE

metadata = pd.DataFrame({
    "sample": samples,
    "group": groups,
    "sex": np.random.choice(["M", "F"], N_SAMPLES),
    "age": np.random.randint(40, 75, N_SAMPLES),
    "bmi": np.round(np.random.uniform(22, 38, N_SAMPLES), 1),
    "diabetes": np.random.choice(["yes", "no"], N_SAMPLES, p=[0.3, 0.7]),
    "statin_use": np.random.choice(["yes", "no"], N_SAMPLES, p=[0.4, 0.6]),
})

# --- Expression matrix (log2-normalized values) ---
gene_names = [f"GENE_{i}" for i in range(N_GENES)]
expr = np.random.normal(loc=5.0, scale=1.0, size=(N_GENES, N_SAMPLES))

# Spike-in upregulated genes (higher in Gallstone)
up_indices = np.random.choice(N_GENES, N_UP, replace=False)
for idx in up_indices:
    fold_change = np.random.uniform(2.0, 4.0)
    expr[idx, N_CONTROL:] += fold_change
    expr[idx] += np.random.normal(0, 0.2, N_SAMPLES)

# Spike-in downregulated genes (lower in Gallstone)
remaining = list(set(range(N_GENES)) - set(up_indices))
down_indices = np.random.choice(remaining, N_DOWN, replace=False)
for idx in down_indices:
    fold_change = np.random.uniform(2.0, 4.0)
    expr[idx, N_CONTROL:] -= fold_change
    expr[idx] += np.random.normal(0, 0.2, N_SAMPLES)

expr = np.clip(expr, 0, 15)

expr_df = pd.DataFrame(expr, index=gene_names, columns=samples)
expr_df.index.name = "Gene"

# --- Save ---
os.makedirs("examples", exist_ok=True)
expr_df.to_csv("examples/expression_matrix.csv")
metadata.to_csv("examples/metadata.csv", index=False)

print(f"Saved examples/expression_matrix.csv  ({N_GENES} genes x {N_SAMPLES} samples)")
print(f"Saved examples/metadata.csv            ({N_SAMPLES} samples)")
print(f"Spiked-in DEGs: {N_UP} upregulated, {N_DOWN} downregulated")
