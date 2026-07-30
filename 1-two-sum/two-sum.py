class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in map1:
                return [map1[rem],i]
            else:
                map1[nums[i]]=i