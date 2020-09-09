"""
Create a Student class and initialize it with name and roll number. Create
methods to :
i) Display - It should display all information of the student.
ii) setAge - It should assign age to student
iii) setMarks - It should assign marks to the student.
Write the main program to access these methods.
"""

class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print("\tName:\t ",self.name)
    print("\tRoll Number: ",self.roll)
    print("\tAge:\t ",self.age)
    print("\tMarks:\t ",self.marks)
  def setAge(self):
    self.age=24
  def setMarks(self):
    self.marks = 95

if __name__ == "__main__" :
    s=Student('Ganesha','1BF18MCA06')
    print("\t\tStudent Information")
    s.setMarks()
    s.setAge()
    s.display()

"""
    OutPut:
    D:\MCA\4TH SEMESTER\PYTHON>python StudentInformation.py
                Student Information
        Name:     Ganesha
        Roll Number:  1BF18MCA06
        Age:      24
        Marks:    95

"""