# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""
        smallest= min(strs, key=len)
        prefix=""
        for i, letter in enumerate(smallest):
            for word in strs:
                if word[i]!= letter:
                    return prefix
            prefix+=letter
        return prefix

# st=Solution()
# print(st.longestCommonPrefix(["flower","flow","flight"]))