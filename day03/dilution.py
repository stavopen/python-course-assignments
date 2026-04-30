def calculate_final_volume(c1, v1, c2):
    if c2 == 0:
        raise ValueError("C2 cannot be zero")
    return (c1 * v1) / c2