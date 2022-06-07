n = int(input("Enter the value for n\n"))
def sum():
    if(n<0 or n==0):
        return "The value of n should be be a natural number" 
    return  n*(n+1) / 2
a = sum()
print(int(a))