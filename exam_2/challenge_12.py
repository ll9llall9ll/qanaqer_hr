a = input().split()
b = len(a)
k = 0
for i in range(len(a)):
    if a[i] in b:
        k += 1
        print(k)