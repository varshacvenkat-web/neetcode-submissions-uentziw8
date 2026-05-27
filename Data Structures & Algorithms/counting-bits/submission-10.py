class Solution:
    def countBits(self, n: int) -> List[int]:
        lists=[]
        for i in range (0,n+1):
            count=0
            while i>0:
                if (i&1)==1:
                    count+=1
                i=i>>1
            lists.append(count)
            
        return lists 