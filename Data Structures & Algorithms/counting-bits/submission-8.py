class Solution:
    def countBits(self, n: int) -> List[int]:
        lists=[]
        for i in range (0,n+1):
            count=0
            tmp=i
            while tmp>0:
                if (tmp&1)==1:
                    count+=1
                tmp=tmp>>1
            lists.append(count)
            
        return lists 