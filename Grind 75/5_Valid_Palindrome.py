class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.lower()
        while i < len(s):
            if not s[i].isalnum():
                s = s.replace(s[i],"")
            else:
                i += 1
        if s[:] == s[::-1]:
            return True
        return False

# most optimal 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(filter(str.isalnum, s.lower()))
        return s[::-1]==s