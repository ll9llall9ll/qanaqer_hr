N = int(input())

count = 0
numbers = input().split()
for i in range(N):
    num = int(numbers[i])
    if num > 0:
        count += 1

print(count)