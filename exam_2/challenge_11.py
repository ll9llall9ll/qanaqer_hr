a = input().split()
max_length = 0


for i in a:  
    if len(i) > max_length:
        max_length = len(i)
        res = i

print(res)