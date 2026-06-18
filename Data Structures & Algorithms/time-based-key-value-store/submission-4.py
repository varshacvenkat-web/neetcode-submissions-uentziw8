class TimeMap:

    def __init__(self):
        self.store={} #make dictionary
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        x=(value,timestamp) #we make a tupule for value and time stamp
        if key in self.store:
            self.store[key].append(x) #we append that tupule for the key
        else:
            self.store[key]=[x]   #or if key doesn't exist make new key

    def get(self, key: str, timestamp: int) -> str: # we want to return the value that is less than or equal to timestamp in get 
        if key not in self.store: #if the key is not in dict. return ""
            return ""
        pair=self.store[key] #we extract all the tupule from the key 
        left=0 #set left bound index
        right=len(pair)-1 #set right bound index
        result="" #results varaibale that we update 
        while left<=right: #while the left bound is less than or equal to the right bound, ensures there is still valid indexes to check
            mid=((left+right))//2 #mid index
            if pair[mid][1]<=timestamp: #if less than or equal to time stamp (what we want)
                result=pair[mid][0] #update the results variable with pair
                left=mid+1 #update left bound to 1 above mid and search right half
            elif pair[mid][1]>timestamp: #if greater than time stamp we move right bound to less to search left half 
                right=mid-1 #check left half
        return result 


        
