def calculate_final_volume(c1, v1, c2):
    """
    Calculates the final volume (V2) and the volume of buffer to add.
    Formula: C1 * V1 = C2 * V2
    """
    if c2 == 0:
        raise ValueError("C2 cannot be zero")
    
    v2 = (c1 * v1) / c2
    v_add = v2 - v1
    
    if v_add < 0:
        raise ValueError("Desired concentration (C2) cannot be higher than stock (C1)")
        
    return v2, v_add