import math
k = int(input())
m = int(input())
n = int(input())


if n % k > k // 2 or n < k or n % k == 0:
    f = math.ceil(n/k)
    x = 2 * m * f
    print(x)
else:
    f = math.floor(n/k)
    x = 2 *m * f + m
    print(x)