from datetime import datetime
def read_data(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line_data = line.strip().split(',')
                data.append(line_data)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")
    return data

def display_options(data):
    print("Available venues:")

    for row in data[1:]:  # Skip the header row
        print(f"Kitta No.: {row[0]} - Location: {row[1]}, {row[2]} facing, Price: Rs.{row[4]}, Availability: {row[5]}")

def get_valid_kitta_no(data):
    while True:
        kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
        if any(row[0] == kitta_no for row in data[1:]):  # Check if kitta_no exists in data
            return kitta_no
        else:
            print("Invalid kitta no. Please enter a valid kitta number.")

def calculate_total_amount(venue_price, duration):
    total_amount = venue_price * duration
    vat_amount = 0.15 * total_amount
    final_amount = total_amount + vat_amount
    return total_amount, final_amount


def write_bill(username, phone_number, address, booked_venues, total_amount, vat_amount, final_amount):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the file name with the customer's name
    file_name = f"rental_bill_{username}.txt"
    
    with open(file_name, "w") as bill_file:
        bill_file.write("Rental Bill\n\n")
        bill_file.write(f"Date and Time: {date_time}\n")
        bill_file.write(f"Customer Name: {username}\n")
        bill_file.write(f"Phone Number: {phone_number}\n")
        bill_file.write(f"Address: {address}\n")
        
        # Write booked venues information
        bill_file.write("\nBooked Venues:\n")
        for venue in booked_venues:
            venue_name = venue[0]
            venue_city = venue[1]
            venue_district = venue[2]
            duration = venue[3]
            bill_file.write(f"- Venue: {venue_name}, {venue_city}, {venue_district} facing\n")
            bill_file.write(f"  Rental Period: {duration} months\n")
        
        # Write billing details
        bill_file.write(f"\nTotal Amount (excluding VAT): Rs.{total_amount}\n")
        bill_file.write(f"VAT (15%): Rs.{vat_amount}\n")
        bill_file.write(f"Final Amount (including VAT): Rs.{final_amount}\n")

    return file_name
def main():
    file_name = 'land.txt'  # File containing venue data
    data = read_data(file_name)

    display_options(data)

    kitta_no = get_valid_kitta_no(data)
    venue = next(row for row in data if row[0] == kitta_no)

    print(f"You have selected venue {venue[0]} in {venue[1]}, {venue[2]} facing, Price: Rs.{venue[4]}")

    duration = int(input("Enter the rental period in months: "))
    username = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    time = input("Enter the rental time: ")
    now =datetime.now()
    date_time = now.strftime("%Y-%m-%d %H-%M-%S")

    total_amount, final_amount = calculate_total_amount(int(venue[4]), duration)
    vat_amount = final_amount - total_amount

    print("\nRental Details:")
    print(f"Venue: {venue[1]}, {venue[2]} facing")
    print(f"Rental Date: {date_time}")
    print(f"Rental Period: {duration} months")
    print(f"Username: {username}")
    print(f"Phone Number: {phone_number}")
    print(f"Address: {address}")
    print(f"Total Amount (excluding VAT): Rs.{total_amount}")
    print(f"VAT (15%): Rs.{vat_amount}")
    print(f"Final Amount (including VAT): Rs.{final_amount}")

    write_bill(username, phone_number, address, venue, date_time, time, duration, total_amount, vat_amount, final_amount)
    print(f"Rental bill saved in{username}'bill.txt'.")

if __name__ == "__main__":
    main()
