print("Dilution Calculator")

C1 = float(input("Enter stock concentration: "))
V1 = float(input("Enter stock volume: "))
C2 = float(input("Enter desired concentration: "))

V2 = (C1 * V1) / C2

print("Final volume needed:", V2)