class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""
        for i in range(len(strs[0])):
            for words in strs:
                if i==len(words) or words[i]!= strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
        
        