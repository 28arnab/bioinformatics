# Counting DNA Nucleotides Topics: String Algorithms
with open("data_set/rosalind_dna.txt", "r") as data_set:
    data_storage = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotides in data_set:
        for base in nucleotides.strip():
            data_storage[base] += 1
for key, value in data_storage.items():
    print(f" {value}", end=" ")
