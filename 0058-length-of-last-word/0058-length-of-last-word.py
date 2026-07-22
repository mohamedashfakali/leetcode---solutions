class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        length=len(a[-1])
        return length