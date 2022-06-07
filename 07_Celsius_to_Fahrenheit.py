Celsius = int(input("Enter the value of Celsius\n"))
def CtoF():
    return Celsius*9/5+32
Fahrenheit = CtoF()
print(Celsius,u"\N{DEGREE SIGN}","C","=",Fahrenheit,u"\N{DEGREE SIGN}","F",sep="")

