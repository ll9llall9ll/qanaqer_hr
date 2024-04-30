numbers = input().split()
count = 0

for i in numbers:
    c = int(i)
    if c > 0:
        count += 1
print(count)
