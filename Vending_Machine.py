# Display food in vending machine
food = { ## Encase dictionary in a list to call it later
    1: {
        "name": "Coca - cola",
        "price": 1.50,
        "stock": 5,
    },
    2: {
        "name": "Sprite",
        "price": 1.50,
        "stock": 0,
    },
    3: {
        "name": "Fanta",
        "price": 1.50,
        "stock": 5,
    },
    4: {
        "name": "Lays",
        "price": 3.00,
        "stock": 0,
    },
    5: {
        "name": "Cheetos",
        "price": 3.00,
        "stock": 5,
    },
    6: {
        "name": "Doritos",
        "price": 3.00,
        "stock": 5,
    }
} 

# Call List
for key, item in food.items():
    print(f"{key} {item['name']} : {item['price']}")

# User chooses item
print("Please choose your item.")
print("Enter '0' when done.") ## Quit value

cart = []
totalprice = 0 ## States an initial amount in a set variable

while True:
    choice = input("Please enter the number of your chosen item: ") ## User will enter the item they want here
    
    if choice == "0": ## When user ends the transaction
        display_cart = {item: cart.count(item) for item in set(cart)} 
        ## .count counts the items in the initial cart. 
        ##Set makes the list into a set allowing no duplicates.
        print("The items you wish to purchase are:")
        for item, quantity in display_cart.items():
            print(f"{item}: {quantity}") 
        
        print(f"Total Price: {totalprice:.2f}") 
        ## ":.2f" specifies that the numbers will always be displayed with 2 decimal places.
        ## ":." specifies where it starts, and "2" specifies that there will be 2 decimal places. 
        ## "f" means fixed point notation, which means that whatever we specified are fixed. 

        # Payment process
        while True: ## Ensures it won't accept inputs other than numbers
            cash= input(f"Please enter the amount in cash: ")
            try:
                cash = float(cash)
                break  # Exit the loop if input is valid
            except ValueError:
                print("INVALID INPUT. Please enter a valid amount.")

        # If cash is less than required
        if cash < totalprice:
            cashneeded = totalprice - cash
            print(f"Insufficient funds. You still owe {cashneeded:.2f} dhs.")
            while True:
                addcash= input("Please add more cash: ")
                try:
                    addcash = float(addcash)
                    cash += addcash
                    break  
                except ValueError:
                    print("INVALID INPUT. Please enter a valid number.")

        # If cash is sufficient
        change = cash - totalprice
        print(f"Thank you for buying! Your change is {change:.2f} dhs.")
        break

    # Make sure input is a digit. Performs the program if the input is a digit.
    elif choice.isdigit(): 
        choice = int(choice)  

        ## Availability check
        ## Food stock process
        if choice in food: 
            if food[choice]['stock'] == 0:  # Removes user input if food isn't in stock anymore.
                print(f"\n{food[choice]['name']} is OUT OF STOCK")
            else:  # Add to cart items in stock
                cart.append(food[choice]['name'])
                totalprice += food[choice]['price']
                food[choice]['stock'] -= 1 ## Subtracts the item by 1
                print(f"\nYou have ordered {food[choice]['name']}.")
                print(f"{food[choice]['name']} : {food[choice]['stock']} left")
        else:
            # Output when input is a number not in the list
            print("INVALID ITEM NUMBER.")
    else:
        print("INVALID INPUT. Please enter a number.")