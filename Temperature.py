"""
Create a Temprature class. Create two methods :
i) convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
ii) convertCelsius - It will take Fahrenheit and will convert it into Celsius.
Write the main program to access these methods.
"""

class Temprature():
    def CelsiustoFahrenheit(self):
        c=int(input('Enter temperatire in Celisius: '))
        f = (9/5)*c + 32
        print(c, "degree celsius is equal to:",f,"Fahrenheit")
    def FahrenheittoCelsius(self):
        f=float(input('Enter temperatire in Fahrenheit: '))
        c = (5/9)*(f - 32)
        print(f,"Fahrenheit is equal to:",c,"degree celsius")

if __name__ == "__main__" :
    t=Temprature()
    t.CelsiustoFahrenheit()
    t.FahrenheittoCelsius()

"""
Output :
D:\MCA\4TH SEMESTER\PYTHON>python Temperature.py
Enter temperatire in Celisius: 36
36 degree celsius is equal to: 96.8 Fahrenheit
Enter temperatire in Fahrenheit: 96.8
96.8 Fahrenheit is equal to: 36.0 degree celsius
"""
