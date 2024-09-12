class Cal_Square:
    def __init__(self) :
        self.list = []
    def Cal_square(self):
        for i in range(0, 21):
            self.list.append(i**2)
        return self.list
if __name__=="__main__":
    square= Cal_Square()
    list = square.Cal_square()
    list_first = list[1:len(list)//2+1]
 
    list_sec  = list[len(list)//2+1:len(list)]
  
    print(list_first)