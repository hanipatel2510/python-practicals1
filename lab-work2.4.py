# Q:-1 Write a Python program that:
#Uses a for loop to print numbers from 1 to 20.
#Skip numbers divisible by 4 using the continue statement.
for i in range(1,21):
    if i%4==0:
        continue
    print(i)

# Q:-2 Implement a program using a while loop to:
#Print numbers from 1 to 10.
#Stop the loop using the break statement when the number is 7.
i=1
while i<=10:
    if i==7:
        break
    print(i)
    i+=1

# Q:-3Create a program that:
#Iterates over a string (e.g., "PYTHON").
#Uses a continue statement to skip vowels and print only consonants
a="PYTHON"
vowels=('A','E','I','O','U')
for i in a:
    if i in vowels:
       continue
    print(i,end="")

# Q:-4 Write a Python program to print multiplication tables using nested loops for up to N numbers in this format:
# 1 x 1 = 1
# 1 x 2 = 2
# …
#Where N is the user-given number.
number=int(input("enter a number:"))
for i in range(1,number+1):
    for j in range(1,11):
        result= i*j
        print(i,"x" ,j,"=",result)
    print()


# Q:-5 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Q:-6 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

for i in range(5,-1,-1):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()

# Q:-7 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end=" ")
    print()

# Q:-8 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
    
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()

