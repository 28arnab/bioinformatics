"""
ID: RNA
Transcribing DNA into RNA 
Topics: String Algorithms
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

with open ("data_set/rosalind_rna.txt", "r") as data_set:
  bases_list = data_set.read()
  updated_base = ""
  for base in bases_list:
    if base == "T":
      updated_base += "U"
    else:
      updated_base += base
print(updated_base)