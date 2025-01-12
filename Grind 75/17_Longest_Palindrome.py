class Solution:
    def longestPalindrome(self, s: str) -> int:
        charSet = set()
        for c in s:
            if c in charSet:
                charSet.remove(c)
            else:
                charSet.add(c)
        return len(s) if len(charSet) == 0 else len(s) - len(charSet) + 1