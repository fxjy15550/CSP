n, i = input().split()
n = int(n)
i = float(i)
money = list(map(int, input().split()))

for j in range(n):
    money[j + 1] = money[j + 1] * (1 + i) ** -(j + 1)

print(sum(money))
