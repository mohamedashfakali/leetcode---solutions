class Solution:
    def reverseWords(self, s: str) -> str:
        l1=s.split()
        l1.reverse()
        return " ".join(l1)