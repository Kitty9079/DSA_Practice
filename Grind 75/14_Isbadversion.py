class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Search for the first bad with binary search
        res = n
        l, r = 1, res

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                res = m  # Update result to current middle
                r = m - 1  # Narrow search to the left half
            else:
                l = m + 1  # Narrow search to the right half

        return res
    

#version 2 
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l