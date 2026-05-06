import sys
from dilution import calculate_final_volume

if len(sys.argv) != 4:
    print("Usage: python3 dilution_args.py <C1> <V1> <C2>")
    sys.exit(1)

try:
    c1 = float(sys.argv[1])
    v1 = float(sys.argv[2])
    c2 = float(sys.argv[3])

    v2, v_add = calculate_final_volume(c1, v1, c2)

    print(f"V2: {v2:.2f}, Buffer to add: {v_add:.2f}")
except ValueError as e:
    print(f"Error: {e}")