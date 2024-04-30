list = input()
og_list = input()
b = list.split()
h = og_list.split()
n = len(h)
c = len(b)
for i in range(0,n-1):
    # print(h[i],h[i+1])
    m = int(h[i])
    l = h[i + 1]
    p = len(l)
    b.append(l)
for i in range(p+c - 1,2, - 1):
    f = b[i]
    b[i] = b[i-1]
    b[i-1] = f
for num in b:
    print(num,end = ' ')