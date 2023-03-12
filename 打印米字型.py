n = int(input())
rice = [] 
for i in range(n):
    rice_i = []
    for j in range(n):
        rice_i.append('.')
    rice.append(rice_i)
for i in range(n):
    lettter = chr(i + 65)
    rice[i][n-1] = lettter
    rice[n-1][i] = lettter
    rice[i][i] = lettter
for i in range(n):
    for j in reversed(range(n-1)):
        rice[i].append(rice[i][j])
for i in reversed(range(n-1)):
    rice.append(rice[i])


for ri in rice:
    for r in ri:
        print(r, end="")
    print("")