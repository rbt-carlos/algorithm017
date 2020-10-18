class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = [0 for i in range(len(nums))]
        def backTrack(tmp, nums, check):
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                backTrack(tmp + [nums[i]], nums, check)
                check[i] = 0
        backTrack([], nums, check)
        return res
