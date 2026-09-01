class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+'#'+strs[i]
        return ''.join(strs)
            

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = s.find('#',i)
            ln = int(s[i:j])
            l.append(s[j+1 : j+1+ln])
            i = j+1+ln
        return l
                
                
                
        
        
                

            
        
        