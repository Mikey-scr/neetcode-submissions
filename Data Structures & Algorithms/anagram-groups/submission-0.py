class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
 
        groups = {} 
 
        for word in strs: 
            frequency = [0] * 26 
 
            for i in range(len(word)): 
                frequency[ord(word[i]) - ord("a")] += 1 
 
            key = tuple(frequency) 
 
            if key not in groups: 
                groups[key] = [] 
 
            groups[key].append(word) 
 
        return list(groups.values())