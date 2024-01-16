class RandomizedSet:

    def __init__(self):
        self.values = []
        self.HashMap = dict()

    def insert(self, val: int) -> bool:
        if val not in self.HashMap:
            self.HashMap[val] = len(self.values)
            self.values.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.HashMap:
            index = self.HashMap[val]
            lastElement = self.values[-1]
            self.values[-1] = val
            self.values[index] = lastElement
            self.values.pop()
            self.HashMap[lastElement] = index
            del self.HashMap[val]
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()