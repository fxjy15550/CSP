n, m = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))


first = [0] * m
last = [n] * m
vis = [False] * m
q = [0] * m

for i in range(m):
    if p[i] == 0:
        first[i] = 1
    else:
        q[p[i] - 1] += 1
        first[i] = first[p[i] - 1] + t[p[i] - 1]

for i in range(m):
    if q[i] == 0:
        last[i] = n - t[i] + 1
        pre = p[i]
        end = last[i]
        while pre > 0:
            print(pre)
            last[pre] = min(last[pre], end - t[pre])
            pre = p[pre] - 1
            end = last[pre]


# foreach first and print each element
for i in range(m):
    print(first[i], end=" ")
# judge element in last is bigger than 0
if last == [i for i in last if i > 0]:
    print("")
    for i in last:
        print(i, end=" ")
