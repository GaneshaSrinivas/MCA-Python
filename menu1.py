import sys
from array import *

def menu():
    print("***Select the option of your choice***")

    choice=input("""
    A: Enter the element to insert into the array.
    B: Largest Element in the Array.
    C: Addition of two parts of the array.
    D: Find the array is monotonic or not.
    X: Exit.
    Please enter your choice:""") 
    if choice == "A" or choice =="a":
        insert()
        menu()
    elif choice == "B" or choice =="b": 
        large()
        menu()
    elif choice == "C" or choice == "c": 
        add()
        menu()
    elif choice == "D" or choice == "d": 
        mono()
        menu()
    elif choice=="X" or choice=="x": 
        sys.exit
    else:
        print("Invalid Option!!!!!") 
        print("Please try again")

def insert(): 
    global arr
    arr=array('i',[])
    print("Enter the number of elements?:",end="") 
    n=int(input())
    for i in range(n):
        print("Enter the element:",end="") 
        arr.append(int(input()))
    print("**************************************") 
    print("The array is:")
    print(arr)
    print(type(arr))
    print("**************************************")

def large(): 
    print("**************************************") 
    print("The largest element in the array is :",max(arr)) 
    print("**************************************")

def add():
    half=len(arr)//2 
    m=arr[:half] 
    n=arr[half:] 
    o=m+n
    print("**************************************") 
    print("First half of the array:")
    print(m)
    print("Second half of the array:") 
    print(n)
    print("After adding first part with the second part:") 
    print(o) 
    print("**************************************")

def mono(): 
    print("**************************************") 
    print("The given array:",arr)
    print("The array is monotonic:",all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)) or (all(arr[i] >= arr[i+1] for i in range(len(arr) - 1))))
    print("**************************************")


menu()
