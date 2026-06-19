import numpy as np
import pandas as pd
from scipy.stats import ranksums
from statsmodels.stats.multitest import multipletests

def run_differential_expression(expr, meta):
    results = []

    control = meta[meta["group"] == "Control"]["sample"]
    case = meta[meta["group"] == "Gallstone"]["sample"]

    for gene in expr.index:
        control_vals = expr.loc[gene, control]
        case_vals = expr.loc[gene, case]

        mean_c = np.mean(control_vals)
        mean_g = np.mean(case_vals)

        log2fc = mean_g - mean_c

        stat, p = ranksums(control_vals, case_vals)

        results.append([gene, log2fc, p])

    df = pd.DataFrame(results, columns=["Gene", "log2FC", "pvalue"])

    _, fdr, _, _ = multipletests(df["pvalue"], method="fdr_bh")
    df["FDR"] = fdr

    return df
