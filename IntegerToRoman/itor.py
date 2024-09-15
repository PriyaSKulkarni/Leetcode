class Solution:
    def intToRoman(self, num: int) -> str:
        listroman = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]

        res=""
        for r,val in reversed(listroman):
            if num // val:
                count= num//val
                res += (count*r)
                num = num%val
        
        return res
