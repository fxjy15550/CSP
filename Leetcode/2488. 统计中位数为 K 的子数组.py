from collections import Counter
from typing import List


class Solution:
    def sign(self, num: int) -> int:
        return (num > 0) - (num < 0)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        kIndex = nums.index(k)
        ans = 0
        counts = Counter()
        counts[0] = 1
        sum = 0
        for i, num in enumerate(nums):
            sum += self.sign(num - k)
            if i < kIndex:
                counts[sum] += 1
            else:
                prev0 = counts[sum]
                prev1 = counts[sum - 1]
                ans += prev0 + prev1
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [2, 5, 1, 4, 3, 6]
    k = 1
    print(s.countSubarrays(nums, k))
