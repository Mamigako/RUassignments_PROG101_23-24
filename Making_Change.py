item_price = int(input())
amount_paid = int(input())

change_list = [20, 10, 5, 2, 1]


# Check whether change is needed, if so print largest possible bill until change amount is 0.


if item_price < amount_paid:
    change_amount = amount_paid - item_price

    for bill in change_list:
        if bill <= change_amount:
            print(bill)

            change_amount = change_amount - bill

            while change_amount >= bill:
                print(bill)
                change_amount = change_amount - bill