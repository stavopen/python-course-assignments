import csv


def read_fasta(filename):
    sequences = {}
    current_name = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                current_name = line[1:]
                sequences[current_name] = ""
            else:
                sequences[current_name] += line.upper()

    return sequences


def calculate_gc(sequence):
    sequence = sequence.upper()

    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")
    return round((gc_count / len(sequence)) * 100, 2)


def is_valid(sequence):
    sequence = sequence.upper()
    valid_bases = {"A", "T", "G", "C"}
    return all(base in valid_bases for base in sequence)


def analyze_sequences(sequences):
    results = []

    for name, sequence in sequences.items():
        result = {
            "Sequence": name,
            "Length": len(sequence),
            "GC%": calculate_gc(sequence),
            "Valid": is_valid(sequence)
        }
        results.append(result)

    return results


def save_to_csv(results, output_file):
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Sequence", "Length", "GC%", "Valid"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)


def print_summary(results):
    print("\n===== FASTA ANALYSIS SUMMARY =====\n")

    for row in results:
        print(
            f"{row['Sequence']} | "
            f"Length: {row['Length']} | "
            f"GC%: {row['GC%']} | "
            f"Valid: {row['Valid']}"
        )

    print("\n==================================\n")


def main():
    input_file = "data/sequences.fasta"
    output_file = "output/analysis_results.csv"

    sequences = read_fasta(input_file)
    results = analyze_sequences(sequences)

    save_to_csv(results, output_file)
    print_summary(results)

    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()