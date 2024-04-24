from read import read ,print_rent_bill
from operations import display
from write import modify_data,rent_invoice
invoice = [] #Creating an empty list to store invoice data.
def rent():
    while True:    
        customer_name = input("Enter your name: ")  # Prompt the user to enter their name.
        phone_no = input("Enter your phone number:")
        address = input("Enter your address:")
        
        if not customer_name.strip() or not phone_no.strip() or not address.strip():
            print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
        else:
            break
    
    rent = True  # Initialize rent before the loop

    while rent: 
        display()  # Call the 'display' function to show a table.
        kitta_no_str = input('Enter the kitta no. of the land you would like to rent ->')
        
        if not kitta_no_str:
            print("Kitta number is required!")
        else:
            kitta_no = int(kitta_no_str)  # Convert kitta_no_str to an integer
            
            if kitta_no > 110 or kitta_no < 101:
                print("Please select a valid kitta number from 101 to 110")
            else:
                data = read()  # Call the 'read' function to retrieve data.
                
                # Check availability for the selected kitta
                for row in data:
                    land_id = int(row[0])  # Convert land ID to integer
                    availability = row[-1]  # Availability is the last element
                    if land_id == kitta_no:
                        if availability == "Not Available":
                            print(f"Kitta {kitta_no} is not available for rent.")
                        else:
                            duration = int(input("Enter the rental period in months ->"))
                            print("Selected land is rented successfully.")
                            
                            # Ensure kitta_no is within the valid range for data
                            if kitta_no >= 0 and kitta_no < len(data):
                                price = int(data[kitta_no][3].strip().strip("Rs."))
                                city = data[kitta_no][2]
                                direction = data[kitta_no][3]
                                area = data[kitta_no][4]
                                total_rate = price
                                
                                invoice.append([price, city, direction, area, total_rate])
                                modify_data(data)
                            else:
                                print("Error: Invalid kitta number.")
                        
                        while True:
                            user_input = input("Would you like to purchase anything else? (Y/N): ").upper()
                            
                            if user_input == "Y":
                                break
                            elif user_input == "N":
                                rent = False
                                rent_invoice(customer_name, invoice)
                                print("\n\n\n\n")
                                print_rent_bill(customer_name)
                                break
                            else:
                                print("Please enter Y or N only.")

 
    
