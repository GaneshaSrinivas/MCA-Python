"""
Derive a class Contact from the base classes Person and Address and use their
methods to print the contact information.
"""

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email= str(email)
    def show(self):
        print(self.name + ' \n' + self.email)

class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)
    def show(self):
        Person.show(self)
        Address.show(self)
        print()

if __name__ == "__main__" :
    print("Contact Information ")
    c=Contact("Ganesha","ganeshas.mca18@bmsce.ac.in","Anekal","Bengaluru")
    c.show()

"""
Output:

D:\MCA\4TH SEMESTER\PYTHON>python Contact.py
Contact Information
Ganesha
ganeshas.mca18@bmsce.ac.in
Anekal
Bengaluru
"""