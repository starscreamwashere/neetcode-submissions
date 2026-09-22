class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int={}
        roman_to_int['I']=1
        roman_to_int['V']=5
        roman_to_int['X']=10
        roman_to_int['L']=50
        roman_to_int['C']=100
        roman_to_int['D']=500
        roman_to_int['M']=1000
        number=0
        i=0
        while i<len(s):
            if i==len(s)-1:
                number+=roman_to_int[s[i]]
                i+=1
                break
            if roman_to_int[s[i]]>=roman_to_int[s[i+1]]:#1 digit hi uda hai tumhara
                number+=roman_to_int[s[i]]
                i+=1
            else:
                number+=roman_to_int[s[i+1]]-roman_to_int[s[i]]#2 digit udd gye tumhare at once
                i+=2
        return number


        