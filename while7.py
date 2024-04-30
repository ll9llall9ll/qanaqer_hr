# chkrknvox tveri qanaak
numbers = input().split()
num = 1  

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        num += 1

print(num)