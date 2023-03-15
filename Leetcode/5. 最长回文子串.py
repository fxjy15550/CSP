class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create a 2D array to store the results
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # Iterate through the string
        max_len = 0
        for i in range(n):
            for j in range(i + 1):
                # Check if the substring is a palindrome
                if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        start = j
        return s[start:start + max_len]
    

    # Manacher algorithm
    def longestPalindrome(self, s: str) -> str:
        # Insert special characters to handle even length cases
        s = "#" + "#".join(s) + "#"
        n = len(s)
        # Create an array to store the palindrome radius
        p = [0] * n
        # Initialize the center and right boundary of the current palindrome
        c = 0
        r = 0
        # Iterate through the string
        for i in range(n):
            # Find the mirror index of i with respect to c
            j = 2 * c - i
            # If i is within the right boundary, use the minimum of p[j] and r - i
            if i < r:
                p[i] = min(p[j], r - i)
            # Expand the palindrome around i as much as possible
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and s[i - p[i] - 1] == s[i + p[i] + 1]:
                p[i] += 1
            # Update the center and right boundary if needed
            if i + p[i] > r:
                c = i
                r = i + p[i]
        # Find the maximum palindrome radius and its index
        max_len = max(p)
        max_idx = p.index(max_len)
        # Return the original substring without special characters
        return s[max_idx - max_len : max_idx + max_len + 1].replace("#", "")