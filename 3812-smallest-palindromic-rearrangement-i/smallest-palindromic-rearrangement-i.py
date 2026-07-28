class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=[0]*26
        left=""
        middle=""
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        for i in range(26):
            ch=chr(i+ord('a'))
            left+=ch*(count[i]//2)
            if count[i]%2==1:
                middle=ch
        return left+middle+left[::-1]
        