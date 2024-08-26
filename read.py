def Information_R(file_path):
    
    '''
    Description: Reads the entire content of a file specified by `file_path` and returns it as a string.

    Arguments:
        file_path (str): The path to the file that needs to be read.

    Return:
        str: The content of the file as a string.
    '''
    with open(file_path, 'r') as file:
        return file.read()
    
    
def see_furniture_info():
    
    '''
    Description: Retrieves and displays the details of the furniture products from the 'Furniture_info.txt' file. 
    The function reads the file content, checks if there are any entries, and prints the details in a formatted table.
    If no furniture information is available, it displays an appropriate message.

    Arguments:
        None

    Return:
        None
    '''
    lines = Information_R('Furniture_info.txt').splitlines()
    
    if not lines:
        print("No furniture information available.\n")
        return
    
    print("\n\n\n\n")
    print(f"{'':28}Details of Our Available Products  ----->\n")
    print('-' * 110)
    print(f"{'':<10}{'ID':<10} {'Company':<35} {'Item':<25} {'Quantity':<15} {'Price':<10}")
    print('=' * 110)
    
    for line in lines:
        parts = line.split(',')
        if len(parts) == 5:
            print(f"{'':<10}{parts[0]:<10} {parts[1]:<35} {parts[2]:<25} {parts[3]:<15} {parts[4]:<10}")
    
    print('-' * 110 + '\n')





