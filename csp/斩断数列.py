# n, k = map(int, input().split())
# a = list(map(int, input().split()))


n = 4
k = 7
a = [17, 5, 21, 15]

for i in range(1, n):
    if a[i] < 0:
        a[i] = -a[i]
        a[i] = a[i] % k

""" 
    dp[i] = dp[i-1] 
"""


def dfs(index, prefix, k, a):
    if index == len(a):
        if prefix % k == 0:
            return True
        else:
            return False
    return dfs(index + 1, prefix + a[index], k, a) or dfs(
        index + 1, prefix - a[index], k, a
    )


if dfs(0, 0, k, a):
    print("Divisible")
else:
    print("Not divisible")
