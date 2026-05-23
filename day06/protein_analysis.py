import requests
from collections import Counter

protein_name = input("Enter protein name: ")

url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{protein_name}+AND+organism_id:9606+AND+reviewed:true&format=json&size=1"

response = requests.get(url)

if response.status_code != 200:
    print("Error retrieving data.")
    exit()

data = response.json()

if not data["results"]:
    print("No protein found.")
    exit()

protein = data["results"][0]

protein_id = protein["primaryAccession"]

try:
    protein_description = protein["proteinDescription"]["recommendedName"]["fullName"]["value"]
except KeyError:
    protein_description = "No description available"

organism = protein["organism"]["scientificName"]
is_human = organism == "Homo sapiens"
print(f"Human protein: {is_human}")

sequence = protein["sequence"]["value"]

length = protein["sequence"]["length"]

print("\nProtein Information")
print("-------------------")
print(f"Protein ID: {protein_id}")
print(f"Description: {protein_description}")
print(f"Organism: {organism}")
print(f"Sequence Length: {length}")

aa_counts = Counter(sequence)

print("\nMost common amino acids:")

for aa, count in aa_counts.most_common(5):
    print(f"{aa}: {count}")

hydrophobic = "AILMFWVY"

hydrophobic_count = sum(aa_counts[aa] for aa in hydrophobic)

hydrophobic_percent = (hydrophobic_count / length) * 100

print(f"\nHydrophobic amino acids: {hydrophobic_percent:.2f}%")
acidic = "DE"
basic = "KRH"

acidic_count = sum(aa_counts[aa] for aa in acidic)
basic_count = sum(aa_counts[aa] for aa in basic)

acidic_percent = (acidic_count / length) * 100
basic_percent = (basic_count / length) * 100

print(f"\nAcidic amino acids (D,E): {acidic_percent:.2f}%")
print(f"Basic amino acids (K,R,H): {basic_percent:.2f}%")
