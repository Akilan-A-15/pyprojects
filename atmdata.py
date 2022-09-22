import datetime
import random
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    database="dataforatm",
    user="root",
    password="12345"
)

def process(t):
    try:
        n=int(input("1.Deposit, 2.Withdraw, 3.balance check\n"))
        if (n==1):
            deposit(t)
        elif(n==2):
            withdraw(t)
        elif(n==3):
            print("Your balance amount is:",t)
        else:
            print("choose only from the option")
            process(t)
    except(ValueError):
        print("please choose only option by 1 or 2 or 3 ")
        process(t)

def deposit(t):
    try:
        d=int(input("Enter the amount to deposit:"))
        t=t+d
        print("your amount has been deposited")
        print("your account balance is :",t)
        mycursor.execute("""UPDATE atmusers SET balance = '%s' WHERE user = '%s'"""%(t,usid))
        mydb.commit()
        isrecipt(t)
    except(ValueError):
        print("please enter the amount in only numerical value")
        deposit(t)

def withdraw(t):
    try:
        w=int(input("Enter the amount:"))
        if (w<=t):
            t=t-w
            print(t)
            mycursor.execute("""UPDATE atmusers SET balance = '%s' WHERE user = '%s'"""%(t,usid))
            mydb.commit()
            isrecipt(t)
        else:
            print("Sorry, there is no sufficient amount in your account")
    except(ValueError):
        print("please enter the amount in only numerical value")
        withdraw(t)

def isrecipt(t):
    try:
        recipt=int(input("Do you want recipt? \n1.yes\n2.no\n "))
        if recipt==1:
            print("____________________________")
            print("----------------------------")
            print("***Mariyamman ATM***")
            print("****dubai branch****")
            print("name:",usid)
            print("balance amount=",t)
            print(datetime.datetime.now())
            print("******THANK YOU*****")
            print("____________________________")
            print("----------------------------")
            
        elif recipt==2:
            print("***THANK YOU***")
    except(ValueError):
        print("please choose only option by 1 or 2")
        isrecipt(t)

def pingen():
    try:
        type=int(input("please select the type: 1.manualy 2.automatic\n"))
        if type==1:
                newpin=int(input("enter your new pin"))
                print("your pin has been changed to",newpin)
                mycursor=mydb.cursor()
                sq="INSERT INTO atmusers(user,balance,pins,phone number,dateofbirth) values(%s,%s,%s,%s,%s)"
                val=(usid,bal,newpin,phno,dob)
                mycursor.execute(sq,val)
                mydb.commit()

        elif(type==2):
                newpin=random.randint(1000,9999)
                print("your new pin is:",newpin)
                mycursor=mydb.cursor()
                sq="INSERT to atmusers(user,balance,pins,phone number,dateofbirth) values(%s,%s,%s,%s,%s)"
                val=(usid,bal,newpin,phno,dob)
                mycursor.execute(sq,val)
                mydb.commit()
        else:
            print("choose only from the option")
            pingen()
    except(ValueError):
        print("please choose only option by 1 or 2")
        pingen()


print("**Welcome to Mariyamman ATM**")
try:
    pr=int(input("1.create account 2.login account "))
    if pr==2:
        usid=str(input("Enter username:"))
        mycursor=mydb.cursor()
        mycursor.execute(""" SELECT * FROM atmusers where user='%s'"""%(usid))
        row=mycursor.fetchone()
        id=row[0]
        if mycursor.rowcount==1:
            count=0
            chance=3
            while count<3:
                ps=int(input("Enter password:"))
                if ps in row:
                    t=row[2]
                    process(t)
                    break
                else:
                    chance=chance-1
                    print(f"wrong pin you have only {chance} chances")
                    count=count+1
                if count==3:
                    print("your account has been locked")
        else:
            print("INVALID DATA")
    elif pr==1:
        usid=str(input("Create username:"))
        dob=str(input("enter your dob(yyyymmdd):"))
        phno=int(input("enter your phone number:"))
        bal=int(input("enter the amount to deposite:"))
        pingen()
except(ValueError):
        print("please choose only option by 1 or 2")