n, m, L = map(int, input().split())
A = []
for i in range(n):
    a_line = list(map(int, input().split()))
    A.append(a_line)

# n, m, L = (4, 4, 16)
# A = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

h = [0] * L

for i in range(n):
    for j in range(m):
        h[A[i][j]] += 1
for i in h:
    print(i,end=" ")
