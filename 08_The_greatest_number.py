a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))
def func1(a,b,c):
    if a<b:
        greatest = b
    else:
        greatest = a
    if greatest<c:
        greatest = c
    return greatest
d = func1(a,b,c)
print(d,"is the greatest of all the numbers entered")