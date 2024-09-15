class Solution:
    def isValid(self, s: str) -> bool:
        parren ={ '(':')','{':'}','[':']',']':'','}':'',')':''}
        stack =[]
        j=-1
        for i in range(0,len(s)):
            stack.append(s[i])
            j+=1
            if s[i] == parren[stack[j-1]] and len(stack)>1:
                stack.pop()
                stack.pop()
                j-=2
        if len(stack) ==0:
            return True
        else:
            return False
            

        
