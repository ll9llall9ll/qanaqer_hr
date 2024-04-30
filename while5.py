#min and max
numbers = input().split()  
erk = len(numbers)
datark = []
max_index = 0
min_index = 0

for i in range(erk):
    k = int(numbers[i])
    datark.append(k)
    if k > datark[max_index]:
        max_index = i
    if k < datark[min_index]:
        min_index = i

k = datark[max_index]
datark[max_index] = datark[min_index]
datark[min_index] = k
for i in range(erk):
    print(datark[i], end=" ")
    print("test")