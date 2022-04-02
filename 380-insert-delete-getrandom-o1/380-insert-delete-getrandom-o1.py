import random
class RandomizedSet:

    def __init__(self):
        self.data_dict = {}
        self.index_dict = {}
        self.max_index = 0 #elements map from 1 onwards

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False
        
        self.max_index += 1
        self.data_dict[val] = self.max_index
        self.index_dict[self.max_index] = val
        return True
                

    def remove(self, val: int) -> bool:
        if not self.max_index:
            return None
        
        if val not in self.data_dict:
            return False
        curr_val = val
        curr_index = self.data_dict[val]
        end_index = self.max_index
        end_val = self.index_dict[end_index]
        
        #Swap in index_dict to maintain uniform list of index
        self.index_dict[curr_index], self.index_dict[end_index] = self.index_dict[end_index], self.index_dict[curr_index]
        
        #Swap in data_dict to maintain uniform list of index
        self.data_dict[val], self.data_dict[end_val] = self.data_dict[end_val], self.data_dict[val]
 
        self.index_dict.pop(end_index)
        self.data_dict.pop(val)
        self.max_index -= 1
        return True

    def getRandom(self) -> int:
        rand_index = random.randint(1, self.max_index)
        return self.index_dict[rand_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()