class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = defaultdict(list)
        for s in strs :
            sors = ''.join(sorted(s))
            ref[sors].append(s)
        return list(ref.values())