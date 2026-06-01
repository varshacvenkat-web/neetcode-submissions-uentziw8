class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results={}
        for i in strs:
            key="".join(sorted(i))
            if key not in results:
                results[key]=[i]
            else:
                results[key].append(i)
        return list(results.values())
        
        



        