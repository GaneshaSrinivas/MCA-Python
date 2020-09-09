class Error(Exception):
   pass

class ValueTooSmallException(Error):
   pass

class ValueTooLargeException(Error):
   pass

number = 10

while True:
   try:
       n = int(input("Enter a number: "))
       if n < number:
           raise ValueTooSmallException
       elif n > number:
           raise ValueTooLargeException
       else:
            print('You gussed it correctly! ')
       break
   except ValueTooSmallException:
       print("Value entered is too small, try again!")
   except ValueTooLargeException:
       print("Value entered is too large, try again!")
