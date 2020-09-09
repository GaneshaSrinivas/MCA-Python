class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

r=int(input("Enter radis :"))
NewCircle = Circle(r)
print("Area of a Circle is  ",NewCircle.area())
print("Perimeter of a circle is ",NewCircle.perimeter())

"""
Output:

D:\MCA\4TH SEMESTER\PYTHON>python Circle.py
Enter radis :8
Area of a Circle is   200.96
Perimeter of a circle is  50.24

"""