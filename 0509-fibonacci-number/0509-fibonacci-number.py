class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1

        for _ in range(1, n + 1):
            t=a+b
            a=b
            b=t

        return a