class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        while i<j:
            y=min(heights[i],heights[j])
            area=y*(j-i)
            if heights[i]<heights[j]:
                i=i+1
            elif heights[i]>heights[j]:
                j=j-1
            else:
                i=i+1
            max_area=max(max_area,area)
        return max_area


        