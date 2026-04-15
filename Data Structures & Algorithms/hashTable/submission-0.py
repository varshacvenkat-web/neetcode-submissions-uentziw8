class Pair:
    def __init__(self,key,value):
        self.key=key
        self.value=value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size=0
        self.capacity=capacity
        self.map=[None]*capacity
    
    def hash(self, key):
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        index=self.hash(key)#we make index from key with hash function
        while True:
            if self.map[index]==None: #None so we add 
                self.map[index]=Pair(key,value)
                self.size+=1
                if self.size>=self.capacity//2:
                    self.resize()
                return
            elif self.map[index].key==key: #if index is occupied with same key
                self.map[index].value=value 
                return
        
            else:
            #if index is occupied just check the next slot and rehash? 
                index+=1
                index=index % self.capacity




    def get(self, key: int) -> int:
        index=self.hash(key)
        while self.map[index]!=None:
            if self.map[index].key==key:
                return self.map[index].value 
            else:
                index +=1
                index=index%self.capacity
        return -1 


    def remove(self, key: int) -> bool:
        index=self.hash(key)
        while self.map[index]!=None:
            if self.map[index].key==key:
                self.map[index]=None 
                self.size-=1
                return True 
            else:
                index +=1
                index=index%self.capacity
        return False 


    def getSize(self) -> int:
        return self.size 



    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity=self.capacity*2 
        newmap=[]
        for i in range(self.capacity):
            newmap.append(None)
        oldmap=self.map
        self.map=newmap 
        self.size=0
        for pair in oldmap:
            if pair:
                self.insert(pair.key,pair.value) 


