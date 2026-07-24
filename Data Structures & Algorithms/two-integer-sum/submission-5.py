class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        res = []
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                res.append(prevMap[diff])
                res.append(i)
            prevMap[n] = i
        return res
                
