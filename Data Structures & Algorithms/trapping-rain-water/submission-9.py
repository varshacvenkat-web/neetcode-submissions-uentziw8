class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        area2=0
        maxright=[]
        water=[]
        maxleft=[]
        for i in range((len(height))-1,-1,-1):
            area=(max(area,height[i+1]) if i+1<len(height) else 0)
            maxright.append(area)
        maxright=maxright[::-1]
        for i in range(len(height)):
            area2=(max(area2,height[i-1]) if i-1>=0 else 0)
            maxleft.append(area2)

        for i in range(len(height)):
            water.append(min(maxleft[i],maxright[i])-height[i])
            if water[i]<0:
                water[i]=0
    
        x=sum(water)
        
        return x

        
    

        