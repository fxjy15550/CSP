# n = int(input())
# a = list(map(int, input().split()))

from math import sqrt


n = 7
a = [-4, 293, 0, -22, 12, 654, 1000]

mu = sum(a) / n
sigma = 0.0
for i in range(n):
    sigma = sigma + (a[i] - mu) ** 2
sigma = sqrt(sigma / n)

for i in a:
    print((i - mu) / sigma)
