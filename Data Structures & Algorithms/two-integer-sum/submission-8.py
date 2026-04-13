class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for x,y in enumerate(nums):
            if target-y not in hashmap:
                hashmap[y]=x
            else:
                return [hashmap[target-y],x]

            

        