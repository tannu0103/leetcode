class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr1=[0]*26
        for ch in s:
            i = ord(ch)-ord('a')
            arr1[i]+=1
        for ch in s:
            if arr1[ord(ch)-ord('a')]==1:
                return s.index(ch)
        return -1