class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_length=0
        max_length=0
        empty_string=[]
        for i in range(len(s)):
            if s[i] in empty_string:
                curr_length=len(empty_string)
                max_length=max(curr_length,max_length)
                empty_string=[]
                empty_string.append(s[i])
                curr_length=len(empty_string)
            else:
                empty_string.append(s[i])
                curr_length+=1
        return max(curr_length,max_length)

        