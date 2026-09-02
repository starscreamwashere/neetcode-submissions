#correct logic is to delete only till those characters before and including the one which is repeated
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_length=0
        max_length=0
        non_repeated=[]
        for i in range(len(s)):
            if s[i] in non_repeated:
                curr_length=len(non_repeated)
                max_length=max(curr_length,max_length)
                del non_repeated[:non_repeated.index(s[i])+1]
                non_repeated.append(s[i])
                curr_length=len(non_repeated)
            else:
                non_repeated.append(s[i])
                curr_length=len(non_repeated)
        return max(curr_length,max_length)
        