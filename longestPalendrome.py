"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
"""

class Solution():
    def longestPalindrome(self, s):
        sMap = {}
        biggest_odd = 0
        biggest_key = None
        count = 0
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
        
        for key in sMap.keys():
            if sMap[key] > biggest_odd:
                biggest_odd = sMap[key]
                biggest_key = key
                
        count += sMap[biggest_key]
        del sMap[biggest_key]

        for value in sMap.values():
            if (value % 2) == 0:
                count += value
            else:
                count += value-1
        return count

        


        




        

answer = Solution()
#print(answer.longestPalindrome('abccccdd'))

test = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

print(answer.longestPalindrome(test))