from operations import display_options, get_valid_kitta_no
from write import calculate_total_amount, write_bill
from read import read_data

def get_user_info():
    username = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = None  # Initialize to None
    while phone_number is None:
        try:
            phone_number = int(input("Enter your phone number: "))
            if phone_number <= 0:
                print("Please enter a positive integer for phone number.")
                phone_number = None  # Reset to None for retry
        except ValueError:
            print("Invalid input. Please enter a valid integer for phone number.")
    return username, phone_number, address

def main():
    file_name = "land.txt"  # File containing venue data
    data = read_data(file_name)
    display_options(data)

    username, phone_number, address = get_user_info()
    Newfunction(data, username, phone_number, address)

def Newfunction(data, username, phone_number, address):
    venues_info = []
    ultimate_total = 0

    while True:
        display_options(data)
        kitta_no, venue = get_valid_kitta_no(data)
        print(
            f"You have selected venue {venue[0]} in {venue[1]}, {venue[2]} facing, Price: Rs.{venue[4]}"
        )

        while True:
            try:
                duration = int(input("Enter the rental period in months: "))
                if duration <= 0:
                    print("Please enter a positive integer for duration.")
                else:
                    break  # Exit the loop if valid duration entered
            except ValueError:
                print("Invalid input. Please enter a valid integer for duration.")

        total_amount, vat_amount, final_amount = calculate_total_amount(int(venue[4]), duration)
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
            print("Your bill has been issued and saved in 'rental_bill.txt'. Thank you!")
            break  # Exit the loop if not selecting another venue

main()
