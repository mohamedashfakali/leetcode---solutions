class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n == 1:
            return 1

        sum_even = 0
        sum_odd = 0

        for i in range(1, n * 2):
            if i % 2 == 0:
                sum_even += i

            else:
                sum_odd += i

        num = min(sum_even, sum_odd)
        num2 = max(sum_even, sum_odd)

        while num > 0:
            x = num
            if num2 % num == 0:
                return num

            num = num2 % num
            num2 = x

        return num
        