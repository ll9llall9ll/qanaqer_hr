a = input().split()
b = len(a)

for i in range(b):
    a[i] = int(a[i])

first_element = a[0]

for i in range(b - 1):
    a[i] = a[i + 1]

a[-1] = first_element

print(a, end=' ')