class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result= result+ str(len(s))+"#"+s
        return result 

    def decode(self, s: str) -> List[str]:
        i=0 
        result = [ ]
        while i < len(s):
            j=s.find("#",i)
            length = int(s[i:j])
            word = s[j+1 : length + j +1 ]
            result.append(word)
            i = j+1+length
        return result 
