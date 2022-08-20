if __name__ == "__main__":
    print("Hello, World!")

# boilerplate code that protects users from accidentally invoking the script when they didn't intend to


def even_num(num):

    if num % 2 == 0:

        return str(num) + ' is an even number'
    else:
        return str(num) + ' is not an even number'

if __name__ == "__main__":

    print(even_num(2))


# to make the case known better
# take a step back to understand how Python initializes scripts and how this interacts with its module import mechanism

print("before import")
import math

print("before first_function")
def first_function():
    print("Second Function")

print("before second_function")
def second_function():
    print("First Function {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    first_function()
    second_function()
print("after __name__ guard")

# It's as if the interpreter inserts this at the top of your module when run as the main program.
# __name__ = "__main__"

# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
# math = __import__("math")

# and the rest of the code is exec/continued simultaneously

"""testing out the efficiency"""

def func():
    print("func() in first.py")

print("top-level, first.py")

if __name__ == "__main__":
    print("first.py is being run directly")
else:
    print("first.py is being imported into another module")


# first you have created a first.py module
# if you import the code block in this case first.py, and run another program second.py with the import still on
# it will print 'first.py is being imported into another module
# picture the load as an entry point to the program which will run if the '__main__' matches the '__name__'