#Profit
Actual_cost=float(input("Please Enter the Actual Product Price:"))
Sale_amount=float(input("Please Enter the Sales Amount:"))

if (Sale_amount>Actual_cost):
    amount=Sale_amount-Actual_cost
    print("Total Profit={0}".format(amount))
else:
    print("No profit!!!!!!")
        