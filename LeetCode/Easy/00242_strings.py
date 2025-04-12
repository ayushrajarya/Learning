# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for i in s:
            if i in dict_s.keys():
                continue
            dict_s[i]=s.count(i)
        for i in t:
            if i in dict_t.keys():
                continue
            dict_t[i]=t.count(i)
        if dict_s==dict_t:
            return True
        else:
            return False

# st= Solution()
# print(st.Solution("anagram", "nagaram"))