#importing function file
import function

function.welcome()
#calling to print welcome message from function file

function.display_bike()
#calling to display bike from function file

function.user_operation()
#calling user operation from function file

#the given below function checks if the input is 1,2 or 3 or any other numbers
def check_user_input():
    loop = True
    #run while loop
    while loop == True:
        try:
            user_input = int(input("Enter the number: "))
            #checking user input
            if user_input == 1:
                function.purchaseBike()
                #calling purchase bike function
                
            elif user_input == 2:
                function.addStock()
                #calling add bike function

            elif user_input == 3:
                function.exit_system()
                #calling exit system function
                loop = False
                #loop terminates
            else:
                function.invalid_user_input()
                #calling to display invalid input function
        except ValueError:
            #value error if any other than integer is entered
            print("\n+++++++++++++++++++++++++++++++++++++++")
            print("Please provide Integer Value!!!!")
            print("+++++++++++++++++++++++++++++++++++++++\n")

            
check_user_input()

#calling function to run
