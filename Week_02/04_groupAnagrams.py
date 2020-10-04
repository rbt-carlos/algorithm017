class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for a in strs:
            key = tuple(sorted(a))
            dict[key] = dict.get(key, []) + [a]
        return list(dict.values())[::-1]
