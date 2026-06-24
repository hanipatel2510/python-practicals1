#Lab Work1.3
# Q.1 Write a Python program to demonstrate the use of type casting constructors (int(), float(), str(), and bool()):
#-Take input from the user as a string.
# convert the string into an integer, a float, and a boolean.
# print the converted values along with their types.

n=input("Enter value:")
int_n = int(n)
float_n = float(n)
string_n = str(n)
bool_n = bool(n)
print(int_n, type(int_n))
print(float_n, type(float_n))
print(string_n, type(string_n))
print(bool_n, type(bool_n))

# Q.2 Write a program where the user inputs a floating-point number.
# Convert this number into an integer using int() and print both values with a message explaining the difference.

number = float(input("Enter number: "))

int_number = int(number)

print("Original Float Value =", number)
print("Integer Value =", int_number)
print("int() removes the decimal part of the number.")

# # Q.3 Create a program that:
# Takes a boolean value (True or False) as input.
# Converts the boolean to an integer and a string.

value = input("Enter True or False: ")

bool_value = value == "True"

int_value = int(bool_value)
str_value = str(bool_value)

print("Boolean Value =", bool_value)
print("Integer Value =", int_value)
print("String Value =", str_value)

# Q.4 Write a Python program to:
# Declare variables of each datatype(integer,float,string,boolean,list,tuple,dictionary)
# Print the value, type(), and memory address using id().

a = 10
b = 10.5
c = "Python"
d = True
e = ['a','b','c']
f = (1, 2, 3)
g = {"name": "Hanee","age": 22}

print( a, type(a), id(a))
print( b, type(b), id(b))
print(c, type(c), id(c))
print(d, type(d), id(d))
print(e, type(e), id(e))
print(f, type(f), id(f))
print(g, type(g), id(g))

# Q.5 Create a program that:
# Declares two variables with the same value.
# Prints their memory addresses using id() and checks if they are the same.
# Modifies one of the variable and checks the amemory ddresses again.

x = 100
y = 100

print(x,  id(x))
print(y, id(y))

y = 200
print("\nafter modication")
print(x,  id(x))
print( y, id(y))
