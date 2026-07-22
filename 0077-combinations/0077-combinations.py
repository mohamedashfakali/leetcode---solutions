class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr_list = []
        num_list = [0]*n
        for i in range(n):
            num_list[i]=i+1
        print(num_list)

        def dfs(index:int)->None:
            # base case
            
            if len(curr_list) == k:
                print("curr_list",curr_list)
                ans.append(curr_list.copy())
                return
            
            # better pruning checking if their is even possible to form a subset of size k with the remaining element
            if len(curr_list) + (n - index) < k:
                return
            
            if index >= n:
                return 
            # take

            curr_list.append(num_list[index])
            dfs(index+1)
            # pop 
            curr_list.pop()
            # not take
            dfs(index+1)

        dfs(0)
        return ans