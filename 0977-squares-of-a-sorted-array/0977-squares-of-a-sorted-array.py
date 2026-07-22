class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            square=i**2
            arr.append(square)
        return sorted(arr)