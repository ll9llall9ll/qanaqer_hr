a = input()
b = a.split()
c = len(b)

krknvox = []
unikal = []
for i in b:
    if i not in krknvox and i not in unikal:
        unikal.append(i)
    else:
        if i in unikal:
            unikal.remove(i)
            krknvox.append(i)
print(unikal)