class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs=[]
        for s in strs:
            pairs.append((s, "".join(sorted(s))))
        
        groups = {}

        for key, value in pairs:
            if value not in groups:
                 groups[value] = []
            groups[value].append(key)
        result = list(groups.values())
        
        return result