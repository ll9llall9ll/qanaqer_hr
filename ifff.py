a = []

for i in range(10):
    a.append(int(input()))

for i in range(2,8):
    if a[i] % 2 == 0 and a[i] % 6 != 0 and a[i - 1] % 6 == 0 and a[i - 2] % 2 == 0:
        print("Activate emergency protocol!")
        break
    if a[i] % 2 == 0 and a[i] % 6 != 0 and a[i + 1] % 6 == 0 and a[i + 2] % 2 == 0:
        print("Activate emergency protocol!")
        break
else:
    if a[1] % 2 == 0 and a[1] % 6 != 0 and a[0] % 6 == 0:
        print("Activate emergency protocol!")
    elif a[1] % 2 == 0 and a[1] % 6 != 0 and a[2] % 6 == 0 and a[3] % 2 == 0:
        print("Activate emergency protocol!")
    elif a[0] % 2 == 0 and a[0] % 6 != 0 and a[1] % 6 == 0 and a[1] % 2 == 0:
        print("Activate emergency protocol!")
    elif a[8] % 2 == 0 and a[8] % 6 != 0 and a[9] % 6 == 0:
        print("Activate emergency protocol!")
    elif a[8] % 2 == 0 and a[8] % 6 != 0 and a[7] % 6 == 0 and a[6] % 2 == 0:
        print("Activate emergency protocol!")
    elif a[9] % 2 == 0 and a[9] % 6 != 0 and a[8] % 6 == 0 and a[7] % 2 == 0:
        print("Activate emergency protocol!")
    else:
        print("Check complete, blueberries are growing!")