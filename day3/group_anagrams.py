class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        smap = {}
        result = []
        
        for i in range(len(strs)):
            word = strs[i]
            a = "".join(sorted(word))
            
            if a not in smap:
                smap[a] = [word]
            else:
                smap[a].append(word)
        
        for value in smap.values():
            result.append(value)
        
        return result