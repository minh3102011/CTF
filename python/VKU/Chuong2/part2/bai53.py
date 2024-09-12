from itertools import *
class Subsets:
    def __init__(self, lst):
        self.lst = lst

    def all_subsets(self):
        subsets = []
        for i in range(len(self.lst) + 1):
            for combo in combinations(self.lst, i):
                subsets.append(list(combo))
        return subsets

if __name__ == "__main__":
    lst = [1, 2, 3]
    subsets = Subsets(lst)
    print(subsets.all_subsets())