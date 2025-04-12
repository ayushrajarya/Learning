# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=len(s)
        left=0
        right=l-1
        while left <=l-1 and right>=0:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower()!=s[right].lower():
                        return False
                    right-=1
                    left+=1
                else:
                    right-=1
            else:
                left+=1
        return True

# st=Solution()
# print(st.isPalindrome("A man, a plan, a canal: Panama"))