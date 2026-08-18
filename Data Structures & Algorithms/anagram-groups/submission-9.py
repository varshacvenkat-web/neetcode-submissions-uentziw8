class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results={}
        for i in strs: 
            key="".join(sorted(i)) #key so we sort i into inidvidual strings and join for eahc i
            if key in results:
                results[key].append(i) #then we append original i to a list 
            else:
                results[key]=[i] #if not, we make a new list 
        return list(results.values())

        



        