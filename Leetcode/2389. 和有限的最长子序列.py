from typing import List
from bisect import bisect_right
from itertools import accumulate


class Solution:
    # Brute force
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        for q in queries:
            cnt = 0
            for i, num in enumerate(sorted_nums):
                cnt += num
                if cnt > q:
                    ans.append(i)
                    break
                if i == len(sorted_nums) - 1:
                    ans.append(i + 1)
        return ans

    # Binary search
    def answerQueries_bs(self, nums: List[int], queries: List[int]) -> List[int]:
        # f[i] = sum(nums[:i]) prefix sum
        f = list(accumulate(sorted(nums)))
        return [bisect_right(f, q) for q in queries]


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(s.answerQueries_bs(nums, queries))
