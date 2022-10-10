from tkinter import *
from tkinter import ttk
import mysql.connector as mp
import os
import sys

def iclear():
    Product_ID.set("")
    Quantity.set("")
    Address.set("")
    Payment.set("")
def Buy1():
    Product_ID_info=Product_ID.get()
    Quantity_info=Quantity.get()
    Address_info=Address.get()
    Payment_info=Payment.get()
    if Product_ID_info[0]=="G":
        mycursor.execute("update geometry_stuff set Quantity=Quantity-{} where GID='{}'".format(Quantity_info,Product_ID_info))
    elif Product_ID_info[0]=="B":
        mycursor.execute("update class_book_copy set Quantity=Quantity-{} where BID='{}'".format(Quantity_info,Product_ID_info))
    elif Product_ID_info[0]=="P":
        mycursor.execute("update projects_stuff set Quantity=Quantity-{} where PID='{}'".format(Quantity_info,Product_ID_info))
    elif Product_ID_info[0]=="S":
        mycursor.execute("update sports set Quantity=Quantity-{} where SID='{}'".format(Quantity_info,Product_ID_info))
    else:
        print("Enter the correct ID")
    mycursor.execute("insert into CART values('{}',{},'{}','{}')".format(Product_ID_info, Quantity_info, Address_info, Payment_info))
    conn.commit()
    cart()
def cart():
    global screen5
    global b
    if b==3:
        c=screen3
    elif b==4:
        c=screen4
    c.destroy()
    screen5=Tk()
    screen5.title("Stationary")
    screen5.geometry("1000x562+300+0")
    #==============================Image=====================================

    my_image = PhotoImage(file=newpath+r'\asset\pics\Cart.PNG')
    label1=ttk.Label(screen5, image=my_image)
    label1.pack()
    #==============================Button=====================================
    Product_details=Button(screen5,text="Product Details",bg="blue",width="20", command=main_screen)
    Product_details.place(x=560,y=30)
    Product_requirement=Button(screen5,text="Product Rrequirement",bg="blue",width="20", command=shopping)
    Product_requirement.place(x=720,y=30)
    Logout=Button(screen5,text="Logout",bg="blue",width="10", command=login)
    Logout.place(x=880,y=30)
    
    lis5=['Product ID','Quantity','Address','Payment']
    x=20
    for column in lis5:
        data_cart=Label(screen5,text=column,font=('arial',10))
        data_cart.place(x=x,y=330)
        x=x+70
    mycursor.execute("select* from CART")
    data2=mycursor.fetchall()
    listbox23 = Listbox(screen5, width=15,height=5)
    listbox24 = Listbox(screen5, width=17,height=5)
    listbox25 = Listbox(screen5, width=12,height=5)
    listbox26 = Listbox(screen5, width=10,height=5)
    for a in data2:
        listbox23.insert(END, a[0])
        listbox24.insert(END, a[1])
        listbox25.insert(END, a[2])
        listbox26.insert(END, a[3])
    listbox23.place(x=20, y=350)
    listbox24.place(x=90, y=350)
    listbox25.place(x=160, y=350)
    listbox26.place(x=235, y=350)

    b=5

    
    #==================Error===============================
    Reg.place(x=330,y=150)
    #======================================================


def shopping():
    global screen4
    global b
    if b==3:
        c=screen3
    elif b==5:
        c=screen5
    c.destroy()
    screen4=Tk()
    screen4.title("Stationary")
    screen4.geometry("1280x720+100+0")
    #==============================Image=====================================

    my_image = PhotoImage(file=newpath+r'\asset\pics\product req.PNG')
    label1=ttk.Label(screen4, image=my_image)
    label1.pack()

    #============================Button=======================================

    Product_details=Button(screen4,text="Product Details",bg="blue",width="20", command=main_screen)
    Product_details.place(x=830,y=30)
    Your_orders=Button(screen4,text="Your Orders",bg="blue",width="10", command=cart)
    Your_orders.place(x=1000,y=30)
    Logout=Button(screen4,text="Logout",bg="blue",width="10", command=login)
    Logout.place(x=1100,y=30)
    Buy=Button(screen4,text="Buy",bg="blue",width="10", command=Buy1)
    Buy.place(x=430,y=480)
    Clear=Button(screen4,text="Clear",bg="blue",width="10", command=iclear)
    Clear.place(x=530,y=480)

    global Product_ID
    global Quantity
    global Address
    global Payment
    Product_ID = StringVar()
    Quantity = StringVar()
    Address = StringVar()
    Payment = StringVar()

    Product_ID_Label=Label(screen4, text="Product ID", font=('arial',12,'bold'))
    Product_ID_Label.place(x=430,y=200)
    Quantity_Label=Label(screen4, text="Quantity", font=('arial',12,'bold'))
    Quantity_Label.place(x=430,y=270)
    Address_Label=Label(screen4, text="Address", font=('arial',12,'bold'))
    Address_Label.place(x=430,y=340)
    Payment_Label=Label(screen4, text="Payment", font=('arial',12,'bold'))
    Payment_Label.place(x=430,y=410)


    Product_ID_entry = Entry(screen4, textvariable = Product_ID, font=('arial',12), width= "15")
    Product_ID_entry.place(x=430, y=220)
    Quantity_entry = Entry(screen4, textvariable = Quantity, font=('arial',12), width= "5")
    Quantity_entry.place(x=430, y=295)
    Address_entry = Entry(screen4, textvariable = Address, font=('arial',12), width= "40")
    Address_entry.place(x=430, y=360)
    Payment_entry = Entry(screen4, textvariable = Payment, font=('arial',12), width= "15")
    Payment_entry.place(x=430, y=430)
    

    b=4
    
    #==================Error===============================
    Reg.place(x=330,y=150)
    #======================================================

    

    
def main_screen():
    global screen3
    global b
    if b==1:
        c=screen1
    elif b==4:
        c=screen4
    elif b==5:
        c=screen5
    c.destroy()
    screen3=Tk()
    screen3.title("Stationary")
    screen3.geometry("1201x800+300+0")
    #==============================Image=====================================

    my_image = PhotoImage(file=newpath+r'\asset\pics\product details.PNG')
    label1=ttk.Label(screen3, image=my_image)
    label1.pack()

    #============================Button=======================================

    Product_requirement=Button(screen3,text="Product Rrequirement",bg="blue",width="20", command=shopping)
    Product_requirement.place(x=830,y=30)
    Your_orders=Button(screen3,text="Your Orders",bg="blue",width="10", command=cart)
    Your_orders.place(x=1000,y=30)
    Logout=Button(screen3,text="Logout",bg="blue",width="10", command=login)
    Logout.place(x=1100,y=30)

    #==============================Headings=====================================
    heading1=Label(text="Geometry stuff", font=('arial',15,'bold'))
    heading1.place(x=250, y=170)
    heading2=Label(text="Class Wise Book And Copy", font=('arial',15,'bold'))
    heading2.place(x=650, y=170)
    heading3=Label(text="Sports", font=('arial',15,'bold'))
    heading3.place(x=250, y=500)
    heading4=Label(text="Stuff related to projects", font=('arial',15,'bold'))
    heading4.place(x=650, y=500)
    

    #=================conectivity with mysql for Database1=====================================
    global mycursor
    mycursor.execute("select* from Geometry_stuff")
    data=mycursor.fetchall()
    lis=['GID','ITEM','TYPE','COMPANY','QUANTITY','PRICE']
    x=250
    for u in lis:
        data_Geometry_stuff=Label(screen3,text=u,font=('arial',10))
        data_Geometry_stuff.place(x=x,y=200)
        if lis[1]==u :
            x=x+75
        elif lis[2]==u:
            x=x+40
        elif lis[3]==u or lis[4]==u:
            x=x+70
        else:
            x=x+30

    listbox1 = Listbox(screen3, width=5,height=15)
    listbox2 = Listbox(screen3, width=17,height=15)
    listbox3 = Listbox(screen3, width=12,height=15)
    listbox4 = Listbox(screen3, width=10,height=15)
    listbox5 = Listbox(screen3, width=15,height=15)
    listbox6 = Listbox(screen3, width=5, height=15)
    for i in data:
        listbox1.insert(END, i[0])
        listbox2.insert(END, i[1])
        listbox3.insert(END, i[2])
        listbox4.insert(END, i[3])
        listbox5.insert(END, i[4])
        listbox6.insert(END, i[5])
    listbox1.place(x=250, y=230)
    listbox2.place(x=280, y=230)
    listbox3.place(x=360, y=230)
    listbox4.place(x=405, y=230)
    listbox5.place(x=465, y=230)
    listbox6.place(x=540, y=230)
    
    #=================conectivity with mysql for Database2=====================================
    mycursor.execute("select* from Class_Book_Copy")
    data2=mycursor.fetchall()
    lis2=['BID','ITEM','CLASS','COMPANY','QUANTITY','PRICE']
    x=650
    for v in lis2:
        data_Class_Book_Copy=Label(screen3,text=v,font=('arial',10))
        data_Class_Book_Copy.place(x=x,y=200)
        if lis2[1]==v or lis2[2]==v:
            x=x+60
        elif lis2[3]==v or lis2[4]==v:
            x=x+70
        else:
            x=x+30
    
    listbox7 = Listbox(screen3, width=5,height=15)
    listbox8 = Listbox(screen3, width=17,height=15)
    listbox9 = Listbox(screen3, width=12,height=15)
    listbox10 = Listbox(screen3, width=10,height=15)
    listbox11 = Listbox(screen3, width=15,height=15)
    listbox12 = Listbox(screen3, width=5, height=15)
    for j in data2:
        listbox7.insert(END, j[0])
        listbox8.insert(END, j[1])
        listbox9.insert(END, j[2])
        listbox10.insert(END, j[3])
        listbox11.insert(END, j[4])
        listbox12.insert(END, j[5])
    listbox7.place(x=650, y=230)
    listbox8.place(x=680, y=230)
    listbox9.place(x=740, y=230)
    listbox10.place(x=805, y=230)
    listbox11.place(x=870, y=230)
    listbox12.place(x=940, y=230)

    #=================conectivity with mysql for Database3=====================================
    mycursor.execute("select* from Sports")
    data3=mycursor.fetchall()
    lis3=['SID','ITEM','COMPANY','QUANTITY','PRICE']
    x=250
    for w in lis3:
        data_Sports=Label(screen3,text=w,font=('arial',10))
        data_Sports.place(x=x,y=530)
        if lis[1]==w :
            x=x+75
        elif lis[2]==w:
            x=x+40
        elif lis[3]==w or lis[4]==w:
            x=x+70
        else:
            x=x+30

    listbox13 = Listbox(screen3, width=5,height=10)
    listbox14 = Listbox(screen3, width=17,height=10)
    listbox15 = Listbox(screen3, width=15,height=10)
    listbox16 = Listbox(screen3, width=10,height=10)
    listbox17 = Listbox(screen3, width=15,height=10)
    for k in data3:
        listbox13.insert(END, k[0])
        listbox14.insert(END, k[1])
        listbox15.insert(END, k[2])
        listbox16.insert(END, k[3])
        listbox17.insert(END, k[4])
    listbox13.place(x=250, y=560)
    listbox14.place(x=280, y=560)
    listbox15.place(x=360, y=560)
    listbox16.place(x=425, y=560)
    listbox17.place(x=490, y=560)

    #=================conectivity with mysql for Database4=====================================
    mycursor.execute("select* from Projects_stuff")
    data4=mycursor.fetchall()
    lis4=['PID','ITEM','COMPANY','QUANTITY','PRICE']
    x=650
    for z in lis4:
        data_projects_stuff=Label(screen3,text=z,font=('arial',10))
        data_projects_stuff.place(x=x,y=530)
        if lis[1]==z :
            x=x+75
        elif lis[2]==z:
            x=x+40
        elif lis[3]==z or lis[4]==z:
            x=x+70
        else:
            x=x+30

    listbox18 = Listbox(screen3, width=5,height=10)
    listbox19 = Listbox(screen3, width=17,height=10)
    listbox20 = Listbox(screen3, width=15,height=10)
    listbox21 = Listbox(screen3, width=10,height=10)
    listbox22 = Listbox(screen3, width=15,height=10)
    for l in data4:
        listbox18.insert(END, l[0])
        listbox19.insert(END, l[1])
        listbox20.insert(END, l[2])
        listbox21.insert(END, l[3])
        listbox22.insert(END, l[4])
    listbox18.place(x=650, y=560)
    listbox19.place(x=680, y=560)
    listbox20.place(x=760, y=560)
    listbox21.place(x=825, y=560)
    listbox22.place(x=890, y=560)

    b=3
    
    #==================Error===============================
    Reg.place(x=330,y=150)
    #======================================================
def confirming():
    user=[]
    passs=[]
    Username1_info=Username1.get()
    Password1_info=Password1.get()
    mycursor.execute("select Username from info")
    data1=mycursor.fetchall()
    mycursor.execute("select Password from info")
    data2=mycursor.fetchall()
    for i in data1:
        i=list(i)
        user=user+i
    for j in data2:
        j=list(j)
        passs=passs+j
    
    if Username1_info in user:
        if Password1_info in passs:
            main_screen()
        else:
            screen2=Tk()
            screen2.title("Stationary")
            screen2.geometry("200x60+230+230")
            message=Label(screen2, text="You typed incorrect Password")
            message.place(x=0,y=0)
            OK=Button(screen2, text="OK", bg="blue",width="10", command=screen2.destroy)
            OK.place(x=0,y=30)
            Cancel=Button(screen2, text="Cancel", bg="blue",width="10", command=screen2.destroy)
            Cancel.place(x=80,y=30)

    else:
        screen2=Tk()
        screen2.title("Stationary")
        screen2.geometry("200x60+230+230")
        message=Label(screen2, text="You typed incorrect Username")
        message.place(x=0,y=0)
        OK=Button(screen2, text="OK", bg="blue",width="10", command=screen2.destroy)
        OK.place(x=0,y=30)
        Cancel=Button(screen2, text="Cancel", bg="blue",width="10", command=screen2.destroy)
        Cancel.place(x=80,y=30)
        
def login():
    global screen1
    global b
    if b==0:
        c=screen
    elif b==3:
        c=screen3
    elif b==4:
        c=screen4
    elif b==5:
        c=screen5
    c.destroy()
    screen1=Tk()
    screen1.title("Stationary")
    screen1.geometry("590x350+200+100")
    #==============================Image=====================================

    my_image = PhotoImage(file=newpath+r'\asset\pics\BG2.PNG')
    label1=ttk.Label(screen1, image=my_image)
    label1.pack()
    

    #==========================================================================
    global Username1
    global Password1
    Username1 = StringVar()
    Password1 = StringVar()

    Log=Label(screen1, text="Login", font=('arial',12,'bold'))
    Log.place(x=230,y=100)
    Username_Label=Label(screen1, text="Username")
    Username_Label.place(x=230,y=130)
    Username_entry = Entry(screen1, textvariable = Username1, font=('arial',12), width= "15")
    Username_entry.place(x=230, y=150)

    Password_Label=Label(screen1, text="Password")
    Password_Label.place(x=230,y=180)
    Password_entry = Entry(screen1, textvariable = Password1, font=('arial',12), width= "15")
    Password_entry.place(x=230, y=200)
    
    Login=Button(screen1,text="Login",bg="blue",width="10", command=confirming)
    Login.place(x=230,y=230)

    b=1
    
    #==================Error===============================
    Reg.place(x=330,y=150)
    #======================================================
def iregister():
    global Username_info
    global Password_info
    Username_info=Username.get()
    Password_info=Password.get()
    mycursor.execute("insert into info values('{}','{}')".format(Username_info,Password_info))
    conn.commit()
    login()

def iReset():
    Name.set("")
    Email.set("")
    Phone_Number.set("")
    Username.set("")
    Password.set("")
    
passs = input("Enter the password of mysql:")
newpath = os.getcwd()

sys.path.append(newpath+r'\asset\details')
import Database

try:
    Database.content(passs)
except:
    pass


conn =mp.connect(host='localhost',user='root',password=passs,database="stationary") 
mycursor=conn.cursor()
global b
screen=Tk()
screen.title("Stationary")
screen.geometry("1067x710+100+50")

#==============================Image=====================================

my_image = PhotoImage(file=newpath+r'\asset\pics\BG.PNG')
label=ttk.Label(screen, image=my_image)
label.pack()


#==========================================================================
Reg=Label(text="Registration", font=('arial',12,'bold'))
Reg.place(x=330,y=150)

Name = StringVar()
Email = StringVar()
Phone_Number = StringVar()
Username = StringVar()
Password = StringVar()

Name_Label=Label(text="Name")
Name_Label.place(x=330,y=190)
Email_Label=Label(text="Email")
Email_Label.place(x=330,y=240)
Phone_Number_Label=Label(text="Phone_Number")
Phone_Number_Label.place(x=330,y=290)
Username_Label=Label(text="Username")
Username_Label.place(x=330,y=340)
Password_Label=Label(text="Password")
Password_Label.place(x=330,y=390)

Name_entry = Entry(textvariable = Name, font=('arial',12), width= "30")
Name_entry.place(x=330, y=210)
Email_entry = Entry(textvariable = Email, font=('arial',12), width= "30")
Email_entry.place(x=330, y=260)
Phone_Number_entry = Entry(textvariable = Phone_Number, font=('arial',12), width= "30")
Phone_Number_entry.place(x=330, y=310)
Username_entry = Entry(textvariable = Username, font=('arial',12), width= "30")
Username_entry.place(x=330, y=360)
Password_entry = Entry(textvariable = Password, font=('arial',12), width= "30")
Password_entry.place(x=330, y=410)

Register=Button(screen,text="Register",bg="blue",width="10", command=iregister)
Register.place(x=330,y=440)
Reset=Button(screen,text="Reset",bg="blue",width="10", command=iReset)
Reset.place(x=430,y=440)
login1=Button(screen,text="Login",bg="blue",width="10", command=login)
login1.place(x=530,y=440)

b=0
