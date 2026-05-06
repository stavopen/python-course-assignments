from dilution import calculate_final_volume

try:
    print("--- Lab Dilution Tool (Day 04) ---")
    c1 = float(input("Stock Concentration (C1): "))
    v1 = float(input("Stock Volume (V1): "))
    c2 = float(input("Desired Concentration (C2): "))

    v2, v_add = calculate_final_volume(c1, v1, c2)

    print("\n" + "="*30)
    print(f"Total Final Volume (V2): {v2:.2f}")
    print(f"Volume of Buffer to add: {v_add:.2f}")
    print("="*30)
    print(f"RECIPE: Mix {v1:.2f} of stock with {v_add:.2f} of buffer.")

except ValueError as e:
    print(f"Error: {e}")