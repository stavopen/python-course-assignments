import os
from data_loader import load_expression_matrix, load_metadata
from differential_expression import run_differential_expression
from visualization import volcano_plot
import seaborn as sns
import pandas as pd
from report_generator import generate_report

print("=" * 50)
print("  Gallstone Transcriptomic Explorer")
print("=" * 50)
print()
print("Would you like to:")
print("  1. Run with example data")
print("  2. Use your own data")
print()

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    expr_path = "examples/expression_matrix.csv"
    meta_path = "examples/metadata.csv"
    print("\nLoading example data...")

elif choice == "2":
    print()
    expr_path = input("Enter path to expression matrix CSV: ").strip()
    meta_path = input("Enter path to metadata CSV: ").strip()

    if not os.path.exists(expr_path):
        print(f"Error: could not find {expr_path}")
        exit(1)
    if not os.path.exists(meta_path):
        print(f"Error: could not find {meta_path}")
        exit(1)

    print("\nLoading your data...")

else:
    print("Invalid choice. Please enter 1 or 2.")
    exit(1)

# Load
expr = load_expression_matrix(expr_path)
meta = load_metadata(meta_path)
print(f"Loaded {expr.shape[0]} genes x {expr.shape[1]} samples")

# Run DEG analysis
print("Running differential expression analysis...")
df = run_differential_expression(expr, meta)

# Save results
os.makedirs("results", exist_ok=True)
df.to_csv("results/differential_expression.csv", index=False)
print("Saved results/differential_expression.csv")

# Volcano plot
volcano_plot(df, "results/volcano.png")
print("Saved results/volcano.png")

from visualization import volcano_plot, heatmap

# Heatmap
heatmap(df, expr, meta, "results/heatmap.png")
print("Saved results/heatmap.png")

generate_report(df, "results/report.txt")

print()
print("Done! Results are in the results/ folder.")