class Counter:
    def __init__(self, start, end):
        self.current=start
        self.end=end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<=self.end:
            current_value=self.current
            self.current+=2
            return current_value
        else:
            raise StopIteration
        
counter=Counter(1, 10)

for number in counter:
    print(number)