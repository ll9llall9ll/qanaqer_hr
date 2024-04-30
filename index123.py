a = input().split()
num = input().split()
a.insert(int(num[0]), num[1])  
for i in (a):
    print(i, end = ' ')