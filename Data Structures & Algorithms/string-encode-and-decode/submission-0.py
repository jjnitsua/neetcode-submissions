class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            l=str(len(s))
            res=res+l+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while len(s)!=0:
            j=i
            while s[j]!='#' :
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+length+1]
            s=s[j+1+length:]
            res.append(word)
        return res
