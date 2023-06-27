class InfiniteIterator: 
    def __init__(self, start): 
        self.start = start 
 
    def __iter__(self): 
        return self 
 
    def __next__(self): 
        self.start += 1 
        return self.start - 1
    
my_iterator = InfiniteIterator(0) 

for i in my_iterator: 
    print(i) 
    if i == 1000:
        break