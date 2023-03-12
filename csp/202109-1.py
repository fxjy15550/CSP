n = int(input())
b = list(map(int, input().split()))

# n = 6
# b = [0, 0, 5, 5, 10, 10]

b_set = set(b)
print(sum(b))
if len(b_set)==n:
    print(sum(b))
    exit()

sum_a = b[0]
for i in range(1,n):
    if(b[i]>b[i-1]):
        sum_a+=b[i]
print(sum_a)


