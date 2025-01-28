import sys

# Sales Tax Calculator
# Programmer: Austin Long
# Date: 1/28/2025

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    # set tax rate
    tax_rate = 0.07

    try:
        # input prices from user
        price_1 = float(input("Enter item 1's price: $"))
        price_2 = float(input("Enter item 2's price: $"))
        price_3 = float(input("Enter item 3's price: $"))
        price_4 = float(input("Enter item 4's price: $"))
        price_5 = float(input("Enter item 5's price: $"))

        # sum up prices
        subtotal = price_1 + price_2 + price_3 + price_4 + price_5

        # calculate sales tax amount
        tax_amount = tax_rate * subtotal

        # calculate total
        total = subtotal + tax_amount

        # display values to user
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${tax_amount:.2f}")
        print(f"Total: ${total:.2f}")
    except ValueError:
        # if invalid input, display error message and exit nonzero
        print("You must enter a valid floating point number. Do not include currency symbols.", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    calculate_total_purchase()