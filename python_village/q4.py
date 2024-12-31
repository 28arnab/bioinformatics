def sum_of_odds(a, b):
    if a % 2 == 0:
        a += 1
    total_sum = 0
    for num in range(a, b + 1, 2):
        total_sum += num
    return total_sum


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a < b < 10000:
    print(sum_of_odds(a, b))
else:
    print("Usage: 1st number < 2nd number < 10000")
