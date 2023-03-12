n = int(input())
seq = []
for i in range(n):
    seq.append(input())
# n = 4
# seq = ["aZ", "tZ", "Xt", "aX "]


def dfs(i):
    for j in range(65, 123):
        if graph[i][j] > 0: # 未访问
            graph[i][j] -= 1
            graph[j][i] -= 1
            dfs(j)
    path.append(i)


graph = []  # ord(alpha) 保证字典序
degree = {}
path = []
for i in range(123):
    g = [0] * 123
    graph.append(g)
for s in seq:
    for i in range(2):
        graph[ord(s[i])][ord(s[1 - i])] += 1
        degree[ord(s[i])] = degree.get(ord(s[i]), 0) + 1
# print(graph)
# print(min(degree.keys()))
start = 0
cnt = 0
for k in sorted(degree.keys()):
    if degree[k] % 2 != 0:
        if start == 0:
            start = k
        cnt += 1
if cnt > 2:
    print("No Solution")
    exit()
if start == 0:
    start = min(degree.keys())
dfs(start)
if len(path) != n + 1:
    print("No Solution")
    exit()
for i in path[::-1]:
    print(chr(i),end="")
