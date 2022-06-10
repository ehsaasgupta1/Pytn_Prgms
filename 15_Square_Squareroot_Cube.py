import math
num = int(input("Enter the number\n"))
class Calculator:
    def __init__(self,num):
        self.num = num
                
    def printObj(self):
        print(f"The square of {self.num} is {self.num*self.num}")
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")
        print(f"The squareroot of {self.num} is {math.sqrt(self.num)} ")

solution = Calculator(num)
solution.printObj()


