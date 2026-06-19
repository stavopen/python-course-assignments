import os
from datetime import datetime

def generate_report(df, output_path, fdr_threshold=0.2, fc_threshold=1.0):

    sig = df[(df["FDR"] < fdr_threshold) & (abs(df["log2FC"]) > fc_threshold)]
    up = sig[sig["log2FC"] > 0].sort_values("FDR")
    down = sig[sig["log2FC"] < 0].sort_values("FDR")

    lines = []
    lines.append("=" * 55)
    lines.append("   Gallstone Transcriptomic Explorer — Report")
    lines.append("=" * 55)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("--- Summary ---")
    lines.append(f"Total genes analyzed:       {len(df)}")
    lines.append(f"FDR threshold:              < {fdr_threshold}")
    lines.append(f"log2FC threshold:           > {fc_threshold}")
    lines.append(f"Significant DEGs:           {len(sig)}")
    lines.append(f"  Upregulated in Gallstone: {len(up)}")
    lines.append(f"  Downregulated in Gallstone: {len(down)}")
    lines.append("")
    lines.append("--- Top 10 Upregulated Genes ---")
    for _, row in up.head(10).iterrows():
        lines.append(f"  {row['Gene']:<15} log2FC={row['log2FC']:+.2f}  FDR={row['FDR']:.3f}")
    lines.append("")
    lines.append("--- Top 10 Downregulated Genes ---")
    for _, row in down.head(10).iterrows():
        lines.append(f"  {row['Gene']:<15} log2FC={row['log2FC']:+.2f}  FDR={row['FDR']:.3f}")
    lines.append("")
    lines.append("=" * 55)

    report_text = "\n".join(lines)

    # Print to terminal
    print(report_text)

    # Save to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report_text)

    print(f"\nReport saved to {output_path}")