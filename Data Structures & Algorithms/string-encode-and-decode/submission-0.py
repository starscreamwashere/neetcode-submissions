class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for string in strs:
            s+=str(len(string))+"#"+string
        return s

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i < len(s):
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            start_of_word=j+1
            end_of_word=j+1+length
            word=s[start_of_word:end_of_word]
            decoded.append(word)
            i=j+1+length
        return decoded
            