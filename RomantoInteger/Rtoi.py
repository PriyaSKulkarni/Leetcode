class Solution:
    def romanToInt(self, s: str) -> int:
        listroman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        res = 0

        for i in range(0,len(s)-1):
            if listroman[s[i]] >= listroman[s[i+1]]:
                res += listroman[s[i]]
                print(res)
            else:
                res -= listroman[s[i]]
                print(res)
    
        res += listroman[s[len(s)-1]]
        return res
             
            
        
