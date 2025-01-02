with open("data_set/rosalind_ini5.txt", "r") as file:
    line_num = 1
    for line in file:
        if line_num % 2 == 0:
            print(f"{line.strip()}")
        line_num += 1
