"""
Viết một chương trình để tạo tuple chứa các phần tử là số chẵn từ một
tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
"""
class EvenTuple:
    def __init__(self, tuple):
        self.tuple = tuple
        self.eventuple= ()
    def GenerateEven(self):
        self.eventuple = tuple(i for i in self.tuple if i %2 ==0)
        return print(self.eventuple)
if __name__ == "__main__":
    tupleInput = (1,2,3,4,5,6,7,8,9,10) 
    check = EvenTuple(tupleInput)
    check.GenerateEven()
  