"""Tip Suggestions - Nathan Henneman - Takes a total from a bill and prints out suggestions for a 15% and 20% tip. - September 5, 2025"""

# Without Rounding
bill = 39.76
bill_15tip = bill * 0.15
bill_20tip = bill * 0.20
print(f"\nWithout Rounding: \n15% Tip: {bill_15tip} \n20% Tip: {bill_20tip} \nBill with 15% Tip: {bill + bill_15tip} \nBill with 20% Tip: {bill + bill_20tip}")

# With Rounding
bill_15tip = round(bill_15tip, 2)
bill_20tip = round(bill_20tip, 2)
print(f"\nWith Rounding: \n15% Tip: {bill_15tip} \n20% Tip: {bill_20tip} \nBill with 15% Tip: {bill + bill_15tip} \nBill with 20% Tip: {bill + bill_20tip}")