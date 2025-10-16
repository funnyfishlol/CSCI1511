"""
UPC Code Verifier
Nathan Henneman
Asks for UPC Code and returns if the code is valid and the check digit 
October 16, 2025
"""
def find_UPC(digits):
    digits = str(digits)
    sum = 0
    for i in range (0, len(digits)):
        if(i%2==0):
            sum += int(digits[i])*3
        else:
            sum += int(digits[i])
    sum_mod = sum%10
    print(sum_mod)
    if(sum_mod == 0):
        print(f"Your UPC Code is valid. Check digit: {digits[-1]}")
    else:
        print("Your UPC Code is not valid.")    

while True:
    find_UPC(input("Enter a UPC Code: "))