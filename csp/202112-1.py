n, N = map(int, input().split())
a = list(map(int, input().split()))
# n, N = (3, 10)
# a = [2, 5, 8]


def searchInsert(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] > target:
            right = m - 1
        elif nums[m] < target:
            left = m + 1
        else:
            return m
    return left


sumA = 0
idx = searchInsert(a, N)
a.insert(idx, N)
# print(idx)
for i in range(idx):
    # temp = (i + 1) * (a[i + 1] - a[i])
    sumA += (i + 1) * (a[i + 1] - a[i])
    # print(a[i], temp)
print(sumA)
