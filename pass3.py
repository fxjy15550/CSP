n = int(input())
parent = list(map(int, input().split()))
s = input()

graph = {0: []}
for i in range(1, n):
    graph[i] = []
    if s[i] != s[parent[i]]:
        graph[i].append(parent[i])
        graph[parent[i]].append(i)

stack = []
seen = set()


def dfs(now_node, father):
    global ans
    dis = 0
    d1, d2 = 0, 0  
    tmp = 0 

    for i in graph[now_node]:
        seen.add(i)
        if i == father:
            continue
        tmp = dfs(i, now_node) + 1  
        dis = max(dis, tmp)
        if tmp > d1:
            d2 = d1
            d1 = tmp
        elif tmp > d2:
            d2 = tmp 

    ans = max(ans, d1 + d2) 
    return dis


ret = 0
for i in range(n):
    if i in seen:
        continue
    ans = 0
    dfs(i, -1)
    if ret < ans:
        ret = ans
print(ret + 1)
