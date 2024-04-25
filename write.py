from datetime import datetime
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


