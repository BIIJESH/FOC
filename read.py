import os

print(os.path.isfile("land.txt"))


def read():
    try:
        data = []
        column = [
            "Kitta No.",
            " City/District ",
            " Land Faced ",
            " Anna ",
            " Price ",
            " Availability ",
        ]
        data.append(column)  # Adding the column headers to the data list.
        print(data)
        # Availability is the last element

        file = open("land.txt", "r")  # Opening the file 'land.txt' in read mode.
        for line in file.readlines():
            data.append(
                line.rstrip().split(",")
            )  # Parsing each line from the file and appending it to the data list.
        file.close()  # Closing the file after reading.

    except FileNotFoundError:
        print(f"Error: File not found!")

    return data




def print_rent_bill(customer_name):
    file = open("Rented By " + customer_name + ".txt", "r")
    bill = file.read()
    print(bill)
    file.close()


def print_return_bill(customer_name):
    file = open(
        "Returned By " + customer_name + ".txt", "r"
    )  # Opening the sell bill file associated with the customer name in read mode.
    bill = file.read()  # Reading the contents of the sell bill file.
    print(bill)  # Orinting the contents of the sell bill.
    file.close()  # Cloasing the sell bill file.


def loopdata():
    with open("land.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Remove leading and trailing whitespaces and split the line by commas
            data = line.strip().split(",")
            # Process the data as needed
            print(data)  # For example, print each line's data




# Initialize an empty list to store the data
data = []

# Open the file 'land.txt' in read mode
with open('land.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Remove leading and trailing whitespaces and split the line by commas
        line_data = line.strip().split(',')
        # Append the line's data to the main data list
        data.append(line_data)

# Print the data to verify
print(data)
