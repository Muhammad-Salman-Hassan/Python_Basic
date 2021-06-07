#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x=1000

def my_func():
    print(x)
my_func()

#Local Varaibel
#If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function
x='Global variable'
def z():
    x='local variable'
    print(x)
z()
#if we print out side the fuction then it will print global function
print(x)