import datetime

def modify_data(data):
    file = open("laptops_data.txt", "w") #Opening the 'land.txt' file in write mode.
    for i in range(1, len(data)):
        each = data[i]
        file.write(f"{each[1]},{each[2]},{each[3]},{each[4]},{each[5]},{each[6]}\n") # writing the updated data to the file.
    file.close() #Closing the file after writing

def rent_invoice(customer_name,phone_no,address,invoice):

    total_amount = 0
    for x in invoice:
        total_amount += int(x[2])                      #Calculating the total amount by summing the net amounts of each item in the invoice.
    vat_amount = total_amount * 0.15                   #Calculating the VAT amount as 15% of the total amount.
    final_amount = total_amount + vat_amount          #Calculatinig the final amount including VAT..

    file = open( "Rented By"+ customer_name+".txt","w") #Opening the purchase invoice file for the specific distributor in write mode.

    file.write("------------------------------------------------------\n") 
    file.write("                   TECHNO PROPERTY NEPAL\n") 
    file.write("------------------------------------------------------\n") 

    file.write("Customer Name: " + customer_name + "\n")
    file.write("Phone Number:"+ phone_no +"\n")
    file.write("Address:"+address+"\n")
    file.write(f"Date & Time of Rent: {datetime.datetime.now()}\n") #Writing the current data and time to the invoice.
    file.write("------------------------------------------------------\n")                
    for i in invoice:
          file.write(f'Kitta No: {i[0]}\n') #Writing the kitta no of land in the invoice.
          file.write(f'City/District: {i[1]}\n') #Writing the location of land in the invoice.
          file.write(f'Land Faced: {i[2]}\n') #Writing the direction of land faced in the invoice.
          file.write(f'Net Amount: {i[3]}\n') #Writing the net amount of each land in the invoice.
          file.write("------------------------------------------------------\n")
    file.write(f"Total net amount : ${total_amount}\n") #Keeping record about the total net amount in the invoice.
    file.write(f"VAT amount (15%): ${vat_amount}\n") # Recording the VAT amount in the invoice.
    file.write(f"Amount including VAT: ${final_amount}") #Recording the final amount including VAT in the invoice.

    file.close() #Closing the purchase invoice file.


def return_invoice(invoice,duration,customer_name,phone_no,address):

    total_amount = 0
    for x in invoice:
        total_amount += int(x[2])                      #Calculating the total amount by summing the net amounts of each item in the invoice.
    vat_amount = total_amount * 0.15                   #Calculating the VAT amount as 15% of the total amount.
    final_amount = total_amount + vat_amount 

    file = open( "Returned By "+ customer_name+".txt","w") #Opening the sell invoice file for the specific customer in write mode.


    file.write("------------------------------------------------------\n") 
    file.write("                   TECHNO PROPERTY NEPAL\n") 
    file.write("------------------------------------------------------\n") 
    file.write("Customer name: " + customer_name + "\n")
    file.write("Phone Number:"+ phone_no +"\n")
    file.write("Address:"+address+"\n")
    file.write(f"Date & Time of Return: {datetime.datetime.now()}\n") #Recording the current date and time to the invoice .
    file.write("------------------------------------------------------\n")                
    for i in invoice:
        file.write(f'Kitta No: {i[0]}\n') #Writing the kitta no of land in the invoice.
        file.write(f'City/District: {i[1]}\n') #Writing the location of land in the invoice.
        file.write(f'Land Faced: {i[2]}\n') #Writing the direction of land faced in the invoice.
        file.write(f'Duration: {i[3]}\n') #Writing the duration of land rental in invoice
        file.write(f'Net Amount: {i[3]}\n') #Writing the net amount of each land in the invoice.
        file.write("------------------------------------------------------\n")
    file.write(f"Total net amount : ${total_amount}\n") #Keeping record about the total net amount in the invoice.
    file.write(f"VAT amount (15%): ${vat_amount}\n") # Recording the VAT amount in the invoice.
    file.write(f"Amount including VAT: ${final_amount}") #Recording the final amount including VAT in the invoice.

                
    file.close() #Closing the sell invoice file after writing.
