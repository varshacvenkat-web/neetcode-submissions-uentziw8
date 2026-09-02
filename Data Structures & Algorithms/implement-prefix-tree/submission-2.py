class TrieNode: #creates node, each node contains a dictionary
    def __init__(self):
        self.children={}
        self.endofword=False 


class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        current=self.root
        for i in word:
            if i in current.children:
                current=current.children[i]
            else:
                current.children[i]=TrieNode()
                current=current.children[i]
        current.endofword=True 



    def search(self, word: str) -> bool:
        current=self.root
        for i in word:
            if i in current.children:
                current=current.children[i]
            else:
                return False 
        if current.endofword==True:
            return True
        else:
            return False 
    
        

    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for i in prefix:
            if i in current.children:
                current=current.children[i]
            else:
                return False
        return True 
            
        
        