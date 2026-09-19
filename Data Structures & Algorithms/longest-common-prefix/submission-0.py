class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as our reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against all other strings
            for s in strs[1:]:
                # Mismatch found OR string s is shorter than current index i
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
                    
        return strs[0]