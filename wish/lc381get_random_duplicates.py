from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.indices = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        is_new = False
        if val not in self.indices:
            is_new = True
        self.elements.append(val)
        self.indices[val].add(len(self.elements) - 1)
        return is_new

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.indices: return False
        out_indx, insert_num = self.indices[val].pop(), self.elements[-1]
        self.elements[out_indx] = insert_num
        self.indices[insert_num].add(out_indx)
        self.indices[insert_num].discard(len(self.elements) - 1)
        self.elements.pop()
        if len(self.indices[val]) == 0: del self.indices[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        """
        ind = random.randint(0, len(self.elements) - 1)
        return self.elements[ind]

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.insert(1)
param_3 = obj.insert(2)
param_4 = obj.insert(2)
param_5 = obj.insert(2)
param_6 = obj.remove(1)
param_7 = obj.remove(1)
param_8 = obj.remove(2)
param_9 = obj.insert(1)
param_0 = obj.remove(2)
param_01 = obj.getRandom()
print(param_01)