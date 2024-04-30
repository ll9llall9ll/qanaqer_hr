a = int(input())
b = int(input())

c = int(input())
d = int(input())
e = int(input())

if (a > c or a > d or a > e) and (b > c or b > d or b > e):
    print("Great, you've stayed within the limits!")
else:
    print("We need to cut the spending the next month")
