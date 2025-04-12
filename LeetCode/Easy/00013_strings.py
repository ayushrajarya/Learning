# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        va={"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        l=[]
        for i in s:
            l.append(va[i]) # converted all to integers
        if len(s)==1:
            return va[s] # if only one roman then directly return
        num=sum(l) # sum of all the integers
        for j in range(len(s)):
            if j+1< len(s) and l[j]<l[j+1]:
                num-=2*l[j] # subtracting twice as sum contained it earlier and since it was to be deducted in first place so twice
        return num

# a=Solution()
# print(a.romanToInt("MCMXCIV"))
