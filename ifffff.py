a = int(input())

if (a // 4 == 0 and a // 100 != 0) or (a // 400 == 0):
    v = "YES"
else:
    v = "NO"

print(v)