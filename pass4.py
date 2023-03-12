T = int(input())

for i in range(T):
    n = int(input())
    step = []
    for j in range(n):
        step_str = input()
        if len(step_str) > 7:
            # print("step :",step_str, step_str[-1])
            step.append(step[int(step_str.split()[-1]) - 1])
        elif step_str.startswith("L"):
            step.append(-1)
        else:
            step.append(1)
    print(sum(step))
