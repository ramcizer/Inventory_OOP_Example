#I imported tabulate as indicated in the course but didn't use for choice of format. 
from tabulate import tabulate

# ========The beginning of the class==========
# As per the instructions the class attributes are set and then referenced
#I used "sale" rather than "cost" because it made more sense when marking sales promotions. 
class Shoe:

    def __init__(self, country, code, product, price, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.price = price
        self.quantity = quantity
        self.special_promotion = False

        pass

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    #This is the promote function for the class. 
    #This also makes use of the get_price method defined at line 19. 
    #Works duing user option 4. 
    def promote(self): 
        self.special_promotion = True
        self.price = round(self.price - (self.price / 100 * 10), 2)
        print("The item has been marked as 10% off\n")
        print(f"The new price is: \t\t\t\t\t\t\t{self.get_price()}")
    
    # This is the string output as requested by the task.
    # I've added some expandtabs formating to assure that is in line.
    def __str__(self):
        output = f"Product: {self.product} \t\t".expandtabs(30)
        output += f" {self.code}\t"
        output += f"Qty: {self.quantity}"
        output += f""
        
        return output   


#=============Shoe list===========

# The list will be used to store a list of objects of shoes.

shoe_list = []
#==========Functions outside the class==============

# This funciton reads from the inventory.txt and then appends shoe_list with shoe objects. 
# The defensive programming has been added as per instructions. 
# The defensive programming is to avoind a FileNotFoundError. 
def read_shoes_data():
    
    pass

    try:
        with open('inventory.txt', 'r') as inventory_list: 

            inventory_list = inventory_list.readlines() 

            # It also skips the first line so it doesn't read inventory.txt headings. 
            # The append function is included here: 
            for i, x in enumerate(inventory_list):
                if x != inventory_list[0]: 
                    shoe_details = x.split(",")
                    shoe_list.append(Shoe(shoe_details[0], shoe_details[1], shoe_details[2], int(shoe_details[3]), int(shoe_details[4])))
    
            
            # print(shoe_list)

    except FileNotFoundError: 
        print("There isn't a file with an inventory to start with, please add to project folder")

    return shoe_list

    
def capture_shoes():
    pass

    while True: 

        country_of_origin = str(input("\nPlease enter where the shoe is made: "))
        product_code = str(input("Please enter the product code: "))
        product_name = str(input("Please enter the product's name: "))
        

        if len(country_of_origin) < 1 or len(product_code) <1 or len(product_name) < 1:
            print("\nAt least one of your choices didn't register, please try again ")
        else: 
            break
    while True: 

        try: 
            product_quantity = int(input("Please enter the quanity of the product to add to stock: ")) 
            product_price = int(input("Please enter the product's price: "))
            break
        except ValueError: 
            print("Please enter a number")  

    shoe_list.append(Shoe(country_of_origin, product_code, product_name, product_price, product_quantity))

    return shoe_list
    
#The view all function for loops the newly created list of Shoes to present the information to the user. 
def view_all():
    pass   

    shoes = shoe_list    
    
    print("\nThe current stock items are: \n")

    for i, obj in enumerate(shoes, 1): 
        output = f"{i}. {obj.product} \t\t ".expandtabs(30)
        output += f" {obj.code}"
        output += f""
        total_shoes = i
        if i > 0:
            print(output)
        else: 
            print("There aren't any shoes to view.")

    print(f"\nThat's a total of {total_shoes} types of shoe in stock.\n")

    return   

# This section is in aid of efficiency as two further functions, search_show() and restock uses.
def shoe_choiced(shoes, shoe_choice): 

    for i, obj in enumerate(shoes):
            if shoe_choice not in obj.code:
                code_search_result = "\nThat code is unrecognised\n"
            if shoe_choice == obj.code:
                print("\nThe product of the code you entered is: \n")
                code_search_result = obj
                # print(f"\n{obj}")
                break
            elif shoe_choice == "Menu":
                code_search_result = "\nYou chose to exit without searching."
                break        

    print(code_search_result)

    return code_search_result

# As per the task, the lowest amount of stock can be viewed with the option of replenishing the stock. 
# Again there's some defensive programming added to avoid crashing upon no entry by the user. 
def re_stock():
    pass

    shoes = shoe_list

    print("\nThe shoes that are nearly depleted stock are: ")

    # Note the list objects are sorted and then looped. 
    shoes.sort(key = lambda x : x.quantity)
    for i, obj in enumerate(shoes):        
        if obj.quantity < 10:
            print(obj)

    while True:
        # The defensive programming here is to avoid an error if no entry by the user. 
        try: 

            shoe_choice = input('''\nPlease enter the code of the shoe that you want to replenish for
                                    or type Menu to return to the main menu.
                                    :  ''')
            #There is efficiency here. 
            shoe_choiced(shoes, shoe_choice)

            
            if shoe_choice != "Menu":                

                for i, obj in enumerate(shoes): 
                    if shoe_choice == obj.code:
                        stock_shoe = shoes[i]
                        replenish_qty = int(input("\nPlease enter the number of shoes you would like to replenish by: "))
                        stock_shoe.quantity = stock_shoe.quantity + replenish_qty
                        print(f"\nThe new stock details are:\n {stock_shoe}")
            else:
                break
        except UnboundLocalError:
            print("\nPlease enter a valid choice\n")        

        
    pass        
    
   
# As per the instructions, this receives a product code as an input before matching the shoes. 
# It then prints the choice of shoes if the product code is part of the stock list. 
# I've added some defensive programming to avoid an error when return is pressed without an entry
def search_shoe():
    pass
     
    shoes = shoe_list

    # The user entry is requested until a code is recognised, the user can also choose to exit. 
    while True:

        try:
            shoe_choice = input('''\nPlease enter the code of the shoe you are searching for
                                    or type Menu to return to the main menu.
                                    :  ''')

            shoe_choiced(shoes, shoe_choice)
            break

        except UnboundLocalError:
            print("Please enter a valid choice")        

    pass

#This function returns the total value of the all stock. 
def value_per_item():
    pass
    
    shoes = shoe_list

    # An adapted for loop with its own output includes the calculation at line 224.
    for i, obj in enumerate(shoes, 1): 
        output = f"{i}. {obj.product} \t\t".expandtabs(30)
        output += f" Qty: {obj.quantity}\t"
        output += f"Total Value: {obj.quantity * obj.price}"
        output += f""
        total_shoes = i
        if i > 0:
            print(output)
        else: 
            print("There aren't any shoes to view.")

# As per the task, the user gets the option to view the most stocked item in order to put on offer.
# The options presented for special offer are items of which there are more than 10 in stock. 
def highest_qty():
    pass    

    shoes = shoe_list

    # A sort function enables a different reading of the list of stock by the following for loop. 
    shoes.sort(key = lambda x : x.quantity, reverse = True)

    for i, obj in enumerate(shoes):
        if obj.quantity > 10 and obj.special_promotion == False:        
            output = f"Product: {obj.product}\t\t".expandtabs(30)
            output += f"{obj.code}\t"
            output += f"{obj.quantity}"
            print(output)

    while True:

        try: 

            shoe_choice = input('''\nPlease enter the code of the shoe that you want to mark as being on special offer
                                    or type Menu to return to the main menu.
                                    :  ''')

            #Note, as noted above, this function is added for the sake of efficiency. 
            shoe_choiced(shoes, shoe_choice)

            if shoe_choice != "Menu":

                for i, obj in enumerate(shoes):
                    if shoe_choice == obj.code and obj.special_promotion == True:
                            print("\nThe shoe is already on promotion\n")
                    if shoe_choice == obj.code and obj.special_promotion == False:
                        stock_shoe = shoes[i]                    
                        stock_shoe.promote()
                        
                        
            else: 
                break
        except UnboundLocalError:
            print("Please enter a valid choice")   
                    

# I added another function, more than the task requires, to show all current promoted items. 
# It makes use of a function within the class Shoe to reduce the price by 10%
def special_offer_stock():

    shoes = shoe_list

    count = 0

    for i, obj in enumerate(shoes):
        if obj.special_promotion == True:
            count += 1
            promoted_shoe = obj
            print(obj)           
            
        

    print(f"\nThat's a total of special offer items of: {count}")  
    # print(f"\n{promoted_shoe} \nNew Price: \t\t\t{promoted_shoe.get_price()} ")


#==========Main Menu=============

# The read shoes function is required to start otherwise there is not stock to view
# As above, the read_shoes_data function reads the txt file and converts the data for purpose. 
# In a version of this program where different files are used for the process it could be a user option. 
# This covers task requirement "read_shoes_data", 
# "capture_shoes" works at user option 7, 
# "view_all" works at user option 1,
# "re_stock" works at user ption 3. 
# "search_shoe" works at user option 2. 
# "value_per_item" works at user option 5, 
# "highest_qty" works at user option 4, 
# and I've added an extra opton 6. 
# note, and a reminder I've used "price" instead of "cost" for attributes so that I could add promotion function. 

read_shoes_data()

#This is the main menu which covers: 
while True:

    try: 

        user_choice = int(input('''\nPlease choose from the following options
        
                                (1) View all the shoes in stock
                                (2) Find a shoe by its code
                                (3) Replenish a depleted stock item
                                (4) Put a high quanity stock item on promotion
                                (5) View the total value per stock item
                                (6) View all special promotion shoes
                                (7) Add a newly produced show to the stock list
                                (8) Exit
                                
                                : '''))

        if user_choice == 1:
            view_all()
        if user_choice == 2:
            search_shoe()
        if user_choice == 3:
            re_stock()
        if user_choice == 4:
            highest_qty()
        if user_choice == 5: 
            value_per_item()
        if user_choice == 6: 
            special_offer_stock()
        if user_choice == 7: 
            capture_shoes()
        if user_choice == 8:
            exit()
        elif user_choice > 8 or user_choice <1: 
            print("Please enter a valid choice")
    except ValueError:
        print("That wasn't a number")
          
        
