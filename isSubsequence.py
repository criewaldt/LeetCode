class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        counter = 0
        for item in range(len(t)):
            if counter <= (len(s)-1):
                if s[counter] == t[item]:
                    counter += 1
        return counter == len(s)








answer = Solution()
print('answer:', answer.isSubsequence(s="abc", t="ahbgdc"))