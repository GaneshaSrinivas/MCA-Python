
try:
    dividend = float(input("Please enter the dividend: "))
    divisor = float(input("Please enter the divisor: "))
    quotient = dividend / divisor
    quotient_rounded = round(quotient)
    print('Result = ',quotient)
    print('Rounded Results = ',quotient_rounded)
except ValueError:
    print("The divisor and dividend have to be numbers!")
except ZeroDivisionError:
    print("The dividend may not be zero!")