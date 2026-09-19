class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char=strs[0][i] #extract ith index from 0th variable in strs
            for j in strs:
                if i>=len(j) or char != j[i]:
                    return strs[0][:i]
        return strs[0]
        