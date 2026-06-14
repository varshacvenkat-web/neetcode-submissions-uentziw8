class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(len(heights)):
            while stack and heights[i]<stack[-1][1]: #stack is a tupule with (length,height) so we are extracting the height
                index,height=stack.pop()
                if stack:
                    leftboundary=stack[-1][0] #index of the top element
                else:
                    leftboundary=-1
                width=i-leftboundary-1 #why -1 here
                area=height*width
                max_area=max(max_area,area)
            stack.append((i, heights[i]))
            
        while stack:
            index,height=stack.pop()
            if stack:
                leftboundary=stack[-1][0]
            else:
                leftboundary=-1
            width=len(heights)-leftboundary-1
            area=height*width
            max_area=max(max_area,area)
        return max_area
