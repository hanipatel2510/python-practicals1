# Lab work 2.1
#  Q:-1 Write a python program to:
#Take  a number as input from the user.
#Use an 'if-else' statement to check if the number is even or odd and print the result.
num=int(input("Enter any number:"))
if num%2 == 0:
    print("even number:")
else :
    print("odd number:") 

# Q:-2 Create a program that:
#Accepts a user's age as input.
#Uses nested 'if-else' statement to categorize the user into age groups:
#child(0-12),Teenager(13-19),Adult(20-59),senior(60+)
age=int(input("Enter your age:"))
if age<12:
    print("Child:")
else:
    if age>13 and age<19:
        print("Teenager:")
    elif age>20 and age<59:
        print("Adult:")
    else:
        print("senior:")

# Q:-3 Implement a program that:
#Takes three interger as input. 
#uses an 'if-elif-else' statement to find and print the largest  number.
user1=int(input("Enter first number:"))
user2=int(input("Enter second number:"))
user3=int(input("Enter third number:"))
if user1>=user2 and user2>=user3:
    largest=user1
elif user2>user1 and user2>user3:
    largest = user2
else :
    largest =user3
print("Largest Number is:",largest)

# Q:-4 Write a python program to:
#Take a number as input from the user and check whether it is a netural number
#or not using a ladder if statement

number1=input("Enter any value:")
if number1.isdigit() and  int(number1) > 0:
    print(number1,"natural number:")
else:
    print("is not natural number:")
