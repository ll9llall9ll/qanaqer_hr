#T-ezaki
a = input().split()
b = len(a)
unikal = []
krknvox = []

for i in range(b):
    if a[i] not in unikal and a[i] not in krknvox:
        unikal.append(a[i])
    elif a[i] in unikal:
            unikal.remove(a[i])
            krknvox.append(a[i])

for num in a:
    if num in unikal:
        print(num, end=" ")