print("Welcome to Pi Pizza Online Delivery!")
print("Pepperoni add-ons cost: 2$ for small pizza & 3$ for large pizza.")
print("Extra Cheese add-ons cost: 1$")
size = input("What is the size of your Pizza? We have: S, M, L: ")
add_pepperoni = input("Do you want pepperoni?: Y or N: ")
extra_cheese = input("Do you want extra cheese?: Y or N: ")

bill = 0
pep_for_small = 2
pep_for_large = 3

#reference variable
isSmall = 15
isMedium = 20
isLarge = 25
isCheese = 1

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2  
    if extra_cheese == "Y":
        bill += 1
    
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 2  
    if extra_cheese == "Y":
        bill += 1
        
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 2  
    if extra_cheese == "Y":
        bill += 1    
        
print(f"Your total bill is: ${bill}.")