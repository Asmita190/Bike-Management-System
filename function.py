#importing date and time
import datetime

#the given below function displays the welcome message to the user
def welcome():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++           Welcome to the program             ++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

#the given function displays the bikes from the text file to the user
def display_bike():
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Bike ID \t Bike-Name \t\t Company Name \t\t\t\t\t\t Colour \t\t Quantity \t Price \t|")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    try:
        #open text file in read mode
        file = open("bike.txt","r")
        a = 1
        for line in file:
            print(a,"\t\t"+line.replace(",","\t\t"))
            a= a+1
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        file.close()
        #close file
    #check for exception
    except IOError:
        print("\nFile name misplaced!")

#the given function adds the bikes from the text file to the 2D list
def add_bike_2D_list():
    #open text file in read mode
    read_file = open("bike.txt","r")
    my_list = []
    for i in read_file:
        i = i.replace("\n","")
        my_list.append(i.split(","))
        #store bike details in 2D list
    return my_list


#the given below function displays options for the users in the system
def user_operation():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Enter 1 to purchase the bike:                         ++++")
    print("Enter 2 to add stock:                                 ++++")
    print("Enter 3 to exit:                                      ++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    
#the given below function displays bike added to stock  when user press 2
def add_bike_stock():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The bike has been added to the stock. Following are the details of the company:")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

#the given below function validate the bike ID
def validating_bike_id():
    loop = True
    #loop runs
    while loop == True:
        try:
            print("\n")
            global valid_id
            #declare global to access it from other functions
            valid_id = int(input("Enter the ID of the bike you want: "))
            print("\n")
            #check if input is greater than 0 and less than the bike listed
            while valid_id<=0 or valid_id>len(add_bike_2D_list()):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid Bike ID !!!")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                display_bike()
                #display bike after invalid input
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                valid_id = int(input("Enter the ID of the bike you want: "))  #ask to input again after invalid input
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
            return valid_id #return the id entered
            loop = False
            #loop terminates
        except ValueError:  #check for value error to catch exception
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Please enter integer value from the table!!!!")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            
            
#the given below function displays bike purchased from stock  when user press 1           
def purchase_bike():
    print("\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Congratulations!! The bike has been purchased. The details of the buyers are below:")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    
    
#the given below function displays invalid user input when the user gives invalid input 
def invalid_user_input():
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Invalid input!!!")
    print("Please provide value as 1, 2 or 3.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    
#the given below function displays system exit when the user press 3
def exit_system():
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Thank you for using our system")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
#the given below function updates bike stock in text file
def update_stock(bike_list):
    #open text file in write mode
    file = open("bike.txt","w")
    for i in bike_list:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+"\n")
        #update bike stock after purchasing bike
    file.close()
    #file closed
    
    display_bike()
    #print bike details

#the given below function updates bike stock in text file by adding quantity
def add_stock(bike_list):
    #open text file in write mode
    file = open("bike.txt","w")
    for i in bike_list:
        file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+"\n")
        #update bike stock after adding bike
    file.close()
    #file closed

    display_bike()
    #print bike details
    
#the given below function updates bike quantity from user 
def final_add(user_input_bike_id, the_quantity):
    bike_list = add_bike_2D_list()
    bike_list[user_input_bike_id - 1][3] = int(bike_list[user_input_bike_id - 1][3]) + the_quantity
    add_stock(bike_list)

#the given below function validates quantity input
def quantity_validation(the_bike_id):
    loop = True
    #loop runs
    while loop == True:
        #using of try except for Value Error
        try:
            bike_list = add_bike_2D_list()
            user_quantity = int(input("Enter the quantity you want to purchase: "))
            print("\n")
            while user_quantity <=0 or user_quantity>int(bike_list[the_bike_id - 1][3]):
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid Quantity ID !!!")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                user_quantity = int(input("Enter the quantity you want to purchase: "))
                print("\n")
            return user_quantity
            loop = False
        except ValueError:
            print("\n+++++++++++++++++++++++++++++++++++++")
            print("Only Integer Values Please!!!!")
            print("+++++++++++++++++++++++++++++++++++++\n")

#the given below function updates bike quantity after sell to user
def final_sell(user_input_bike_id, the_quantity):
    bike_list = add_bike_2D_list()
    bike_list[user_input_bike_id - 1][3] = int(bike_list[user_input_bike_id - 1][3]) - the_quantity
    update_stock(bike_list)
    
#the given below function calculates total price
def total_price(user_input_bike_id, the_quantity):
    bike_list = add_bike_2D_list()
    total_price = int(bike_list[user_input_bike_id-1][4].replace("$",""))*the_quantity
    return total_price


#the given below function validates quantity input
def quantity_val(the_bike_id):
    loop = True
    while loop == True:
        try:
            global bike_list, id
            #declaring global so it can be accessed
            
            bike_list = add_bike_2D_list()
            id = the_bike_id
            user_quantity = int(input("Enter the quantity you want to add: "))
            print("\n")
            #checking if quantity input is greater than 0
            while user_quantity <=0:
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid Quantity ID !!!")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                user_quantity = int(input("Enter the quantity you want to add: "))
                print("\n")
            return user_quantity
            loop = False
            #loop breaks
            
        except ValueError:
            print("\n+++++++++++++++++++++++++++++++++++++")
            print("Please Integer Value Only!!!!")
            print("+++++++++++++++++++++++++++++++++++++\n")

  

#the given below function returns selected bike color to user
def color(user_input_bike_id):
    bike_list = add_bike_2D_list()
    bcolor = (bike_list[user_input_bike_id-1][2])
    print("Bike Color: ", bcolor)
    return bcolor

#the given below function returns selected bike name to user
def nameb(user_input_bike_id):
    bike_list = add_bike_2D_list()
    bname = (bike_list[user_input_bike_id-1][0])
    print("Bike Name: ", bname)
    return bname

#the given below function returns selected bike company name to user
def cname(user_input_bike_id):
    bike_list = add_bike_2D_list()
    cname = (bike_list[user_input_bike_id-1][1])
    print("Bike's Company Name: ", cname)
    return cname

#the given below function returns selected bike price to user
def price(user_input_bike_id):
    bike_list = add_bike_2D_list()
    bprice = (bike_list[user_input_bike_id-1][4].replace("$",""))
    print("Price of a single bike: ", bprice)
    return bprice

#the given below function checks if valid price is given 
def validPrice(text):
    price = input(text)
    try:
        price = int(price.replace('$',''))
        #check input in integer and catch exception
    except:
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('Price can only contain numbers and $ (dollar) sign. Please try again!')
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        price = validPrice(text).replace('$','')
    return '$'+str(price)

#the given below function checks integer and string
def number(text):
    in_num = input(text)
    try:
        in_num = int(in_num)
        #check input in integer and catch exception
    except:
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('Phone number only contain numbers. Please try again!')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        in_num = number(text)
    return str(in_num)

#the given below function checks name is in string
def check_name(text):
    in_name = input(text)
    st1 = in_name.replace(" ","").isalpha()
    try:
        if not st1:
            raise ValueError
            #raises valueerror if it contains any integer
    except ValueError:
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('Name only contains alphabets. Please try again!')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        in_name = check_name(text)
    return str(in_name)

#the given below function takes user details input
def user():
    global name, num, email, location, curr_date
    name = check_name("Enter your name: ") #call check name function from above
    num = number("Enter your phone number: ") #call check number function from above
    email = str(input("Enter your email address: "))
    location = str(input("Enter your current location: "))
    
    date = datetime.datetime.now()
    curr_date = date.strftime("%m/%d/%Y, %H:%M:%S")
    print("\n-------------------------------------------------------------------------------------------")
    print("Hello " + name + "! Welcome to our Bike Store.\nPlease select product as per your choice.")
    print("-------------------------------------------------------------------------------------------\n")
    display_bike()

#the given below function prints user details
def puser():
    print("Full Name: ", name)
    print("Phone Number: ", num)
    print("Email-address: ", email)
    print("Current Location: ",location)
    nameb(the_bike_id)
    cname(the_bike_id)
    color(the_bike_id)
    print("Quantity of Bike: ", the_q)
    price(the_bike_id)
    print("Total cost of the bike: ", the_price)
    print("Date: ", curr_date)


#the given below function asks if user wants to purchase more
def user_ask():
    run = True
    #loop runs till False not returned
    while run == True:
        print("\n")
        ask = input("Do you want to purchase another bike? Y/N ")

        #if input is yes
        if ask.upper() == "Y":
            display_bike() #display bike details
            the_bike_id = validating_bike_id() #validate bike id
            the_q = quantity_validation(the_bike_id) #validate bike quantity
            final_sell(the_bike_id, the_q) #finalize the sell
            the_price = total_price(the_bike_id, the_q) #calculate price
            bike.update({the_bike_id:the_q}) #update bike list of user
            bill(the_bike_id, bike, name, num, email, location, curr_date) #append bill after purchase again
            purchase_bike() #purchase message display
            puser() #display user details

        #if input is no
        elif ask.upper() == "N":
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Thank you!! Your selected bikes were purchased successfully.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            run = False
            #loop terminates
            
         #input except yes and no
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++")
            print("\n Invalid Input!!! Please enter Y or N ")
            print("+++++++++++++++++++++++++++++++++++++++++++")

#the given below function takes company details input  
def com_user():
    global comp_name, comp_number, comp_email, comp_location, current_date, ship, shipCost
    #ask for input
    comp_name = check_name("Enter your company name: ") #call check name function from above
    comp_number = number("Enter company phone number: ") #call check number function from above
    comp_email = input("Enter company email address: ")
    comp_location = input("Enter the company current location: ")
    date = datetime.datetime.now()
    current_date = date.strftime("%m/%d/%Y, %H:%M:%S")
    ship = input("\nEnter the name of the Shipping Company: ")
    shipCost = validPrice("\nEnter the shipping Cost: ") #call check valid price function from above
    print("\n------------------------------------------------------------------------------------------------")
    print("Hello " + comp_name + "! Welcome to our Bike Store.\nPlease select product as per your choice.")
    print("------------------------------------------------------------------------------------------------\n")
    display_bike()
    
#the given below function prints company details
def comp_user():
    print("Company Name: ", comp_name)
    print("Company's Phone Number: ", comp_number)
    print("Company's Email-address: ", comp_email)
    print(" Company's Current Location: ", comp_location)
    nameb(the_bike_id)
    cname(the_bike_id)
    color(the_bike_id)
    print("Quantity of Bike: ",the_q)
    price(the_bike_id)
    print("Total cost of the bike: ", the_price)
    print("Name of Shipping Company: ", ship)
    print("Shipping Cost: ", shipCost)
    print("Date: ", current_date)

#the given below function asks if user wants to add more   
def comp_ask():
    run = True
    while run == True:
        print("\n")
        ask = input("Do you want to add another bike? Y/N ")
        #if input is yes
        if ask.upper() == "Y":
            display_bike() #displaying bike
            the_bike_id = validating_bike_id() #validate bike id
            the_q = quantity_val(the_bike_id) #validate quantity
            final_add(the_bike_id, the_q) #finalize add
            the_price = total_price(the_bike_id, the_q) #calculate total price
            bikeDetails = [the_q,ship,shipCost.replace('$','')] #store user details
            bike.update({the_bike_id:bikeDetails}) #update user details
            invoice(the_bike_id,bike, comp_name, comp_number, comp_email, comp_location, current_date, ship, shipCost) #append bill
            add_bike_stock() 
            comp_user() #print details

        #if input is no
        elif ask.upper() == "N":
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(" Thank you!! Your selected bikes were added successfully.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            run = False
            #loop terminates

         #input except yes and no   
        else:
            print("\n++++++++++++++++++++++++++++++++++++++++")
            print("Invalid Input!!! Please enter Y or N ")
            print("++++++++++++++++++++++++++++++++++++++++\n")


        

#the given below function runs when user press 1 for purchase
def purchaseBike():
    global the_bike_id, bike, the_q, the_price
    print("\n\n----------------------")
    print("|  Purchase  Bikes   |")
    print("----------------------\n")
    the_bike_id = 0
    the_q = 0
    bike = {}
    buyMore = True
    while buyMore:
        user()
        the_bike_id = validating_bike_id() #validating bike id
        print("\n")
        the_q = quantity_validation(the_bike_id) #validating quantity
        bike.update({the_bike_id:the_q}) #updating user input

        final_sell(the_bike_id, the_q) #finalizing sell
        the_price = total_price(the_bike_id, the_q) #total price calculate
        purchase_bike() #purchase bike display
        bill(the_bike_id, bike, name, num, email, location, curr_date) #generating bill

        puser() #user details
        user_ask() #asking if user wants to add more
        print("\n")
        user_operation() #asking user to operate
        buyMore = False
        #loop terminates
        

#the given below function runs when user press 2 for add           
def addStock():
    global the_bike_id, bike, the_q, the_price
    print("\n\n------------------")
    print("|   Add  Stock   |")
    print("------------------\n")
    the_bike_id = 0
    the_q = 0
    bike = {}
    bikeDetails = []
    addMore = True
    #loop runs
    while addMore:
        com_user()
        the_bike_id = validating_bike_id() #validating bike id
        the_q = quantity_val(the_bike_id) #validating quantity
        final_add(the_bike_id, the_q) #finalizing add
        the_price = total_price(the_bike_id, the_q) #total price calculate
        bikeDetails = [the_q,ship,shipCost.replace('$','')] #updating required parameters on list
        add_bike_stock() #adding bike to stock
        bike.update({the_bike_id:bikeDetails}) #updating user input
        invoice(the_bike_id,bike, comp_name, comp_number, comp_email, comp_location, current_date, ship, shipCost) #generating bill
        comp_user() #user details
        comp_ask() #asking if user wants to add more
        print("\n")
        user_operation() #asking user to operate
        addMore = False
        #loop terminates

        
#the given below function generates bill when user purchases bike
def bill(the_bike_id,bike, name, num, email, location, curr_date):
    global bike_id, b_curr
    #declaring global to access it from other function
    results = add_bike_2D_list()
    bike_id = the_bike_id
    b_name = name
    b_num = num
    b_email = email
    b_location = location
    b_curr = curr_date
    bbike = bike
            #function to extract current date and time
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time
    grandTotal = 0
    with open("invoice-"+""+name+""+""+num+".txt", 'w') as f:
    #function to write in the text file
        f.write("                    Bike Management System                   \n")
        f.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        f.write("\n\nInvoice: " + invoice + "\t\tDate: " + d +"\n" +'\n\t\t\t\tTime: ' + e + "")
        f.write('\n'+"\nName of Customer: " + str(b_name) +"" + "\n")
        f.write("Phone Number: " + str(b_num)+"" + "\n")
        f.write("Email-address: " + str(b_email) +"" + "\n")
        f.write("Current Location: " + str(b_location) +"" + "\n" + '\n\nBikes Purchased:\n---------------------------------------------------------\n')
    for i in bbike:
        with open("invoice-"+""+name+""+""+num+".txt", 'a') as f:
        #function to append the text file
            f.write('Bike Name: ' + results[i-1][0] + '\nCompany Name: ' + results[i-1][1] + '\nBike Color: ' + results[i-1][2] + '\nQuantity: ' + str(bbike[i]) + '\nPrice of Single Bike: ' + results[i-1][4] + '\nTotal Amount: $' + str(int(results[i-1][4].replace('$',''))*bike[i]) + '\n---------------------------------------------------------\n')

        grandTotal = grandTotal + int(results[i-1][4].replace('$',''))*bbike[i]
         #function to calculate grand total
        
    with open("invoice-"+""+name+""+""+num+".txt", 'a') as f:
    #function to append the text file with grand total
        f.write('\nGrand Total: $' + str(grandTotal))


        
#the given below function generates bill when user adds bike
def invoice(the_bike_id,bike, comp_name, comp_number, comp_email, comp_location, current_date, ship, shipCost):
    global bike_id, dd
    results = add_bike_2D_list()
    bike_id = the_bike_id
    nam = comp_name
    numb = comp_number
    em = comp_email
    loc = comp_location
    dd = current_date
    sship = ship
    sshipCost = shipCost
    bbike = bike
    
            #function to extract current date and time
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time
    grandTotal = 0
    with open("invoice-"+""+comp_name+""+""+comp_number+".txt", 'w') as f:
    #function to write in the text file

        f.write("                  Bike Management System                    \n")
        f.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        f.write("\n\nInvoice: " + invoice + "\t\tDate: " + d +"\n" +'\n\t\t\t\tTime: ' + e + "")
        f.write('\n'+"\nName of Customer: " + str(nam) +"" + "\n")
        f.write("Phone Number: " + str(numb)+"" + "\n")
        f.write("Email-address: " + str(em) +"" + "\n")
        f.write("Current Location: " + str(loc) +"" + "\n" + '\n\nBikes Added:\n---------------------------------------------------------\n')

    for i in bbike:
        with open("invoice-"+""+comp_name+""+""+comp_number+".txt", 'a') as f:
        #function to append the text file
            
            f.write('Bike Name: ' + results[i-1][0] + '\nCompany Name: ' + results[i-1][1] + '\nBike Color: ' + results[i-1][2] + '\nQuantity: ' + str(bbike[i][0]) + '\nPrice of Single Bike: ' + results[i-1][4] + '\nTotal Amount: $' + str(int(results[i-1][4].replace('$',''))*bike[i][0]) + '\nShipping Company: ' + bbike[i][1] + '\nShipping Cost: $' + bbike[i][2] +'\n---------------------------------------------------------\n')

        grandTotal = grandTotal + int(results[i-1][4].replace('$',''))*bbike[i][0] + int(bbike[i][2])
        #function to calculate grand total

    with open("invoice-"+""+comp_name+""+""+comp_number+".txt", 'a')  as f:
    #function to append the text file with grand total
        f.write('\nGrand Total: $' + str(grandTotal))

                                                         














        
            

