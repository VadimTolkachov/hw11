class Iter:
    def __init__(self, lst = []):
        self.lst = lst
        self.light = 3
        if self.light == 0:
            self.light = 1
        self.iter = 0
    def __next__(self):
        result = self.lst[self.iter:self.iter+self.light]
        if self.iter < len(self.lst):
            self.iter += self.light
        
            return result
        
        else:
            raise StopIteration
    
    def __iter__(self):
        return self
        
        
    
    

a = Iter([i for i in range( 5)])

print(next(a))