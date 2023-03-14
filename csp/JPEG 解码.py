from math import pi
from math import cos
from math import sqrt

# 8*8 zigzag reverse
def zigzag_reverse(b):
    n = int(len(b) ** 0.5)  # 矩阵的大小（假设b是平方数）
    a = [[0] * n for _ in range(n)]  # 存放结果的矩阵
    k = 0  # b的索引
    i = 0  # 行索引
    j = 0  # 列索引

    while i < n and j < n:
        a[i][j] = b[k]
        k += 1
        if (i + j) % 2 == 0:
            if i > 0 and j != n - 1:
                i -= 1
                j += 1
            elif j == n - 1:
                i += 1
            else:
                j += 1
        elif (i + j) % 2 == 1:
            if j > 0 and i != n - 1:
                i += 1
                j -= 1
            elif i == n - 1:
                j += 1
            else:
                i += 1
    return a


Q = []
for i in range(8):
    Q.append(list(map(int, input().split())))

n = int(input())
t = int(input())
check = list(map(int, input().split()))
while len(check) < 64:
    check.append(0)

T = []
T.append(zigzag_reverse(check))
# matrix * matrix
T.append(list(map(lambda x, y: list(map(lambda a, b: a * b, x, y)), T[0], Q)))

def clamp(x, min_val, max_val):
    return max(min(x, max_val), min_val)

# 离散余弦逆变换
def idct_2d(a):
    n = len(a)
    b = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0.0
            for u in range(n):
                for v in range(n):
                    alpha_u = sqrt(1.0 / 2) if u == 0 else 1
                    alpha_v = sqrt(1.0 / 2) if v == 0 else 1
                    sum += (
                        alpha_u
                        * alpha_v
                        * a[u][v]
                        * cos((2 * i + 1) * u * pi / (2 * n))
                        * cos((2 * j + 1) * v * pi / (2 * n))
                    )
            b[i][j] = sum / 4
    return [[clamp(round(x + 128),0,255) for x in y] for y in b]

# print(len(T[1]))
T.append(idct_2d(T[1]))

# print list
for row in T[t]:
    print(" ".join(map(str, row)))