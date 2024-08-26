import datetime

def Information_W (furniture_details):
    
    '''
    Description: Appends furniture details to the 'Furniture_info.txt' file. 
    The function opens the file in append mode and writes the provided 
    furniture details to the end of the file.

    Arguments:
        furniture_details (str): A string containing the details of the furniture 
        to be appended to the file.

    Return:
        None
    '''
    
    with open('Furniture_info.txt', 'a') as file:
        file.write(furniture_details)


def generate_invoice(transactions, name, is_employee):
    
    '''
    Description: Generates an invoice for a list of furniture transactions, either for an employee 
    or a customer. The function creates a text file with a unique name based on the recipient's name 
    and the current timestamp. It includes a detailed breakdown of each transaction, including furniture 
    ID, manufacturer, product name, quantity, price, shipping cost, and location. The invoice also 
    calculates and displays the total amount, shipping cost, VAT (13%), and provides a thank you message.

    Arguments:
        transactions (list of tuples): A list where each tuple contains transaction details 
        (furniture ID, manufacturer, product name, quantity, price, shipping cost, location).
        name (str): The name of the customer or employee for whom the invoice is generated.
        is_employee (bool): A flag indicating whether the invoice is for an employee (True) 
        or a customer (False).

    Return:
        None
    '''
    
    formatted_name = name.replace(" ", "_")
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    if is_employee:
        invoice_filename = f"{formatted_name} (Brj Furniture-Staff) - Invoice {timestamp}.txt"
    else:
        invoice_filename = f"{formatted_name} (Customer) - Invoice {timestamp}.txt"

    with open(invoice_filename, 'w') as file:
        
        # Header of the invoice txt file
        file.write("=" * 60 + "\n")
        file.write("INVOICE".center(60) + "\n")
        file.write("=" * 60 + "\n\n")
        
        # Customer or Staff messege details and thankfullness
        file.write(f"Thank you for your purchase, Mr./Ms. {name}!\n")
        file.write("We truly appreciate your business. If you need anything,\n")
        file.write("please remember us!\n\n")
        
        # Invoice Information
        file.write(f"Invoice for {name}\n")
        file.write(f"Date of purchase: {datetime.datetime.now().strftime('%Y-%m-%d    Time of purchase :%H:%M:%S')}")
        file.write(f"\n{'=' * 60 }\n\n")
        
        # initial items details
        total_amount = 0
        total_shipping_cost = 0
        total_vat = 0

        for transaction in transactions:
            furniture_id, manufacturer, product_name, quantity, price, shipping_cost, location = transaction
            
            amount = price * quantity
            shipping_cost_total = shipping_cost + quantity
            vat_amount = 0.13 * amount
            
            total_shipping_cost += shipping_cost_total
            total_vat += vat_amount
            total_amount += amount

            file.write(f"Furniture ID: {furniture_id}\n")
            file.write(f"Manufacturer: {manufacturer}\n")
            file.write(f"Product Name: {product_name}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Price per Item: ${price:.2f}\n")
            file.write(f"Shipping Cost: ${shipping_cost_total:.2f}\n")
            file.write(f"Location: {location}\n")
            file.write(f"Total for this item: ${amount:.2f}\n")
            file.write("-" * 60 + "\n")

        total_amount_with_vat = total_amount + total_vat
        total_invoice_amount = total_amount_with_vat + total_shipping_cost

        file.write(f"\nTotal cost without shipping cost and VAT: ${total_amount:.2f}\n")
        file.write(f"Total shipping cost: ${total_shipping_cost:.2f}\n")
        file.write(f"Total VAT Amount: ${total_vat:.2f}\n")
        file.write(f"Total Amount with VAT (No shipping cost): ${total_amount_with_vat:.2f}\n")
        file.write(f"Total Invoice Amount with shipping cost: ${total_invoice_amount:.2f}\n\n")

        file.write("=" * 60 + "\n")
        file.write("Thank you for your business! If you have any questions,\n")
        file.write(f"please contact us at (123) 456-7890 or email info@{manufacturer}.com.\n")
        file.write("Terms and Conditions apply.\n")
        file.write("=" * 60 + "\n")