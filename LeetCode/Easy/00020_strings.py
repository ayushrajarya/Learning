# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        para_open=["(", "{", "["]
        para_close={"(": ")", "{": "}", "[": "]", " ":" "}
        track=" "
        for i in s:
            if i in para_open:
                track+=i
            elif para_close[track[-1]]!=i:
                return False
            else:
                track=track[:-1]
        return track==" "

# st= Solution()
# print(st.isValid("([])"))