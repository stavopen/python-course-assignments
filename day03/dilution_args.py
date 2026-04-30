import sys
from dilution import calculate_final_volume

c1 = float(sys.argv[1])
v1 = float(sys.argv[2])
c2 = float(sys.argv[3])

print(calculate_final_volume(c1, v1, c2))