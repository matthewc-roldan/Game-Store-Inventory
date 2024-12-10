# Matthew Chaparro-Roldan
# Program 10
# COP 2500
# November 21, 2024


# This creates the main function that will call all the others and creates an empty dictionary
def main():
    inventory = {}
    true = 0

    # This function says that when menu is called it will display the menu options.
    def menu():
        print("1. Increase Inventory\n")
        print("2. Decrease Inventory\n")
        print("3. View Inventory\n")
        print("4. Quit")
        

    # When increase_inventory is called it will ask what game and how many are being bought and adds
    # it to the dictionary with its key and value
    def increase_inventory():
           gb = input("What game are you purchasing?\n")  
           gc = int(input("How many are you purchasing?\n"))

           # If game is found in the dictionary it will add to its value, else it will add it to dictionary
           if gb in inventory:
               inventory[gb] += gc
           else:
               inventory[gb] = gc
            
               


    # Asks user what game is being sold
    def decrease_inventory():
           game_sold = input("What game are you selling?\n")
           # If game is not in inventory it will print error message and prompt user to select from menu again
           if game_sold not in inventory:
               print("You do not have any copies of", game_sold, "in stock")
               return
           elif game_sold in inventory:
               sold_count = int(input("How many are you selling?\n"))
            # If the amount being sold is greater than the amount in stock it will give error message
           if inventory[game_sold] < sold_count:
               print("You do not have "+str(sold_count),"copies of "+str(game_sold), "in stock. You sold "+str(inventory[game_sold]),"of them")
               inventory.pop(game_sold)
               return
        # If amount sold is less than it will subract it from the current value
           else:
               inventory[game_sold] -= sold_count
               print("Updated Inventory:"+str(inventory))
                
    # creates a list for the low stock items and the high stock items and prints out the entire dictionary
    # If criteria is right the value is added to the list and then it uses a if statement to print all items in list if any.
    def view_inventory():
        low_stock = []  
        high_stock = []
        for key in inventory:
            print(key,"\t",inventory[key])

            if inventory[key] < 100:
               low_stock.append(key)
            elif inventory[key] > 1000:
                high_stock.append(key)

        if len(low_stock) > 0:
            print("\nLow Stock Warning(s):")
            for key in low_stock:
                print(key)
        if len(high_stock) > 0:
            print("\nSale Recommendations:")
            for key in high_stock:
                print(key)


    # Uses a boolean to loop the menu and then uses if statements to call the proper function.
    # If 4 is selected then it will kill the loop
    while true == 0:
        menu()
        menu_selection = int(input("Choose a menu option (1-4)\n"))
        if menu_selection == 1:
            increase_inventory()
        elif menu_selection == 2:
            decrease_inventory()
        elif menu_selection == 3:
            view_inventory()
        elif menu_selection == 4:
            true = 1


    
           

    


            
        




main()

