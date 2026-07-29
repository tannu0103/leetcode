from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [x // 2 for x in freq]

        middle = ""
        for i in range(26):
            if freq[i] % 2:
                middle = chr(i + ord('a'))
                break

        def count_ways():
            total = sum(half)
            ans = 1

            for x in half:
                if x:
                    ans *= comb(total, x)
                    total -= x
                    if ans >= k:
                        return k

            return ans

        if count_ways() < k:
            return ""

        left = []

        for _ in range(len(s) // 2):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_ways()

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    break

                k -= ways
                half[i] += 1

        left = ''.join(left)

        return left + middle + left[::-1]