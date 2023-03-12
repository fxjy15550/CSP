# n, x = map(int,input().split())
# a_list = []
# for i in range(n):
#     a_list.append(input())
# a_list = list(map(int, a_list))

# n = 4
# x = 100
# a_list = [20, 90, 60, 60]
n = 3
x = 30
a_list = [15, 40, 30]

# a_list = sorted(a_list, reverse=True)
# price = []
# for i in range(1, n + 1):
#     tmp = 0
#     for j in range(i):
#         tmp += a_list[j]
#     if tmp > x:
#         flag = i

price = sum(a_list)
dp = [0] * (n * x)
for i in range(n):
    for j in range(price, a_list[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - a_list[i]] + a_list[i])
for i in range(x, price + 1):
    if dp[i] >= x:
        print(dp[i])
        break
