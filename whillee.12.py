numbers = input().split() 
num = input().split()  
index = int(num[0])
numbers.append(num[1])
a = len(numbers)
for i in range(a - 1, index, -1):
    d = numbers[i]
    numbers[i] = numbers[i - 1]
    numbers[i - 1] = d
for number in numbers:
    print(number, end = ' ')
