class Solution:
    def isSubsequence(self, s, t):
        counter = 0
        target = head
        while target != None:
            counter += 1
            target = target.next
        if counter % 2 == 0:
            half = counter / 2
            half = int(half)
        else:
            half = int(counter / 2)
        export = head
        for item in range(0, half):
            export = export.next
        return export








answer = Solution()
print('answer:', answer.isSubsequence(s="abc", t="ahbgdc"))