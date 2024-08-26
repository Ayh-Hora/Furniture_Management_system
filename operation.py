from read import Information_R , see_furniture_info
from write import Information_W
from write import generate_invoice


#setting the variable for design
design_line = '-'*60
design_line2 = '='*60

def add_furniture_info():
    
    '''
    Description: Manages the process of adding or updating furniture information in the 'Furniture_info.txt' file.
    This function allows staff to input details about furniture, including ID, manufacturer, product name, 
    quantity, price, location, and the province for calculating shipping costs. It validates inputs, updates 
    existing entries if the furniture ID already exists, or adds new entries if the ID is new. It also updates 
    the file with the new or modified information and generates an invoice for the transaction. The function 
    prompts the user to continue adding more furniture or finalize the process.

    Arguments:
        None

    Return:
        None
    '''

    file_path = 'Furniture_info.txt'
    transactions = []
    existing_entries = {}

    
    # Load existing furniture entries from the file
    for line in Information_R(file_path).splitlines():
        parts = line.split(',')
        if len(parts) == 5:
            furniture_id = int(parts[0])
            manufacturer, product_name, quantity, price = parts[1], parts[2], int(parts[3]), float(parts[4].replace('$', ''))
            existing_entries[furniture_id] = [manufacturer, product_name, quantity, price]
            
    
    while True:
        try:
            name = input("\n--- Enter the name of staff: ").strip()
            if not all(char.isalpha() or char.isspace() for char in name):
                print(f"\n{design_line}\n{'':<8}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                continue
            if not name:
                print(f"\n{design_line}\n{'':<8}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                continue
            break
                        
        except:
            print(f"\n{design_line}")
            print(f"{'':<8}Invalid input --> Please enter a name\n")
            
    while True:
        while True:
            try:
                furniture_id = int(input("\n--- Enter the ID of the furniture: "))
                if furniture_id < 0:
                    print(f"\n{design_line}")
                    print(f"{'':<8}ID cannot be negative.\n")
                    continue
                break
            except ValueError:
                print(f"\n{design_line}")
                print(f"{'':<8}Invalid input --> Please enter a numeric value.\n")

        if furniture_id in existing_entries:
            
            # Update existing entry
            print(f"\nID {furniture_id} already exists. Updating existing entry.")
            print(f"{design_line}")
            manufacturer, product_name, old_quantity, old_price = existing_entries[furniture_id]
            print(f"--- Existing Quantity : {old_quantity}\n--- Existing Price for single items : ${old_price:.2f}")

            while True:
                try:
                    quantity = int(input("\n\n--- Enter the quantity of the furniture: "))
                    if quantity < 0:
                        print(f"\n{design_line}")
                        print(f"{'':<8}Quantity cannot be negative.\n")
                        continue
                    break
                except ValueError:
                    print(f"\n{design_line}")
                    print(f"{'':<8}Invalid input --> Please enter a numeric value.\n")

       
            # Update the existing entry with new quantity and price
            existing_entries[furniture_id][2] += quantity
            existing_entries[furniture_id][3] = price
            print(f"\n--- Remaining: {existing_entries[furniture_id][2]}")

        else:
            print(f"\nID {furniture_id} donot  exists. So Adding items in entry.")
            print(f"\n{design_line}")
            while True:
                manufacturer = input("\n--- Enter the name of the Manufacturer: ").strip()
                if not all(char.isalpha() or char.isspace() for char in manufacturer):
                    print(f"\n{design_line}")
                    print(f"{'':<5}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                    continue
                break

            while True:
                product_name = input("\n--- Enter the name of furniture: ").strip()
                if not product_name:
                    print(f"\n{design_line}")
                    print(f"{'':<5}Input cannot be empty. Please enter a valid product name.\n")
                    continue
                if not all(char.isalpha() or char.isspace() for char in product_name):
                    print(f"\n{design_line}")
                    print(f"{'':<5}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                    continue
                break

            while True:
                try:
                    quantity = int(input("\n--- Enter the quantity of the furniture: "))
                    if quantity <=0:
                        print(f"\n{design_line}")
                        print("Quantity must be greater than 0\n")
                        continue
                    break
                except ValueError:
                    print(f"\n{design_line}")
                    print("Invalid input --> Please enter a numeric value.\n")

            while True:
                price_input = input("\n--- Enter the price of the furniture (e.g., 400 or $400 ): ")
                if not price_input and price_input<=0:
                    print(f"\n{design_line}")
                    print("Please enter the price.\n")
                    continue
                try:
                    price = float(price_input.replace('$', ''))
                    if price < 0:
                        print(f"\n{design_line}")
                        print("Price cannot be negative.\n")
                        continue
                    break
                except ValueError:
                    print(f"\n{design_line}")
                    print(f"{'':<8}Invalid input --> Please enter a numeric value.\n")

            # Add new entry to the dictionary
            existing_entries[furniture_id] = [manufacturer, product_name, quantity, price]

        while True:
            location = input("\n--- Enter the Location: ").strip()
            if not location:
                print(f"\n{design_line}")
                print(f"{'':<5}Input cannot be empty. Please enter a valid location name.\n")
                continue
            if not all(char.isalpha() or char.isspace() for char in location):
                print(f"\n{design_line}")
                print(f"{'':<5}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                continue
            break

        while True:
            try:
                province = int(input("\n--- Select Your Province for shipping cost (1-7): "))
                if 1 <= province <= 7:
                    costs = [68, 109, 199, 205,344, 419, 498]
                    shipping_cost_per_item = costs[province - 1]
                    total_shipping_cost = shipping_cost_per_item + quantity
                    print(f"\n{design_line2}")
                    print(f"{'':<8}--- Shipping cost per item is ${shipping_cost_per_item}\n{'':<8}--- Total shipping cost is ${total_shipping_cost}.\n")
                    break
                else:
                    print(f"\n{design_line}")
                    print(f"{'':<8}Invalid province selection. Please choose a number between 1 and 7.")
            except ValueError:
                print(f"\n{design_line}")
                print(f"{'':<8}Invalid input --> Please enter a numeric value between 1 and 7.")

        # Write all entries back to the file
        with open(file_path, 'w') as file:
            for fid, (man, pname, qty, prc) in existing_entries.items():
                file.write(f"{fid},{man},{pname},{qty},${prc:.2f}\n")

        # Record the transaction details
        transactions.append([furniture_id, manufacturer, product_name, quantity, price, shipping_cost_per_item, location])
        print("=" * 68)
        print("     --- Furniture is bought successfully from manufacturer --       ")
        print("=" * 68 + "\n")

         # Prompt user to continue or finalize
        while True:
            re_sell = input("--- Want to buy more furniture? (Yes/No): ").strip().lower()
            if re_sell == 'yes':
                break
            elif re_sell == 'no':
                if transactions:
                    generate_invoice(transactions, name=name, is_employee=True)
                    print("\n------------------------------------------")
                    print("          Thank you for Your Visit          ")
                    print("        please collect your invoice          ")
                    print("------------------------------------------\n")
                    exit()
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.\n")
        




def sell_furniture():
    '''
    Description: Manages the selling of furniture from the 'Furniture_info.txt' file. This function allows
    customers to view available furniture details, input their name, and specify the quantity they wish to buy.
    It validates inputs, updates the quantity of the sold furniture in the file, calculates shipping costs 
    based on the selected province, and generates an invoice for the transaction. The function handles multiple 
    sales transactions and prompts the user to continue selling or finalize the process.

    Arguments:
        None

    Return:
        None
    '''
    
    file_path = 'Furniture_info.txt'
    transactions = []
    
    see_furniture_info()
     
    print(f"\n\n\n{'':<8}Just buy if only you are satisfied with the price range of available items\n{'='*92}\n")
    print(f"{'':<9}----- Satisfied = Type 'Yes' and continue purchase\n\n{'':<9}----- Not satisfied = Type 'No' and leave the store: ")
    while True:
        leave_input = input(f"{'':<25}(Yes/No) : ").lower().strip()
        if leave_input == 'yes':
            break
        elif leave_input == 'no':
            print("\n--------------------------------------------------------------------------------------------------------")
            print("         This time we are extremely sorry, Next Time we will deduce the price of the product ----          ")
            print("---------------------------------------------------------------------------------------------------------\n")
            exit()
        else:
            print(f"\n{'':<7}{'='*55}")
            print(f"\n{'':<9}Invalid input. Please prompt 'Yes' or 'No'.\n")
    
    # Get and validate customer name
    while True:
        customer = input(f"\n{'':<10}--- Enter your Name (Customer): ").strip()
        if not customer:
            print(f"\n{'':<7}{'='*55}")
            print(f"{'':<8}Input cannot be empty. Please enter a valid buyer name.\n")
            continue
        if any(char.isdigit() for char in customer):
            print(f"\n{'':<7}{'='*55}")
            print(f"{'':<8}Invalid input --> Please enter a valid buyer name (alphabetic characters and spaces only).\n")
            continue
        break

    while True:
        # Load existing furniture information
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
    
        # Get and validate furniture ID
        while True:
            furniture_id = input(f"\n--- Enter the ID of the furniture: ").strip()
            if not furniture_id.isdigit():
                print(f"\n{design_line}")
                print(f"{'':<8}Invalid ID --> Please enter a numeric value.\n")
                continue
            furniture_id = int(furniture_id)
            if furniture_id < 0:
                print(f"\n{design_line}")
                print("ID cannot be negative.\n")
                continue

            # Check if the product exists
            product_exist = False
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 5 and parts[0].strip() == str(furniture_id):
                    available_quantity = int(parts[3].strip())
                    price = float(parts[4].strip().replace('$', ''))
                    product_exist = True
                    break

            if product_exist:
                print(f"\n----Furniture ID = {furniture_id}\n----Available quantity = {available_quantity}\n----Price of product is ${price:.2f}\n")
                break
            else:
                print(f"\nFurniture ID does not exist in our product details.")

        # Get and validate quantity
        while True:
            try:
                quantity = int(input(f"\n--- Enter the quantity to Buy as a Customer: "))
                if quantity <= 0:
                    print(f"\n{design_line}")
                    print(f"{'':<5}please add the valid quantity\n")
                    continue
                if quantity > available_quantity:
                    if available_quantity == 0:
                        print(f"\n\n{'='*90}")
                        print(f"{'':<5}This amount of quantity is not available right now, buy another product instead")
                        return sell_furniture()
                    else:
                        print(f"{'':<5}--- The quantity you have asked is not available right now")
                        print(f"{'':<5}--- Available quantity = {available_quantity} ")
                        continue
                break                      
            except ValueError:
                print(f"\n{design_line}")
                print("Invalid input --> Please enter a numeric value.\n")

        # Update quantity in the file
        updated_lines = []
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 5 and parts[0].strip() == str(furniture_id):
                manufacturer, product_name, current_quantity, price = parts[1], parts[2], int(parts[3]), float(parts[4].replace('$', ''))
                new_quantity = current_quantity - quantity
                parts[3] = str(new_quantity)
                updated_lines.append(','.join(parts))
                print(f"Updated quantity for Furniture ID {furniture_id}: {new_quantity}\n")
            else:
                updated_lines.append(line.strip())

        with open(file_path, 'w') as file:
            file.write('\n'.join(updated_lines) + '\n')

        # Get and validate location
        while True:
            location = input(f"\n--- Enter the Location: ").strip()
            if not location:
                print(f"\n{design_line}")
                print(f"{'':<5}Input cannot be empty. Please enter a valid location name.\n")
                continue
            if not all(char.isalpha() or char.isspace() for char in location):
                print(f"\n{design_line}")
                print(f"{'':<5}Invalid input --> Please enter alphabetic characters only (spaces allowed).\n")
                continue
            break

        # Get and validate province and calculate shipping cost
        while True:
            try:
                province = int(input("--- Select Your Province (1-7): "))
                if 1 <= province <= 7:
                    costs = [68, 109, 199, 205, 344, 419, 498]
                    shipping_cost_per_item = costs[province - 1]
                    total_shipping_cost = shipping_cost_per_item + quantity
                    print(f"\n{design_line2}")
                    print(f"{'':<8}Shipping cost per item is ${shipping_cost_per_item}. Total shipping cost is ${total_shipping_cost}.\n")
                    break
                else:
                    print(f"\n{design_line}")
                    print(f"{'':<8}Invalid province selection. Please choose a number between 1 and 7.")
            except ValueError:
                print(f"\n{design_line}")
                print(f"{'':<8}Invalid input --> Please enter a numeric value between 1 and 7.")

        transactions.append((furniture_id, manufacturer, product_name, quantity, price, shipping_cost_per_item, location))

        print("=" * 68)
        print("     --- Furniture is bought successfully from Brj Furniture --       ")
        print("=" * 68 + "\n")

        while True:
            re_sell = input("\n--- Want to Buy more furniture? (Yes/No): ").strip().lower()
            if re_sell == 'yes':
                break
            elif re_sell == 'no':
                if transactions:
                    generate_invoice(transactions, name=customer, is_employee=False)
                    
                    print("\n------------------------------------------")
                    print("          Thank you for Your Visit          ")
                    print("        please collect your invoice          ")
                    print("------------------------------------------\n")
                    exit()
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.\n")
