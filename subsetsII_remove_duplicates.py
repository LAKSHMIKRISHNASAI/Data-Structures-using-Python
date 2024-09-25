class Solution:
    def check_nums(self,visited,ans):
        for subset in visited:
            if subset==ans:
                return True 
        return False
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # if in approach it goes to last index then answer will get.
        # if once condition reached, then backtrack to previous position and go through another solution. similarly backtrack and goes through all possible cases.
        # [1,2,3]--[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
    #                            [1,2,3]
    # 1                  [1]                   []
    # 2            [1,2]       [1]         [2]      []
    # 3        [1,2,3] [1,2] [1,3] [1] [2,3] [2]   [3] []

   

                  #          [1,2,2]
        #             [1]               []
        #    [1,2]          [1]       [2]      []
        # [1,2,2] [1,2] [1,2] [1] [2,2] [2]  [2]  []---[2] obtaining twice need to remove it.
         
        res=[]
        sol=[]
        visited=[]
        n=len(nums)
        nums.sort()
        def backtrack(i):
        
            if i==n:
                if self.check_nums(visited,sol[:])==False:
                    res.append(sol[:])
                    visited.append(sol[:])
                return 
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            backtrack(i+1)
        backtrack(0)
        return res
