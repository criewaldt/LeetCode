"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
"""

class Solution():
    def longestPalindrome(self, s):
        sMap = {}
        longest_odd = 0
        even_count = 0
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
        for v in sMap.values():
            if v % 2 != 0:
                if v > longest_odd:
                    longest_odd = v
            else:
                even_count += v
        return even_count + longest_odd

        

answer = Solution()
print(answer.longestPalindrome('abccccdd'))