class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group first with same word lengths
        # then, use dictionary to add/sub and see what gives 0 OR sort letters for unique key
        anagram_map = {}
        for word in strs:
            keysort = "".join(sorted(word))
            anagram_map.setdefault(keysort, []).append(word)

        return list(anagram_map.values())