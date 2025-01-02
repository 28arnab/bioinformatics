with open("data_set/rosalind_ini6.txt", "r") as data_set:
    data_storage = dict()
    for line in data_set:
        word = line.split()
        for w in word:
            data_storage[w] = data_storage.get(w, 0) + 1
for key, value in data_storage.items():
    print(f"{key} {value}")
