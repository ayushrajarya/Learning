# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min_len=min(len(a), len(b))
        c= a if len(a) >= len(b) else b
        carry=0
        ans=""
        for i in range(min_len):
            curr=int(a[-(i+1)])+int(b[-(i+1)])+carry
            if curr==0 or curr==2:
                ans="0"+ans
                if curr==2:
                    carry=1
            elif curr==3:
                ans="1"+ans
                carry=1
            else:
                carry=0
                ans="1"+ans
        for i in range(len(c)-min_len):
            curr= int(c[-(i+min_len+1)])+carry
            if curr==0 or curr==2:
                ans="0"+ans
                if curr==2:
                    carry=1
            else:
                carry=0
                ans="1"+ans
        if carry==1:
            return "1"+ans
        return ans

# st= Solution()
# print(st.addBinary("1011", "10101"))