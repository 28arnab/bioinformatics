"""
ID: DNA
Problem Name: Counting DNA Nucleotides 
Topics: String Algorithms
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

with open("data_set/rosalind_dna.txt", "r") as data_set:
    data_storage = {"A": 0, "C": 0, "G": 0, "T": 0} # initialized keys and values within the dictionary
    for nucleotides in data_set:
        for base in nucleotides.strip():
            data_storage[base] += 1
for value in data_storage.values():
    print(f" {value}", end=" ")
