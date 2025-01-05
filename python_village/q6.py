"""
ID: INI6
Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
"""

with open("data_set/rosalind_ini6.txt", "r") as data_set:
    data_storage = dict()
    for line in data_set:
        word = line.split()
        for w in word:
            data_storage[w] = data_storage.get(w, 0) + 1 # if w not found return 0 & increment by 1
for key, value in data_storage.items():
    print(f"{key} {value}")
