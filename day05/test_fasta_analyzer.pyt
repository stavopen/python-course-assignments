from fasta_analyzer import calculate_gc, is_valid, read_fasta


def test_calculate_gc():
    assert calculate_gc("GCGC") == 100.0
    assert calculate_gc("ATAT") == 0.0
    assert calculate_gc("") == 0


def test_is_valid():
    assert is_valid("ATGC") is True
    assert is_valid("ATGX") is False


def test_read_fasta():
    test_file = "data/sequences.fasta"
    sequences = read_fasta(test_file)

    assert isinstance(sequences, dict)
    assert len(sequences) > 0
