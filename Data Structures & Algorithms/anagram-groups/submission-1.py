class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s1 in strs:
            ss1 = "".join(sorted(s1))
            if ss1 in groups:
                groups[ss1].append(s1)
            else: 
                groups[ss1] = [s1]

        return list(groups.values())

