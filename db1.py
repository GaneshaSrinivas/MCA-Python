from tkinter import *
from tkinter import ttk
import MySQLdb
from tkinter import *
import os
from subprocess import call
import sys
mydb=MySQLdb.connect(host="localhost",user="root",passwd="root",database="mysql")
mycursor=mydb.cursor()
def insert():
    str1=e1.get()
    str2=e2.get()
    str3=e3.get()
    str4=e4.get()
    str5=e5.get()
    str6=e6.get()
    str7=e7.get()
    val=(str1,str2,str3,str4,str5,str6,str7)
    sql= "INSERT INTO student (usn,name,coursename,coursecode,cie1,cie2,see) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted")
def update():
call(["python", "update.py"])
    def displaybyusn():
call(["python", "update.py"])
    def deletebyusn():
