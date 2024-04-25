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
