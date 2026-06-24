#Lab work 2.3
# Q:-1 write a program using a while loop to:
#Take numbers as input from the user until they enter '0'.
num=-1
while num !=0:
    num=int(input("enter any number(0-stop):"))
    if num !=0:
        print("you entered: ",num)
print("terminated:")

# Q:-2 Create a program using 'for' loop to:
#Iterater over a given range(1 to 10).
#print each digit's square ,one per line.
number1=[x**2 for x in range(1,11)]
print(*number1,sep="\n")

# Q:-3 Write a program to:
#Use a 'while' loop to print all even numbers between 1 and 50.
i=0
while i<=50:
    if i%2 ==0:
        print("even num",i)
    i+=1

# Q:-4 Write a program to:
#Use the `range()` function to generate a sequence of numbers from 1 to 20.
#Print only the odd numbers using a `for` loop.
number2=[x**2 for x in range(1,20)]
for i in number2:           
    if i%2 !=0:
        print(i)

# Q:-5 Implement a program that:
#Uses the `range()` function with three arguments (start, stop, step) to print multiples of 5 from 5 to 50.
for i in range(5,51,+1):
    if i%5 ==0:
        print(i,end=" ")

# Q:-6 Create a program using a `for` loop and `range()` to:
#Print a reverse countdown from 10 to 1.
for i in range(10,0,-1):
    print(i,end=" ")

# Q:-6 Write a program that:
#Uses a `for` loop and `range()` to iterate through numbers from 1 to 50.
#Checks if each number is divisible by 2, 3, or both using nested `if-elif-else`.
#Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both").
for i in range(1,50):
    if i%2==0 and i%3==0:
            print("Both (2,3)",i)
    elif i%2==0:
           print("Divide By 2:",i)
    elif i%3==0:
        print("Divide by 3:",i)
    



