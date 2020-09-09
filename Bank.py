#Create a class to handle Bank transactions and display the transaction details.
class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 

if __name__ == "__main__" :
    s=Bank_Account() 
    s.deposit() 
    s.withdraw() 
    s.display() 

"""
Output:
D:\MCA\4TH SEMESTER\PYTHON>python Bank.py
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 1000

 Amount Deposited: 1000.0
Enter amount to be Withdrawn: 500

 You Withdrew: 500.0

 Net Available Balance= 500.0

"""