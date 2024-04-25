
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
