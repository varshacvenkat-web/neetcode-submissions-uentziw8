class TimeMap:

    def __init__(self):
        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        x=(value,timestamp)
        if key in self.store:
            self.store[key].append(x)
        else:
            self.store[key]=[x]  

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        pair=self.store[key]
        left=0
        right=len(pair)-1
        result=""
        while left<=right:
            mid=((left+right))//2
            if pair[mid][1]<=timestamp: #if less than or equal to time stamp
                result=pair[mid][0] #update the results variable with pair
                left=mid+1 #update left bound to 1 above mid and search right half
            elif pair[mid][1]>timestamp: #if greater than time stamp we move right bound to less to search left half 
                right=mid-1
        return result 


        
