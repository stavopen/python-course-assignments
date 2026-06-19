import pytest
import pandas as pd
import numpy as np
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from data_loader import load_expression_matrix, load_metadata
from differential_expression import run_differential_expression
from visualization import volcano_plot, heatmap
from report_generator import generate_report

EXPR_PATH = "examples/expression_matrix.csv"
META_PATH = "examples/metadata.csv"


# --- data_loader tests ---

def test_load_expression_matrix_shape():
    expr = load_expression_matrix(EXPR_PATH)
    assert expr.shape[0] > 0, "Expression matrix should have genes"
    assert expr.shape[1] > 0, "Expression matrix should have samples"

def test_load_expression_matrix_index():
    expr = load_expression_matrix(EXPR_PATH)
    assert expr.index.name == "Gene"

def test_load_metadata_columns():
    meta = load_metadata(META_PATH)
    assert "sample" in meta.columns
    assert "group" in meta.columns

def test_load_metadata_groups():
    meta = load_metadata(META_PATH)
    groups = meta["group"].unique()
    assert "Control" in groups
    assert "Gallstone" in groups


# --- differential_expression tests ---

def test_deg_output_columns():
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    assert "Gene" in df.columns
    assert "log2FC" in df.columns
    assert "pvalue" in df.columns
    assert "FDR" in df.columns

def test_deg_output_length():
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    assert len(df) == len(expr)

def test_fdr_range():
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    assert df["FDR"].between(0, 1).all(), "FDR values must be between 0 and 1"

def test_has_significant_degs():
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    sig = df[(df["FDR"] < 0.2) & (abs(df["log2FC"]) > 1)]
    assert len(sig) > 0, "Should detect significant DEGs in example data"


# --- visualization tests ---

def test_volcano_plot_saves_file(tmp_path):
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    out = str(tmp_path / "volcano.png")
    volcano_plot(df, out)
    assert os.path.exists(out)

def test_heatmap_saves_file(tmp_path):
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    out = str(tmp_path / "heatmap.png")
    heatmap(df, expr, meta, out)
    assert os.path.exists(out)


# --- report_generator tests ---

def test_report_saves_file(tmp_path):
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    out = str(tmp_path / "report.txt")
    generate_report(df, out)
    assert os.path.exists(out)

def test_report_contains_summary(tmp_path):
    expr = load_expression_matrix(EXPR_PATH)
    meta = load_metadata(META_PATH)
    df = run_differential_expression(expr, meta)
    out = str(tmp_path / "report.txt")
    generate_report(df, out)
    with open(out) as f:
        content = f.read()
    assert "Total genes analyzed" in content
    assert "Upregulated" in content
    assert "Downregulated" in content