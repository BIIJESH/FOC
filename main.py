from operations import display_options,get_valid_kitta_no
from write import calculate_total_amount, write_bill
from read import read_data
def main():
    while True:
        file_name = "land.txt"  # File containing venue data
        data = read_data(file_name)
        display_options(data)

        # Initialize user information
        username = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        address = input("Enter your address: ")
        if not username.strip() or not phone_number.strip() or not address.strip():
                print("Please provide valid customer name, phone number, and address.")  # Print an error message if any field is empty
        else:
            break
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

main()
