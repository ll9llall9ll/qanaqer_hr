def get_odd_numbers(num):
    odd_numbers = []
    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

a = int(input())
b = get_odd_numbers(a)

for num in b:
    print(num, end=" ") 

