class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        holder = {} #key letter, value index
        longest, lower, upper = 0, 0, 0

        for i in range(len(s)):
            if s[i] in holder and holder[s[i]] >= lower:
                lower = holder[s[i]] + 1
            holder[s[i]] = i
            longest = max(longest, i + 1 - lower)

        return longest
