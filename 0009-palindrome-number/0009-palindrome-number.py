class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp=x
        rever=0
        while x>0:
            digit=x%10
            rever=rever*10+digit
            x=x//10
        return temp==rever
        