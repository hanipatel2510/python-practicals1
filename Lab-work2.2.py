# Lab work 2.2
# Q:-1Write a program in python to find the maximum number from the given three numbers using a nested if statement.
user1=int(input("Enter first number:"))
user2=int(input("Enter second number:"))
user3=int(input("Enter third number:"))
if user1>=user2 and user2>=user3:
    max =user1
elif user2>=user1 and user2>=user3:
    max = user2
else :
    max = user3
print(max)

# Q:-2 Write a program in python to find the manimum number from the given three numbers using a nested if statement.
user1=int(input("Enter first number:"))
user2=int(input("Enter second number:"))
user3=int(input("Enter third number:"))
if user1<=user2 and user2<=user3:
    min =user1
elif user2<=user1 and user2<=user3:
    min = user2
else :
    min = user3
print(min)

# Q:-3 Write a program in python to find the maximum number from the given four numbers using a nested if statement.
user1=int(input("Enter first number:"))
user2=int(input("Enter second number:"))
user3=int(input("Enter third number:"))
user4=int(input("Enter four number:"))
if user1>=user2 and user2>=user3 and user1>=user4:
    max =user1
elif user2>=user1 and user2>=user3 and user2>=user4:
    max = user2
elif user3>=user1 and user3>=user2 and user3>=user4:
    max = user3
else :
    max = user4
print(max,"is maximum number:")

# Q:- 4 write a program in python using a 'switch-case' equivalent to:
#Take an operator(+,-,*,/)as input.
#perfrom the corrreponding operation on two numbers entered by the user.
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
operator=input("Enter an operator (+, -, *, /): ")
match operator:
    case "+":
        result1=number1+number2
        print(result1)
    case "-":
        result2=number1-number2
        print(result2)
    case "*" :
        result3 = number1*number2
        print(result3)
    case "/":
        result4 = number1 / number2
        print(result4)

# Q:-5 Write a program in python to create a menu-driven fast-food order system using the 'match case' feature.
#for example :press 1 to order a Sandwich
# press 2 to order a Pizza
# press 3 to order a burger
#extend this program by adding a nested match case for each menu item's subtype selection by the user.
#for example: press 1 for Thin Crust pizza.
#press 2 for Cheese Brust pizza.
#prees 3  for Fresh Dough Pizza.

print("--- Welcome to that AI fast food corner.---")
print("1. order a Sandwich")
print("2. order a Pizza")
print("3. order a Burger")
choice1 = input("Enter your choice(1-3):")
match choice1:
    case "1":
        print("\n Sandwich  Manu:")
        print("1.Grilled cheese sandwich")
        print("2. veg club sandwich")
        print("3. Spicy sandwich")

        sub_choice = input("selected your sandwich type(1-3): ")
        match sub_choice:
            case "1":
                print("\nGrilled Cheese Sandwich added to your cart!")
            case "2":
                print("\nVeg Club Sandwich added to your cart!")
            case "3":
                print("\nSpicy Sandwich added to your cart!")
            case _:
                print("\nInvalid choice! Item not added.")
    case "2":
        print("\n Pizza Menu ")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")
        
        sub_choice = input("selected your pizza type(1-3): ")
        match sub_choice:
            case "1":
                print("\nThin Crust pizza added to your cart!")
            case "2":
                print("\ncheeses burst pizza added to your cart!")
            case "3":
                print("\nfresh Dough pizza added to your cart!")
            case _:
                print("\nInvalid choice! Item not added.")

    case "3":
        print("\n burger Menu")
        print("1. Classic Aloo Tikki Burger")
        print("2. Crispy Veggie Burger")
        print("3. Double Cheese Burger")

        sub_choice = input("selected your burger type(1-3): ")
        match sub_choice:
            case "1":
                print("\nClassic Aloo Tikki Burger added to your cart!")
            case "2":
                print("\nCrispy Veggie Burger added to your cart!")
            case "3":
                print("\nDouble Cheese Burger added to your cart!")
            case _:
                print("\nInvalid choice! Item not added.")
    case _:
         print("\nInvalid selection! Please choose a number between 1 and 3.")

# Q:-6 Write a program in python to create a menu-driven telecom calling system using the 'match case' feature.
#for example :press 1 for English
# press 2 for Hindi
# press 3 for Gujrati
#extend this program by adding a nested match case for each menu item's  appropriate subtype selection by the user.


print("--- Welcome to Telecom customer Care.---\n")
print("1. English Languge")
print("2. Hindi Language")
print("3. Gujarati Language")
choice1 = input("Enter your choice(1-3):")
match choice1:
    case "1":
        print("\n English Language:")
        print("Press 1 to Check Balance and Validity")
        print("Press 2 for Internet Settings and Data Plans")
        print("Press 3 to Talk to our Customer Executive")

        sub_choice = input("selected your sandwich type(1-3): ")
        match sub_choice:
            case "1":
                print("\nYour current balance is Rs. 149 and valid till next month. !")
            case "2":
                print("\nInternet settings have been sent to your mobile via SMS.!")
            case "3":
                print("\nPlease wait... Connecting your call to our executive.")
            case _:
                print("\nInvalid input! Hanging up the call.")
    case "2":
        print("\n--- Hindi Menu ---")
        print("Balance aur Validity jaanne ke liye 1 dabayein")
        print("Internet settings aur Data Plans ke liye 2 dabayein")
        print("Humare Customer Executive se baat karne ke liye 3 dabayein")
        
        sub_choice = input("Apna vikalp chunein (1-3): ")
        match sub_choice:
            case "1":
                print("\nAapka baaki balance Rs. 149 hai aur agle mahine tak valid hai.")
            case "2":
                print("\nInternet settings aapke number par SMS dwara bhej di gayi hai.")
            case "3":
                print("\nKripya prateeksha karein... Hum aapki call executive ko transfer kar rahe hain.")
            case _:
                print("\nAvaidh vikalp! Call samaapt ki ja rahi hai.")

    case "3":
        print("\n--- Gujarati Menu ---")
        print("Balance ane Validity janva mate 1 dabavo")
        print("Internet settings ane Data Plans mate 2 dabavo")
        print("Amara Customer Executive sathe vaat karva mate 3 dabavo")
        
        sub_choice = input("Tmaro vikalp pasand karo (1-3): ")
        match sub_choice:
            case "1":
                print("\nTmaru balance Rs. 149 che ane avta mahina sudhi valid che.")
            case "2":
                print("\nInternet settings tmara number par SMS dwara mokli devama aavi che.")
            case "3":
                print("\nKrupa karine raah juo... Amari team tmaro sampark kari rahi che.")
            case _:
                print("\nAnyanya vikalp! Call kat thai rahi che.")

    case _:
        print("\nInvalid Selection! Please try again.")

