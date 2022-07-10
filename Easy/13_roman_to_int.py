
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        num=roman_dt[s[n - 1]]
        print(num)
        for i in range(n-2,-1,-1):
            if roman_dt[s[i]]>=roman_dt[s[i+1]]:
                num+=roman_dt[s[i]]
            else:
                num-=roman_dt[s[i]]

        return num


        
