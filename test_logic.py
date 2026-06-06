from protein_logic import amino_acid_counts


def test_amino_acid_counts_basic():
    seq = "AAABC"
    result = amino_acid_counts(seq)

    assert result["A"] == 3
    assert result["B"] == 1
    assert result["C"] == 1