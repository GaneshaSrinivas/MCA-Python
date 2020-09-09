class Error(Exception):
       pass

class NumberLessThanOneException(Error):
   pass

try:
    avg=float(input('Enter a average marks of a class : '))
    students=int(input('Enter total number of students : '))
    if students<1:
        raise NumberLessThanOneException
except ValueError:
    print('Entered value should be numbers')
except NumberLessThanOneException:
    print('Total students should greater than 1')
