class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        total_ones = 0
        prev_zero_group = float("-inf")
        max_gain = 0

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                total_ones += length
            else:
                max_gain = max(max_gain, prev_zero_group + length)
                prev_zero_group = length

            i = j

        return total_ones + max_gain