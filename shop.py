#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program calculates area and circumference.
#  from user input

import constants


def main():
    # this function calculates total from subtotal and tax
    # input
    quantity = input("Enter the Item(s) Quantity, $100 per item: Pcs.")
    print("")

    # Process and Output
    try:
        quantity_as_int = int(quantity)
        item = quantity_as_int * constants.cost_per_item
        print("Item(s) Total before Tax: ${0:,.2f}".format(item))
        print("")
        tax = item * constants.HST
        total = tax + item
        print("Item(s) Total after Tax: ${0:,.2f}".format(total))
        print("")
        if total > constants.minimum_discount:
            print("Good News!!, You got a 10% OFF Discount")
            print("")
            subtotal = total*constants.Discount
            sub_total = total - subtotal
            print("Cost before Discount ${0:,.2f}, and the total cost\
        after Discount is: ${1:,.2f}".format(total, sub_total))
            print("")
            print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}"
                  .format(tax, sub_total))
        else:
            print("Buy 9 or more items to get a Discount")
            print("")
            print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}"
                  .format(tax, total))
    except Exception:
        print("This is Not a Quantity")
    finally:
        print("")
        print("Thanks For Shopping")


if __name__ == "__main__":
    main()
