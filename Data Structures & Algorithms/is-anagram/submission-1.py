class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if lowercase
        # count number of each letter and compare
        # add counts of characters in s and subtract from t. this should be 0 if equal

        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        return (all(value == 0 for value in count.values()))
