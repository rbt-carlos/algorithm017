class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backTrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backTrack(nums, [])
        return res
