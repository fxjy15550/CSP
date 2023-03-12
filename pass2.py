t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    stack = []
    for j in range(n):
        m = tuple(map(int, input().split()))
        # print(m)
        if len(stack) == 0:
            if m[1] == 0:
                ans += 1
            else:
                stack.append(m)
        else:
            if m[1] == stack[-1][1]:
                stack.append(m)
            else:
                tmp_len = len(stack)
                for k in range(tmp_len):
                    if stack[-1][0] < m[0]:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                        ans += 1
    print(ans + len(stack))
