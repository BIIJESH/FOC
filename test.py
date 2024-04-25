from datetime import datetime


def read_data(file_name):
    data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_data = line.strip().split(",")
                data.append(line_data)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")
    return data


# def display_options(data):
# it reads data from  the text file
# print("-----------------------------------------------------------------------------------------------")
# for row in data: # using for loop so it iterates over each row in the file_data
#     print(row[0].ljust(9) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
#     for each in row[1:]:
#         print(each.ljust(16) + '|', end='') #prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
#     print() #Print a new line after printing each row
#     print("-----------------------------------------------------------------------------------------------")
# def display_options(data):
#     print("Available venues:")
#     for row in data[0:]:  # Skip the header row
#         print(f"Kitta No.: {row[0]} - Location: {row[1]}, {row[2]} facing, Price: Rs.{row[4]}, Availability: {row[5]}")


def display_options(data):
    # it reads data from  the text file
    print(
        "-----------------------------------------------------------------------------------------------"
    )
    for row in data:  # using for loop so it iterates over each row in the file_data
        print(
            row[0].ljust(9) + "|", end=""
        )  # prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        for each in row[1:]:
            print(
                each.ljust(16) + "|", end=""
            )  # prints first element of the row and left-align it with a width if 4 characters, followed by a '|'
        print()  # Print a new line after printing each row
        print(
            "-----------------------------------------------------------------------------------------------"
        )


def get_valid_kitta_no(data):
    while True:
        kitta_no = input("Enter the kitta no. of the land you would like to rent: ")
        if any(
            row[0] == kitta_no for row in data[0:]
        ):  # Check if kitta_no exists in data
            venue = next(row for row in data if row[0] == kitta_no)
            if venue[-1].strip() == "Not Available":
                print("This venue is not available. Please choose another one.")
            else:
                return kitta_no, venue
        else:
            print("Invalid kitta no. Please enter a valid kitta number.")


def calculate_total_amount(venue_price, duration):
    total_amount = venue_price * duration
    vat_amount = 0.15 * total_amount
    final_amount = total_amount + vat_amount
    return total_amount, vat_amount, final_amount


def write_bill(username, phone_number, address, venues_info, ultimate_total):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("rental_bill.txt", "w") as bill_file:
        bill_file.write("Rental Bill\n\n")
        bill_file.write(f"Date and Time: {date_time}\n")
        bill_file.write(f"Customer Name: {username}\n")
        bill_file.write(f"Phone Number: {phone_number}\n")
        bill_file.write(f"Address: {address}\n")

        bill_file.write("\nVenue Details\n")
        for info in venues_info:
            kitta_nos, locations, rental_periods, prices = info
            total_price, total_vat, final_amount = prices

            bill_file.write(f"Kitta No.: {', '.join(kitta_nos)}\n")
            bill_file.write(f"Location: {', '.join(locations)}\n")
            bill_file.write(
                f"Rental Period: {', '.join(str(period) for period in rental_periods)} months\n"
            )
            bill_file.write(
                f"Price (excluding VAT): Rs.{', '.join(str(price) for price in total_price)}\n"
            )
            bill_file.write(f"VAT (15%): Rs.{total_vat}\n")
            bill_file.write(f"Final Amount (including VAT): Rs.{final_amount}\n")
            bill_file.write("\n")

        bill_file.write(
            f"Ultimate Total (including VAT) for all venues: Rs.{ultimate_total}\n"
        )


def main():
    file_name = "land.txt"  # File containing venue data
    data = read_data(file_name)
    display_options(data)

    # Initialize user information
    username = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")

    venues_info = []  # To store details of selected venues
    ultimate_total = 0  # Initialize ultimate total

    while True:
        display_options(data)
        kitta_no, venue = get_valid_kitta_no(data)
        print(
            f"You have selected venue {venue[0]} in {venue[1]}, {venue[2]} facing, Price: Rs.{venue[4]}"
        )

        duration = int(input("Enter the rental period in months: "))

        total_amount, vat_amount, final_amount = calculate_total_amount(
            int(venue[4]), duration
        )
        ultimate_total += final_amount  # Update ultimate total

        venues_info.append(
            (
                [venue[0]],
                [f"{venue[1]}, {venue[2]}"],
                [duration],
                ([total_amount], vat_amount, final_amount),
            )
        )

        choice = input("Do you want to select another venue? (Y/N): ").upper()
        if choice != "Y":
            write_bill(username, phone_number, address, venues_info, ultimate_total)
            print(
                "Your bill has been issued and saved in 'rental_bill.txt'. Thank you!"
            )
            break


if __name__ == "__main__":
    main()
