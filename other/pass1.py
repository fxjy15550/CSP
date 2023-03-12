n = int(input())

a = []
for i in range(n):
    a_i = [0] * 3
    a.append(a_i)

a[0][0] = 10
for i in range(1, n):
    a[i][0] = a[i - 1][0] * 9 + a[i - 1][1] * 9
    a[i][1] = a[i - 1][0]
    a[i][2] = a[i - 1][1] + a[i - 1][2] * 10
print(a[n - 1][2])
