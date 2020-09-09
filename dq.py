class Dequeue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def insert_end(self, data):
        self.items.append(data)
 
    def insert_begining(self, data):
        self.items.insert(0, data)
 
    def remove_last(self):
        return self.items.pop()
 
    def remove_first(self):
        return self.items.pop(0)
    def display(self):
        print('Dequee elemets are',self.items)
 
q = Dequeue()
print('\t Menu')
print('1. Insert at Begining ')
print('2. Insert at End ')
print('3. Remove First ')
print('4. Remove Last')
print('5. Display')
print('6. Quit')
 
while True:
    operation = int(input('Enter Choice between 1 to 5 :  '))
    if operation == 1 :
        data=int(input("Enter a value "))
        q.insert_begining(data)
        q.display()
    elif operation == 2:
        data=int(input("Enter a value "))
        q.insert_end(data)
        q.display()
    elif operation == 3:
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Removed value from First : ', q.remove_first())
            q.display()
    elif operation ==4 :
        if q.is_empty():
            print('Dequeue is empty.')
        else:
            print('Removed value from Last: ', q.remove_last())
            q.display()
    elif operation == 5:
        q.display()
    elif operation>=6:
        break