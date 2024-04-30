number = input()

if len(number) != 3:
    print("Input should be a 3-digit number.")
else:
    print(number)
    print(number[0] + number[2] + number[1])
    print(number[1] + number[0] + number[2])
    print(number[1] + number[2] + number[0])
    print(number[2] + number[0] + number[1])
    print(number[2] + number[1] + number[0])

 

