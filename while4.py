#o
numbers = input().split()
erk = len(numbers)

for i in range(0,erk):
    l = numbers[i + 1] 
    numbers[i + 1] = numbers[i]
    numbers[i] = l


print(numbers)

