import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text
import seaborn as sns
import pandas as pd

def volcano_plot(df, output_path, title="Gallstone vs Control"):

    plt.figure(figsize=(9, 6))

    x = df["log2FC"]
    y = -np.log10(df["FDR"] + 1e-10)

    jitter = np.random.normal(0, 0.02, size=len(y))
    colors = ["red" if (abs(xi) > 1 and yi > -np.log10(0.2)) else "steelblue" for xi, yi in zip(x, y)]
    plt.scatter(x, y + jitter, c=colors, alpha=0.5, s=10)

    plt.axvline(1, color="grey", linestyle="--")
    plt.axvline(-1, color="grey", linestyle="--")
    plt.axhline(-np.log10(0.2), color="red", linestyle="--")

    # Top 10 upregulated
    up = df[df["log2FC"] > 1].nsmallest(10, "FDR")
    # Top 10 downregulated
    down = df[df["log2FC"] < -1].nsmallest(10, "FDR")

    texts = []
    for _, row in up.iterrows():
        texts.append(plt.text(row["log2FC"], -np.log10(row["FDR"] + 1e-10),
                     row["Gene"], fontsize=6, color="darkred"))

    for _, row in down.iterrows():
        texts.append(plt.text(row["log2FC"], -np.log10(row["FDR"] + 1e-10),
                     row["Gene"], fontsize=6, color="darkblue"))

    adjust_text(texts, arrowprops=dict(arrowstyle="-", color="grey", lw=0.5))

    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10(FDR)")
    plt.title(title)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def heatmap(df, expr, meta, output_path, n_genes=50):

    # Get top 25 up and top 25 down by FDR
    up = df[df["log2FC"] > 1].nsmallest(25, "FDR")
    down = df[df["log2FC"] < -1].nsmallest(25, "FDR")
    top_genes = pd.concat([up, down])["Gene"].tolist()

    # Subset expression matrix
    expr_subset = expr.loc[top_genes]

    # Create sample color bar (Control=blue, Gallstone=red)
    group_colors = meta.set_index("sample")["group"].map({
        "Control": "steelblue",
        "Gallstone": "salmon"
    })

    # Plot
    g = sns.clustermap(
        expr_subset,
        col_colors=group_colors,
        cmap="RdBu_r",
        z_score=0,
        figsize=(10, 12),
        xticklabels=True,
        yticklabels=True,
        dendrogram_ratio=0.1,
        cbar_pos=(0.02, 0.8, 0.03, 0.15)
    )

    g.ax_heatmap.set_xlabel("Samples")
    g.ax_heatmap.set_ylabel("Genes")
    g.fig.suptitle("Top DEGs Heatmap", y=1.01, fontsize=14)

    g.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()