# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            if s[-(i+1)]==" " and count!=0 :
                break
            elif s[-(i+1)]!=" ":
                count+=1
        return count

# st= Solution()
# print(st.lengthOfLastWord("Hello World"))