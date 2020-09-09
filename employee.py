class Employee:
    __id=0
    __name=""
    __gender=""
    __age=""
    __designation=""
    __doj=""
    __bs=0

    def setData(self,id,name,gender,age,designation,doj,bs):
        self.__id=id
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__designation = designation
        self.__doj=doj
        self.__bs=bs

    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("Age\t:", self.__age)
        print("Designation\t:", self.__designation)
        print("Date of Joining\t:",self.__doj)
        print("Basic Salary\t:", self.__bs)

def main():
    emp=Employee()
    emp.setData(1,'Ganesha','M','24',"Developer",'27/08/2019',45000)
    emp.showData()
	
if __name__=="__main__":
    main()
