m, k = map(int, input().split())
x = []
y = []
for i in range(k):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
# print(x,y)
# m = 10
# k = 7
# x = [1, 3, 3, 3, 6, 2, 8]
# y = [2, 3, 0, 3, 2, 1, 2]

a = [0] * (m + 1)
a[0] = 1
ans = 0
for i in range(k):
    if a[y[i]] == 0:
        ans += 1
    a[x[i]] = 1
print(ans)
