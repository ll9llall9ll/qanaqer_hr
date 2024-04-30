#N
a = input()
b = a.split()
erk = len(b)

for i in range(0, erk - 1, 2):
    num = b[i]
    b[i] = b[i + 1]
    b[i + 1] = num

for num in b:
        print(num, end=' ')
