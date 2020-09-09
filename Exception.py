class GuessNumberException(Exception):
    def __init__(self,arg):
        self.msg=arg
def GuessNumber(m):
    if(m>15):
        raise GuessNumberException("Value too large")
    elif(m<15):
        raise GuessNumberException("Value too less")
    else:
        raise GuessNumberException("Congrats you have guessed the correct number")
        

while True: 
    n=int(input("Enter a number to guess(1-30): "))
    try:
        GuessNumber(n)
    except GuessNumberException as me:
        print(me)
    chk=input("Do you want guess again(Y/N): ")
    if(chk=='n'):
        break

