import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dic = {}

    def search(self, val):
        return val in self.dic
    
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.lst.append(val)
        self.dic[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if self.search(val):
            index = self.dic[val]
            self.lst[index] = self.lst[-1]
            self.dic[self.lst[-1]] = index
            self.lst.pop()
            del self.dic[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()