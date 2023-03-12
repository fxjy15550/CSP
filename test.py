# n =  int(input())
# wall = []
# for i in range(n):
#     wall.append(list(map(float, input().split())))
# print(wall)

n = 2
wall = [[4.0, 2.0, 7.0, 8.0, 9.0], [7.0, 3.0, 4.5, 6.0, 7.0]]
wall_n =[]

graph = []
for i in range(22):
    graph_i = [False] * 1001
    graph.append(graph_i)
graph[0][500] = True
graph[-1][500] = True

for i in range(n):
    x = int(wall[i][0] * 2)
    wall_n.append(x)
    for j in range(int(wall[i][1] * 100), int(wall[i][2] * 100) + 1):
        graph[x][j] = True
    for j in range(int(wall[i][3] * 100), int(wall[i][4] * 100) + 1):
        graph[x][j] = True
for i in range(1,21):
    if i not in wall_n:
        for j in range(1,1000):
            graph[i][j] = True



def distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


dp = []
for i in range(n + 1):
    dp_i = [0] * 1001
    dp.append(dp_i)

dp[0][500] = 0
for i in range(n):
    for j in range(1001):
        dp[i][j] = min(distance(0,j,0.5,))
