class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)          # canonical key → list of words

        for s in strs:
            count = [0] * 26                # letter frequencies, a–z
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)              # canonical form (hashable)
            groups[key].append(s)           # drop word into its bucket

        return list(groups.values())        # the grouped lists