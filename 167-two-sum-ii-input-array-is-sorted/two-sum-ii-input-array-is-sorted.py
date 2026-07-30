class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rem = target-nums[i]
            temp =nums[i+1:]
            if rem in temp:
                return [i+1,temp.index(rem)+i+2]
            