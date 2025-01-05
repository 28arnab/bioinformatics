"""
ID: INI5
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

with open("data_set/rosalind_ini5.txt", "r") as file:
    line_num = 1
    for line in file:
        if line_num % 2 == 0:
            print(f"{line.strip()}")
        line_num += 1
