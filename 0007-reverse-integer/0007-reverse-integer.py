class Solution:
    def reverse(self, x: int) -> int:
        rever=0
        y=x
        if x<0:
            x*=(-1)
        while x!=0:
            digit=x%10
            rever=rever*10+digit
            x=x//10
        if y<0:
            rever*=(-1)
        
        if -2**31<rever<2**31-1:
            return rever
        else:
            return 0