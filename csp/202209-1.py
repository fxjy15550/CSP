# m_n = input()
# a_n = input()
# n = int(m_n.split()[0])
# m = int(m_n.split()[1])
# a_list = a_n.split()
# a_list = list(map(int, a_list))

# n = 7
# m = 23333
# a_list = [3, 5, 20, 10, 4, 3, 10]
# n = 15
# m = 32767
# a_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
n = 4
m = 0
a_list = [2, 3, 2, 5]

c_list = [1]
for i in range(n):
    c_list.append(c_list[-1] * a_list[i])
mc_list = []
b_list = []
for i in range(n):
    mc_list.append(m % c_list[i + 1])

for i in range(n - 1, 0, -1):
    mc_list[i] = mc_list[i] - mc_list[i - 1]
for i in range(n):
    if mc_list != 0:
        tmp = int(mc_list[i] / c_list[i])
    b_list.append(tmp)
for i in b_list:
    print(i, end=" ")
