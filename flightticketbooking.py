import datetime
import random
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    database="ticketbooking",
    user="root",
    password="12345"
)

def select_to(route,start):
    a=0
    for i in route:
        a=a+1
        print(a,i)
    try:
        to=int(input("SELECT DESTINATION:"))
        if to==1:
            dest=route[0]
            ticketfare=3500
            print(f"starting:{start} destination:{dest}")
            print(f"ticketfare={ticketfare}")
            booking(route,start,ticketfare)
        elif to==2:
            dest=route[2]
            ticketfare=3500
            print(f"starting:{start} destination:{dest}")
            print(f"ticketfare={ticketfare}")
            booking(route,start,ticketfare)
        elif to==3:
            dest=route[2]
            ticketfare=3500
            print(f"starting:{start} destination:{dest}")
            print(f"ticketfare={ticketfare}")
            booking(route,start,ticketfare)
        elif to==4:
            dest=route[3]
            ticketfare=3500
            print(f"starting:{start} destination:{dest}")
            print(f"ticketfare={ticketfare}")
            booking(route,start,ticketfare)
        elif to==5:
            dest=route[4]
            ticketfare=3500
            print(f"starting:{start} destination:{dest}")
            print(f"ticketfare={ticketfare}")
            booking(start,dest,ticketfare)
        else:
            print("select only from option")
    except:
        print("select only by option(1-5)")
        select_to(route,start)

def booking(start,dest,ticketfare):
    no=int(input("how many passengers:"))
    i=0
    while i<no:
        i=i+1
        name=str(input("Enter passenger name:"))
        age=int(input("Enter the age :"))
        date=(input("Enter date of travel(YYYYMMdd):"))
        seatno=seat()
        confirmation=int(input("confrim the ticket(1.Yes (or) 2.No):"))
        if confirmation==1:
            mycursor=mydb.cursor()
            sq="INSERT INTO passengerslist( name, age, from, to, dateoftravel, paid,seatno) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(name,age,start,dest,date,ticketfare,seatno)
            mycursor.execute(sq,val)
            mydb.commit()

def seat():
    print("select seat no between 1-100")
    seatno=int(input("Select the seat:"))
    mycursor=mydb.cursor()
    mycursor.execute(""" SELECT * FROM passengerslist where seatno ='%s'"""%(seatno))
    row=mycursor.fetchone()
    if mycursor.rowcount==1:
        print("seat was already booked\nplease select another seat")
        seat()
    else:
        print("seat was selected ")
    return seatno


available_seats=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
seats_booked=[]  
route=["chennai","madurai","tuticorin","thiruchirapalli","coimbatare","pondicherry"]

while 1:
    print("***WELCOME TO SUNDRA TRAVELS***")
    print("1.chennai  4.tiruchirapalli  ")
    print("2.madurai  5.coimbatare")
    print("3.tuticorin  6.pondicherry")

    try:
        frm=int(input("SELECT STARTING POINT:"))
        if frm==1:
            start=route[0]
            route.remove(start)
            select_to(route,start)
            break
        elif frm==2:
            start=route[1]
            route.remove(start)
            select_to(route,start)
            break
        elif frm==3:
            start=route[2]
            route.remove(start)
            select_to(route,start)
            break
        elif frm==4:
            start=route[3]
            route.remove(start)
            select_to(route,start)
            break
        elif frm==5:
            start=route[4]
            route.remove(start)
            select_to(route,start)
            break
        elif frm==6:
            start=route[5]
            route.remove(start)
            select_to(route,start)
            break
        else:
                print("select only from the option")
    except:
        print("select only the options(1-12)")

    