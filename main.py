from operation import add_furniture_info
from operation import sell_furniture
from read import see_furniture_info

def Show_Details():
    '''
    Description: Displays the details of the products available in the inventory. It retrieves and shows
    the current list of furniture items by calling the `see_furniture_info()` function.

    Arguments:
        None

    Return:
        None
    '''
    see_furniture_info()

def main():
    
    '''
    Description: Main entry point of the BRJ Furniture application. This function provides a menu with options
    to interact with the system, including showing product details, buying products from the manufacturer, 
    selling products to customers, or exiting the store. It handles user input and performs actions based on 
    the selected option, presenting the menu in a loop until the user decides to exit the store.

    Arguments:
        None

    Return:
        None
    '''
    
    print("\n\n-------------------  Welcome To BRJ Furniture  -----------------")
    print(f"{'':<2}{'_'*60}")
    
    while True:                                                                                                                                                     
        print(f"\n{'':<3}||----------------------------------------------------||")
        print(f"{'':<3}||  1 : Show Details of Products                      ||")
        print(f"{'':<3}||  2 : Inorder To Buy Product from manufacture       ||")
        print(f"{'':<3}||  3 : Inorder To sell Product with Customer         ||")
        print(f"{'':<3}||  4 : Incase If you want to leave the store         ||")
        print(f"{'':<3}||----------------------------------------------------||")
        
        Option = input("\n\n    Select the Number as the above information : ")
        print(f"{'-'*58}\n")
        
        
        if Option == '1':
            Show_Details() 
        elif Option == '2':
            add_furniture_info()
        elif Option == '3':
            sell_furniture()
        elif Option == '4':
            while True:
                Leaving_Option = input("\n--- Do you really want to leave store (Yes/No) : ").lower()
                if Leaving_Option == 'yes':
                    print("\n------------------------------------------")
                    print("          Thank you for Your Visit          ")
                    print("------------------------------------------\n")
                    exit()  
                elif Leaving_Option == "no":
                    print("\n--------------------------------------------------------")
                    print("               Once Again I kindly welcome you       \n")
                    break  
                else:
                    print("\n   Please input a valid option.")
        else:
            print("\n--- Please input from only the given options.")

if __name__ == '__main__':
    main()
