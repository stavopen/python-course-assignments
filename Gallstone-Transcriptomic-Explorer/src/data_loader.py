import pandas as pd

def load_expression_matrix(path):
    df = pd.read_csv(path)
    return df.set_index("Gene")

def load_metadata(path):
    return pd.read_csv(path)
