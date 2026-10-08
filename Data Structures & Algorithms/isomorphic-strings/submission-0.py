#so looking at the examples,and the constraints, I feel that if 2 strings have same number of unique characters ,then they are isomorphic......Well turns out that isn't enough, I need to make sure positions of the letters and their replacement letters are also the same, which implies , hashset won't be enough , hashmap needs to be used here
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper={}
        for i in range(len(s)):
            if s[i] not in mapper:
                mapper[s[i]]=t[i]
            else:
                if mapper[s[i]]!=t[i]:#here I want to check if a character is already present in the map , and it comes up again, then is its corresponding value at that position matches the one we got in its first ever occurence 
                    return False
        if len(mapper)==len(set(mapper.values())):
            return True
        else:
            return False
                
        
        