color = int(input())

if color == 0:
    print("green")
elif color >= 10:
    if color % 2 == 0:
        print("Black")
    else:
        print("Red")
    