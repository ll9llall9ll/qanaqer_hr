#unikal
a = input().split()
unikal = []

for i in range(len(a)):
    if a[i] not in unikal:
        unikal.append(a[i])

erk = len(unikal)
print(erk)