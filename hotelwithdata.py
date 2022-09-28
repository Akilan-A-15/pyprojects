import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    database="hotel",
    user="root",
    password="12345"
)

print("************************WELCOME************************")
print("*******************HOTEL VELACHERY*******************")
print("Ellaaaru vaaanga..... Always welcomes you....! Inaiku oru pudi...")
tiffen_menu=["idly","dosa","pongal","poori"]
lunch_menu=["biriyani","full meals","fried rice"]
dinner_menu=["dosa","idly","chapathi","parota","noodles","fried rice"]
juice_menu=["lemon","apple","pomogranate","badham"]
idly=dosa=poori=chapathi=parota=lemon=5
pongal=apple=pomogranate=badham=10
biriyani=fullmeals=friedrice=noodles=50

def askingforjuice(amount):
    ju=str(input("do you want juice?:yes(or)no\n\n"))
    if ju=="yes":
        amount=juice(amount)
    elif(ju=="no"):
        print(f"\n your total bill is Rs. {amount}\n {timenow}")
    else:
        print("select only yes(or)no")
        askingforjuice(amount)
    return amount

def extrajuice(amount):
    ask=str(input("Do you want any another juice:yes(or)no\n\n"))
    if ask=="yes":
        amount=juice(amount)
    elif ask=="no":
        print(f"\n your total bill is Rs. {amount}\n {timenow}")
    else:
        print("select only yes(or)no")
        extrajuice(amount)
    return amount
def morextradish(amount):
    ask=str(input("Do you want any another dish:yes(or)no\n"))
    if (ask=="yes"):
        amount=mrng(amount)
    elif ask=="no":
        print(f"\n your total bill is Rs. {amount}\n {timenow}")
    else:
        print("select only yes(or)no")
        morextradish(amount)
    return amount
def aftextradish(amount):
    ask=str(input("Do you want any another dish:yes(or)no\n"))
    if (ask=="yes"):
        amount=aftnon(amount)
    elif ask=="no":
        amount=askingforjuice(amount)
    else:
        print("select only yes(or)no")
        aftextradish(amount)
    return amount

def nitextradish(amount):
    ask=str(input("Do you want any another dish:yes(or)no\n"))
    if ask=="yes":
        amount=night(amount)
    elif ask=="no":
        amount=askingforjuice(amount)
    else:
            print("select only yes(or)no")
            nitextradish(amount)
    return amount

def juice(amount):
    j=str(input(f"select the juice:{juice_menu}\n")).lower()
    if j=="lemon":
        no=int(input("how many :"))
        amount=amount+(lemon*no)
        amount=extrajuice(amount)
            
    elif j=="apple":
        no=int(input("how many :"))
        amount=amount+(apple*no)
        amount=extrajuice(amount)

    elif j=="pomagranate":
        no=int(input("how many :"))
        amount=amount+(pomogranate*no)
        amount=extrajuice(amount)

    elif j=="badham":
        no=int(input("how many :"))
        amount=amount+(badham*no)
        ask=str(input("Do you want any another juice:yes(or)no\n"))
        amount=extrajuice(amount)
    else:
        print("slect only form the menu")
        juice(amount)
    return amount

def mrng(amount):
    print(f"select your oder:{tiffen_menu}")
    oder=input("").lower()
    oder=oder.replace(" ","")
    if (oder=="idly"):
        no=int(input("how much do you want:"))
        amount=amount+(idly*no)
        amount=morextradish(amount)

    elif (oder=="dosa"):
        no=int(input("how much do you want:"))
        amount=amount+(dosa*no)
        amount=morextradish(amount)

    elif (oder=="poori"):
        no=int(input("how much do you want:"))
        amount=amount+(poori*no)
        amount=morextradish(amount)

    elif (oder=="chapathi"):
        no=int(input("how much do you want:"))
        amount=amount+(chapathi*no)
        amount=morextradish(amount)

    elif (oder=="pongal"):
        no=int(input("how much do you want:"))
        amount=amount+(pongal*no)
        amount=morextradish(amount)
    else:
        print("Select only form menu")
        mrng(amount)
    return amount

def aftnon(amount):
    print(f"select your oder:{lunch_menu}")
    oder=input("USER:").lower()
    oder=oder.replace(" ","")
    if (oder=="biriyani"):
        no=int(input("how much do you want:"))
        amount=amount+(biriyani*no)
        amount=aftextradish(amount)


    elif (oder=="fullmeals"):
        no=int(input("how much do you want:"))
        amount=amount+(fullmeals*no)
        amount=aftextradish(amount)
        
    elif (oder=="friedrice"):
        no=int(input("how much do you want:"))
        amount=amount+(friedrice*no)
        amount=aftextradish(amount)
    else:
        print("Select only form menu")
        aftnon(amount)
    return amount
        
def night(amount):
    print(f"select your oder:{dinner_menu}")
    oder=input("").lower()
    oder=oder.replace(" ","")
    if (oder=="idly"):
        no=int(input("how much do you want:"))
        amount=amount+(idly*no)
        amount=nitextradish(amount)
        
    elif (oder=="dosa"):
        no=int(input("how much do you want:"))
        amount=amount+(dosa*no)
        amount=nitextradish(amount)
        
    elif (oder=="noodles"):
        no=int(input("how much do you want:"))
        amount=amount+(noodles*no)
        amount=nitextradish(amount)
        
    elif (oder=="chapathi"):
        no=int(input("how much do you want:"))
        amount=amount+(chapathi*no)
        amount=nitextradish(amount)
        
    elif (oder=="parota"):
        no=int(input("how much do you want:"))
        amount=amount+(parota*no)
        amount=nitextradish(amount)
        
    elif (oder=="friedrice"):
        no=int(input("how much do you want:"))
        amount=amount+(friedrice*no)
        amount=nitextradish(amount)

    else:
        print("Select only form menu")
        night(amount)
    return amount

timenow=datetime.datetime.now()
oder_time=int(datetime.datetime.now().hour)
if (oder_time>=7 and oder_time<=11):
    total=mrng(0)
elif(oder_time>=12 and oder_time<=16):
    total=aftnon(0)
elif(oder_time>=18 and oder_time<=23):
    total=night(0)


name=input("Enter your name:")
phonenumber=int(input("Enter your phone number:"))
feedback=input("please share your feedback:")
bill=total
mycursor=mydb.cursor()
sq="INSERT INTO customerdata(name, phonenumber, feedback, bill, datetime) values(%s,%s,%s,%s,%s)"
val=(name,phonenumber,feedback,bill,timenow)
mycursor.execute(sq,val)
mydb.commit()
print("****************THANK YOU FOR COMMING****************")
print("*******************VISIT AGAIN*******************")
