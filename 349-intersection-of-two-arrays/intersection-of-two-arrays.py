class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common=[]
        l1=len(nums1)
        l2=len(nums2)
        if l1>l2:
            large=nums1
            small=nums2
        else:
            large=nums2
            small=nums1
        for start in small:
            for num in large:
                if start == num:
                    if start not in common:
                        common.append(start)
        return common
