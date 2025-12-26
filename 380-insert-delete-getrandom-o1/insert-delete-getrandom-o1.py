class RandomizedSet:

    def __init__(self):
        self.array = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        index = self.pos[val]
        lastIndex = self.array[-1]

        self.array[index] = lastIndex
        self.pos[lastIndex] = index

        self.array.pop()        
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()