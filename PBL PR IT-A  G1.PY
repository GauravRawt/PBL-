from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector

db =mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "root",
    database = "pbl"
)
mycursor = db.cursor()


################################################################ Getting User Ids  ##########################################33

  
sid=[]
mname=[]
ename=[]
pid=[]

  
#####################  FUNCTIONS Patient  ################################################################

def searchpatientFN():
  def submitsearchP():
    id= gslname.get()
    mycursor.execute("select id from patients")
    p =  mycursor.fetchall()
    db.commit()
    for i in p:
      pid.append(i[0])
    if not(id.isnumeric()): 
      tmsg.showerror("Alert","Use only numbers in ID")
    id = int(id)
    if id not in pid:
      tmsg.showerror("Alert","ID Does not exists")
    query = "select * from patients where id = {}".format(id)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
      names = i[1]
      age = i[2]
      gender = i[3]
      contact = i[4]
      address = i[5]
      address = address.strip()
    psl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Patient Details")
    psl.place(x=5,y=80,width=600,height=240)
    
    pslname = Label(psl,text="Name :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslname.grid(row=0,column=0,sticky=W)
    
    pslid = Label(psl,text="ID :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslid.grid(row=1,column=0,sticky=W)

    pslage = Label(psl,text="Age :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslage.grid(row=2,column=0,sticky=W)

    pslgender = Label(psl,text="Gender :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgender.grid(row=3,column=0,sticky=W)

    pslcontact = Label(psl,text="Contact No :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontact.grid(row=5,column=0,sticky=W)

    psladdress = Label(psl,text="Address :",padx =2,pady =0,font=("comicsansms",12,"bold"))
    psladdress.grid(row=4,column=0,sticky=W)
    
    
    pslnamev = Label(psl,text=names,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslnamev.grid(row=0,column=1,sticky=W)
    
    pslidv = Label(psl,text=id,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslidv.grid(row=1,column=1,sticky=W)

    pslagev = Label(psl,text=age,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslagev.grid(row=2,column=1,sticky=W)

    pslgenderv = Label(psl,text=gender,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgenderv.grid(row=3,column=1,sticky=W)

    pslcontactv = Label(psl,text=contact,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontactv.grid(row=5,column=1,sticky=W)

    psladdressv = Label(psl,text=address,padx =2,pady =6,font=("comicsansms",12,"bold"))
    psladdressv.grid(row=4,column=1)
    
    
    
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Search Patients")
  asl.place(x=0,y=10,width=700,height=320)
  
  aslname = Label(asl,text="Give Patient ID",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)
  gslname = Entry(asl,font=("comicsansms",11),width=55)
  gslname.grid(row=0,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitsearchP)
  submitbuttonAddS.grid(row = 1, column =1)

############################################## STAFF  ###################################################

def addstaffFN():
  def submitAddS():
    
    name = gslname.get()
    id = gslid.get()
    address = gsladdress.get(1.0,END)
    contactno = gslcontact.get()
    gender = click.get()
    age = gslage.get()
    
    mycursor.execute("select id from staff")
    s =  mycursor.fetchall()
    db.commit()
    for i in s:
      sid.append(i[0])  
    if not(id.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In ID")
      
    elif not(age.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In Age")
      
    elif not(contactno.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In Contact")
    
    id = int(id)
    if id in sid:
      tmsg.showerror("Alert","ID already exists")
    
    query = "insert into staff values({},'{}',{},'{}',{},'{}')".format(id,name,age,gender,contactno,address)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been Added")

  
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Add Staff")
  asl.place(x=0,y=10,width=700,height=320)
  
  aslname = Label(asl,text="Name Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)

  aslage = Label(asl,text="Age Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslage.grid(row=2,column=0,sticky=W)

  aslid = Label(asl,text="ID Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=1,column=0,sticky=W)

  aslgender = Label(asl,text="Gender Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslgender.grid(row=3,column=0,sticky=W)

  aslcontact = Label(asl,text="Contact Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslcontact.grid(row=4,column=0,sticky=W)

  asladdress = Label(asl,text="Address Of Staff",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asladdress.grid(row=5,column=0,sticky=W)

  lblpatientaddres = Label(asl,padx =2,pady =6,font=("comicsansms",12,"bold"))
  lblpatientaddres.grid(row=6,column=0,sticky=W)
  
  gslname = Entry(asl,font=("comicsansms",11),width=55)
  gslname.grid(row=0,column=1)

  gslage = Entry(asl,font=("comicsansms",11),width=55)
  gslage.grid(row=2,column=1)

  gslid = Entry(asl,font=("comicsansms",11),width=55)
  gslid.grid(row=1,column=1)

  gslcontact = Entry(asl,font=("comicsansms",11),width=55)
  gslcontact.grid(row=4,column=1)

  gsladdress = Text(asl,font=("comicsansms",11),width=55,height=2,pady=6)
  gsladdress.grid(row=5,column=1)

  click=StringVar()
  clicked.set("Gender")
  gslgender = OptionMenu(asl,click,"Male","Female","Other")
  gslgender.grid(row = 3, column =1 ,sticky=W)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitAddS)
  submitbuttonAddS.grid(row = 7, column =1)
  

def searchstaffFN():  
  def submitsearchS():
    mycursor.execute("select id from staff")
    s =  mycursor.fetchall()
    db.commit()
    for i in s:
      sid.append(i[0])
    id = gslname.get()
    id = int(id)
    if id not in sid:
      tmsg.showerror("Alert","ID Does not exists")
    query = "select * from staff where id = {}".format(id)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
      name = i[1]
      age = i[2]
      gender = i[3]
      contact = i[4]
      address = i[5]
      address = address.strip()
      psl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10),text="Staff Details")
      psl.place(x=5,y=80,width=600,height=240)
    
      pslname = Label(psl,text="Name :",padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslname.grid(row=0,column=0,sticky=W)
    
      pslid = Label(psl,text="ID :",padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslid.grid(row=1,column=0,sticky=W)

      pslage = Label(psl,text="Age :",padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslage.grid(row=2,column=0,sticky=W)

      pslgender = Label(psl,text="Gender :",padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslgender.grid(row=3,column=0,sticky=W)

      pslcontact = Label(psl,text="Contact No :",padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslcontact.grid(row=5,column=0,sticky=W)

      psladdress = Label(psl,text="Address :",padx=2,pady=6,font=("comicsansms",12,"bold"))
      psladdress.grid(row=4,column=0,sticky=W)
    
    
      pslnamev = Label(psl,text=name,padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslnamev.grid(row=0,column=1,sticky=W)
    
      pslidv = Label(psl,text=id,padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslidv.grid(row=1,column=1,sticky=W)

      pslagev = Label(psl,text=age,padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslagev.grid(row=2,column=1,sticky=W)

      pslgenderv = Label(psl,text=gender,padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslgenderv.grid(row=3,column=1,sticky=W)

      pslcontactv = Label(psl,text=contact,padx =2,pady =6,font=("comicsansms",12,"bold"))
      pslcontactv.grid(row=5,column=1,sticky=W)

      psladdressv = Label(psl,text=address,font=("comicsansms",12,"bold"))
      psladdressv.grid(row=4,column=1,sticky=W)
    
    
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Search Staff")
  asl.place(x=0,y=10,width=700,height=320)
  
  aslname = Label(asl,text="Give Staff ID",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)
  gslname = Entry(asl,font=("comicsansms",11),width=65)
  gslname.grid(row=0,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitsearchS)
  submitbuttonAddS.grid(row = 1, column =1)
  
  
def deletestaffFN():
  def submitdeleteS():
    mycursor.execute("select id from staff")
    s =  mycursor.fetchall()
    db.commit()
    for i in s:
      sid.append(i[0])
    id = getid.get()
    if not(id.isnumeric()): 
      tmsg.showerror("Alert","Use only numbers in ID")
    id = int(id)
    if id not in sid:
      tmsg.showerror("Alert","ID Does not exists")
    else:
      query = "delete from staff where id = {}".format(id)
      mycursor.execute(query)
      db.commit()
      if mycursor.rowcount>0:
        tmsg.showinfo("Alert","Data deleted successfully")
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Delete Staff Details")
  asl.place(x=0,y=10,width=700,height=320)
  aslid = Label(asl,text="Type the ID",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitdeleteS)
  submitbuttonAddS.grid(row = 1, column =1)
  

def updatestaffFN():
  def submitUpdateS():
    id = getid.get()
    updated = getuid.get()
    field = click.get()
    mycursor.execute("select id from staff")
    s =  mycursor.fetchall()
    db.commit()
    for i in s:
      sid.append(i[0])
    if not(id.isnumeric()): 
      tmsg.showerror("Alert","Use only numbers in ID")
    id = int(id)
    if id not in sid:
      tmsg.showerror("Alert","ID Does not exists")
    if field == "Contact No":
      query = "update staff set contact = '{}' where id = {}".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Address":
      query = "update staff set address = '{}' where id = {}".format(updated,id)
      mycursor.execute(query)
      db.commit()
    else:
      tmsg.showerror("Alert","Please select data you want to change")
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been updated")
      
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Update Staff Details")
  asl.place(x=0,y=10,width=700,height=320)
  click=StringVar()
  click.set("Choose Option for Search")
  getidus = OptionMenu(asl,click,"Address","Contact No")
  getidus.grid(row = 1, column =1 ,sticky=W)
  
  aslid = Label(asl,text="Type the ID",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  
  aslupd = Label(asl,text="Select the Detail you Want to change",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslupd.grid(row=1,column=0,sticky=W)
  
  asluid = Label(asl,text="Type the updated value",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asluid.grid(row=2,column=0,sticky=W)
  
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  
  getuid = Entry(asl,font=("comicsansms",11),width=45)
  getuid.grid(row=2,column=1)
  
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitUpdateS)
  submitbuttonAddS.grid(row = 4, column =1)
  

#####################################################  Medicine   ############################################

def addmedicineFN():
  def submitAddM():
    name = gslname.get()
    price = gslprice.get()
    date = gsldate.get()
    contactno = gslcontact.get()
    quantity = gslquantity.get()
    address = gsladdress.get(1.0,END)
    mycursor.execute("select name from medicine")
    m =  mycursor.fetchall()
    db.commit()
    for i in m:
      mname.append(i[0].lower())  
    if name in mname:
      tmsg.showerror("Alert","Medicine already exists")
      
    if not(price.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In Price")
    elif not(contactno.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In Contact")
    elif not(quantity.isnumeric()):
      tmsg.showerror("Alert","Use Only numbers In Quantiy")
    
    query = "insert into medicine values('{}','{}','{}',{},'{}',{})".format(name,date,contactno,quantity,address,price)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been added")
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Add Medicine")
  asl.place(x=0,y=10,width=700,height=320)
  
  datel = Label(asl,text="Please enter date in Format YYYY-MM-DD",font=("arial",10),padx= 8,pady = 6)
  datel.grid(row = 6 ,column =0)
    
  aslname = Label(asl,text="Name Of Medicine",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)

  aslprice = Label(asl,text="Price",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslprice.grid(row=1,column=0,sticky=W)

  asldate = Label(asl,text="Expiry Date",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asldate.grid(row=2,column=0,sticky=W)

  aslquantity = Label(asl,text="Quantity Of Medicine",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslquantity.grid(row=3,column=0,sticky=W)

  aslcontact = Label(asl,text="Contact No Of Provider",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslcontact.grid(row=4,column=0,sticky=W)

  asladdress = Label(asl,text="Address Of Provider",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asladdress.grid(row=5,column=0,sticky=W)

  lblpatientaddres = Label(asl,padx =2,pady =6,font=("comicsansms",12,"bold"))
  lblpatientaddres.grid(row=6,column=0,sticky=W)
  
  gslname = Entry(asl,font=("comicsansms",11),width=45)
  gslname.grid(row=0,column=1)

  gslprice = Entry(asl,font=("comicsansms",11),width=45)
  gslprice.grid(row=1,column=1)

  gsldate = Entry(asl,font=("comicsansms",11),width=45)
  gsldate.grid(row=2,column=1)

  gslquantity = Entry(asl,font=("comicsansms",11),width=45)
  gslquantity.grid(row=3,column=1)
  
  gslcontact = Entry(asl,font=("comicsansms",11),width=45)
  gslcontact.grid(row=4,column=1)

  gsladdress = Text(asl,font=("comicsansms",11),width=45,height=2,pady=6)
  gsladdress.grid(row=5,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitAddM)
  submitbuttonAddS.grid(row = 7, column =1)

def searchmedicineFN():
  def submitsearchP():
    mycursor.execute("select name from medicine")
    m =  mycursor.fetchall()
    db.commit()
    for i in m:
      mname.append(i[0].lower()) 
    id = gslname.get()
    if id.lower() not in mname:
      tmsg.showerror("Alert","Medicine Does not exists")
    query = "select * from medicine where name = '{}'".format(id)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
      name = i[0]
      expirydate = i[1]
      contact = i[2]
      quantity = i[3]
      address = i[4]
      address=address.strip()
      price = i[5]
    psl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Medicine Details")
    psl.place(x=5,y=80,width=600,height=240)
    
    pslname = Label(psl,text="Name :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslname.grid(row=0,column=0,sticky=W)
    
    pslid = Label(psl,text="Expiry Date :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslid.grid(row=1,column=0,sticky=W)

    pslage = Label(psl,text="Contact No :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslage.grid(row=2,column=0,sticky=W)

    pslgender = Label(psl,text="Quantiy :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgender.grid(row=3,column=0,sticky=W)

    pslcontact = Label(psl,text="Address :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontact.grid(row=4,column=0,sticky=W)

    psladdress = Label(psl,text="Price :",padx =2,pady =0,font=("comicsansms",12,"bold"))
    psladdress.grid(row=5,column=0,sticky=W)
    
    
    pslnamev = Label(psl,text=name,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslnamev.grid(row=0,column=1,sticky=W)
    
    pslidv = Label(psl,text=expirydate,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslidv.grid(row=1,column=1,sticky=W)

    pslagev = Label(psl,text=contact ,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslagev.grid(row=2,column=1,sticky=W)

    pslgenderv = Label(psl,text=quantity,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgenderv.grid(row=3,column=1,sticky=W)

    pslcontactv = Label(psl,text=address,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontactv.grid(row=4,column=1,sticky=W)

    psladdressv = Label(psl,text=price,padx =2,pady =6,font=("comicsansms",12,"bold"))
    psladdressv.grid(row=5,column=1,sticky=W)
    
    
    
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Search Medicine")
  asl.place(x=0,y=10,width=700,height=320)
  
  aslname = Label(asl,text="Give Medicine Name",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)
  gslname = Entry(asl,font=("comicsansms",11),width=55)
  gslname.grid(row=0,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitsearchP)
  submitbuttonAddS.grid(row = 1, column =1)

def updatemedicineFN():
  def submitUpdateM():
    id = getid.get()
    updated = getuid.get()
    field = click.get()
    mycursor.execute("select name from medicine")
    m =  mycursor.fetchall()
    db.commit()
    for i in m:
      mname.append(i[0].lower()) 
    if id.lower() not in mname:
      tmsg.showerror("Alert","ID Does not exists")
    if field == "Contact No":
      query = "update medicine set contact_no = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Address":
      query = "update medicine set address = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Price":
      query = "update medicine set price = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Quantiy":
      query = "update medicine set quantiy = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    else:
      tmsg.showinfo("Alert","Please select data you want to change")
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been updated")
      
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Update Medicine Details")
  asl.place(x=0,y=10,width=700,height=320)
  click=StringVar()
  click.set("Choose Option for Search")
  getidus = OptionMenu(asl,click,"Address","Contact No","Price","Quantity")
  getidus.grid(row = 1, column =1 ,sticky=W)
  
  aslid = Label(asl,text="Medicine Name",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  
  aslupd = Label(asl,text="Select the Detail you Want to change",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslupd.grid(row=1,column=0,sticky=W)
  
  asluid = Label(asl,text="Type the updated value",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asluid.grid(row=2,column=0,sticky=W)
  
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  
  getuid = Entry(asl,font=("comicsansms",11),width=45)
  getuid.grid(row=2,column=1)
  
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitUpdateM)
  submitbuttonAddS.grid(row = 4, column =1)
  

def deletemedicineFN():
  def submitdeleteM():
    id = getid.get()
    mycursor.execute("select name from medicine")
    m =  mycursor.fetchall()
    db.commit()
    for i in m:
      mname.append(i[0].lower()) 
    if id.lower() not in mname:
      tmsg.showerror("Alert","Medicine Does not exists")
    query = "delete from medicine where name = '{}'".format(id)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Data deleted successfully")
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Delete Medicine ")
  asl.place(x=0,y=10,width=700,height=320)
  aslid = Label(asl,text="Type the ID",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitdeleteM)
  submitbuttonAddS.grid(row = 1, column =1)

#################################################  EQUIPMENNT  ########################################################
def addequipmentFN():
  def submitAddE():
    name = gslname.get()
    price = gslprice.get()
    date = gsldate.get()
    contactno = gslcontact.get()
    quantity = gslquantity.get()
    address = gsladdress.get(1.0,END)
    mycursor.execute("select name from equipment")
    e =  mycursor.fetchall()
    db.commit()
    for i in e:
      ename.append(i[0].lower())
    if name.lower() in ename:
      tmsg.showerror("Alert","Equipment already exists")
    if not(price.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In ID")
    elif not(contactno.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In Contact")
    elif not(quantity.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In Quantity")
    
    query = "insert into equipment values('{}','{}','{}',{},'{}',{})".format(name,date,contactno,quantity,address,price)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been Added")
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Add Equipment")
  asl.place(x=0,y=10,width=700,height=320)
  
  datel = Label(asl,text="Please enter date in Format YYYY-MM-DD",font=("arial",10),padx= 8,pady = 6)
  datel.grid(row = 6 ,column =0)
  
  aslname = Label(asl,text="Name Of Equipment",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)

  aslprice = Label(asl,text="Price Of Equipment",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslprice.grid(row=1,column=0,sticky=W)

  asldate = Label(asl,text="Purchase Date",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asldate.grid(row=2,column=0,sticky=W)

  aslquantity = Label(asl,text="Quantity",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslquantity.grid(row=3,column=0,sticky=W)

  aslcontact = Label(asl,text="Contact No Of Provider",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslcontact.grid(row=4,column=0,sticky=W)

  asladdress = Label(asl,text="Address Of Provider",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asladdress.grid(row=5,column=0,sticky=W)

  lblpatientaddres = Label(asl,padx =2,pady =6,font=("comicsansms",12,"bold"))
  lblpatientaddres.grid(row=6,column=0,sticky=W)
  
  gslname = Entry(asl,font=("comicsansms",11),width=45)
  gslname.grid(row=0,column=1)

  gslprice = Entry(asl,font=("comicsansms",11),width=45)
  gslprice.grid(row=1,column=1)

  gsldate = Entry(asl,font=("comicsansms",11),width=45)
  gsldate.grid(row=2,column=1)

  gslquantity = Entry(asl,font=("comicsansms",11),width=45)
  gslquantity.grid(row=3,column=1)
  
  gslcontact = Entry(asl,font=("comicsansms",11),width=45)
  gslcontact.grid(row=4,column=1)

  gsladdress = Text(asl,font=("comicsansms",11),width=45,height=2,pady=6)
  gsladdress.grid(row=5,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitAddE)
  submitbuttonAddS.grid(row = 7, column =1)

def searchequipmentFN():
  def submitsearchP():
    ename=[]
    mycursor.execute("select name from equipment")
    e =  mycursor.fetchall()
    for i in e:
      ename.append(i[0].lower())
    id = gslname.get()
    if id.lower() not in ename:
      tmsg.showerror("Alert","Equipment Does not exists")
    query = "select * from equipment where name = '{}'".format(id)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
      name = i[0]
      purchasedate = i[1]
      contact = i[2]
      quantity = i[3]
      address = i[4]
      address=address.strip()
      price = i[5]
    psl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Equipment Details")
    psl.place(x=5,y=80,width=600,height=240)
    
    pslname = Label(psl,text="Name :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslname.grid(row=0,column=0,sticky=W)
    
    pslid = Label(psl,text="Purchase Date :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslid.grid(row=1,column=0,sticky=W)

    pslage = Label(psl,text="Contact No :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslage.grid(row=2,column=0,sticky=W)

    pslgender = Label(psl,text="quantiy :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgender.grid(row=3,column=0,sticky=W)

    pslcontact = Label(psl,text="Address :",padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontact.grid(row=4,column=0,sticky=W)

    psladdress = Label(psl,text="Price :",padx =2,pady =0,font=("comicsansms",12,"bold"))
    psladdress.grid(row=5,column=0,sticky=W)
    
    
    pslnamev = Label(psl,text=name,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslnamev.grid(row=0,column=1,sticky=W)
    
    pslidv = Label(psl,text=purchasedate,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslidv.grid(row=1,column=1,sticky=W)

    pslagev = Label(psl,text=contact ,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslagev.grid(row=2,column=1,sticky=W)

    pslgenderv = Label(psl,text=quantity,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslgenderv.grid(row=3,column=1,sticky=W)

    pslcontactv = Label(psl,text=address,padx =2,pady =6,font=("comicsansms",12,"bold"))
    pslcontactv.grid(row=4,column=1,sticky=W)

    psladdressv = Label(psl,text=price,padx =2,pady =6,font=("comicsansms",12,"bold"))
    psladdressv.grid(row=5,column=1,sticky=W)
    
    
    
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Search Equipment")
  asl.place(x=0,y=10,width=700,height=320)
  
  aslname = Label(asl,text="Give Equipment Name",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslname.grid(row=0,column=0,sticky=W)
  gslname = Entry(asl,font=("comicsansms",11),width=55)
  gslname.grid(row=0,column=1)

  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitsearchP)
  submitbuttonAddS.grid(row = 1, column =1)

def updateequipmentFN():
  def submitUpdateE():
    id = getid.get()
    updated = getuid.get()
    field = click.get()
    mycursor.execute("select name from equipment")
    e =  mycursor.fetchall()
    for i in e:
      ename.append(i[0].lower())
    if id.lower() not in ename:
      tmsg.showerror("Alert","Equipment does not exists")
    if field == "Contact No":
      query = "update equipment set contact_no = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Address":
      query = "update equipment set address = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Price":
      query = "update equipment set price = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    elif field == "Quantiy":
      query = "update equipment set quantiy = '{}' where name = '{}'".format(updated,id)
      mycursor.execute(query)
      db.commit()
    else:
      tmsg.showinfo("Alert","Please select data you want to change")
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been updated")
      
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Update Equipment Details")
  asl.place(x=0,y=10,width=700,height=320)
  click=StringVar()
  click.set("Choose Option for Search")
  getidus = OptionMenu(asl,click,"Address","Contact No","Price","Quantity")
  getidus.grid(row = 1, column =1 ,sticky=W)
  
  aslid = Label(asl,text="Equipment Name",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  
  aslupd = Label(asl,text="Select the Detail you Want to change",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslupd.grid(row=1,column=0,sticky=W)
  
  asluid = Label(asl,text="Type the updated value",padx =2,pady =6,font=("comicsansms",12,"bold"))
  asluid.grid(row=2,column=0,sticky=W)
  
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  
  getuid = Entry(asl,font=("comicsansms",11),width=45)
  getuid.grid(row=2,column=1)
  
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitUpdateE)
  submitbuttonAddS.grid(row = 4, column =1)

def deleteequipmentFN():
  def submitdeleteE():
    id = getid.get()
    mycursor.execute("select name from equipment")
    e =  mycursor.fetchall()
    for i in e:
      ename.append(i[0].lower())
    if id.lower() not in ename:
      tmsg.showerror("Alert","Equipment does not exists")
    query = "delete from equipment where name = '{}'".format(id)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Data deleted successfully")
  aswindow = Toplevel()
  aswindow.geometry("700x320")
  asl = LabelFrame(aswindow,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Delete Equipment ")
  asl.place(x=0,y=10,width=700,height=320)
  aslid = Label(asl,text="Type the Name",padx =2,pady =6,font=("comicsansms",12,"bold"))
  aslid.grid(row=0,column=0,sticky=W)
  getid = Entry(asl,font=("comicsansms",11),width=45)
  getid.grid(row=0,column=1)
  submitbuttonAddS = Button(asl,text="SUBMIT",command=submitdeleteE)
  submitbuttonAddS.grid(row = 1, column =1)




root  = Tk()

#MAIN WORKSPACE
root.title("DATABASE MANAGEMENT SYSTEM FOR HOSPITALS")
root.geometry("1540x800")

###################### SUBMIT BUTTON ###########################

def submitAddP():
    name = getpatientname.get()
    id = getpatientid.get()
    address = getpatientaddress.get(1.0,END)
    contactno = getpatientcontact.get()
    gender = clicked.get()
    age = getpatientage.get()
    if id.lower() in pid:
      tmsg.showerror("Alert","ID already exists")
    if not(id.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In ID")
    elif not(age.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In Age")
    elif not(contactno.isnumeric()):
      tmsg.showinfo("Alert","Use Only numbers In Contact")
    
    query = "insert into patients values({},'{}',{},'{}',{},'{}')".format(id,name,age,gender,contactno,address)
    mycursor.execute(query)
    db.commit()
    if mycursor.rowcount>0:
      tmsg.showinfo("Alert","Your Data has been Added")
      
                      
############################  TITLE  ################################
f1 = Frame(root)
f1.pack(side=TOP,fill=X)
l1 = Label(f1,text= "DATABASE MANAGEMENT SYSTEM FOR HOSPITALS",bd=20,fg = "red",font=("comicsansms",30,"bold"), bg="white",relief=RIDGE)
l1.pack(fill=X)

#DATA SPACE
ds = Frame(root,bd=15,relief=RIDGE,bg="white")
ds.place(x=0,y=100,height=380,width=1270)

#DATA SPACE SEPRATIONS
dfl = LabelFrame(ds,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Patient Details")
dfl.place(x=0,y=10,width=700,height=320)

dfr = LabelFrame(ds,bd = 10,relief=RIDGE,font=("comicsansms",10,),text="Other Options")
dfr.place(x= 720,y=10,width=500,height=320)

################################   Extra Frame  ##########################
ef = Frame(root,bd=15,relief=RIDGE,bg="white")
ef.place(x=0,y=455,height=55,width=1270)

##################################   Details  ####################################3
de = Frame(root,bd=15,relief=RIDGE,bg="white")
de.place(x=0,y=520,height=200,width=1270)

################################### DataSpaceLeft  ###################################
lblpatientname = Label(dfl,text="Name Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientname.grid(row=0,column=0,sticky=W)

lblpatientage = Label(dfl,text="Age Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"),justify="left")
lblpatientage.grid(row=2,column=0,sticky=W)

lblpatientid = Label(dfl,text="ID Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientid.grid(row=1,column=0,sticky=W)

lblpatientgender = Label(dfl,text="Gender Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientgender.grid(row=3,column=0,sticky=W)

lblpatientcontact = Label(dfl,text="Contact Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientcontact.grid(row=4,column=0,sticky=W)

lblpatientaddress = Label(dfl,text="Address Of Patient",padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientaddress.grid(row=5,column=0,sticky=W)

lblpatientaddres = Label(dfl,padx =2,pady =6,font=("comicsansms",12,"bold"))
lblpatientaddres.grid(row=6,column=0,sticky=W)


###########################################   Taking Values    ############################333

getpatientname = Entry(dfl,font=("comicsansms",13),width=55)
getpatientname.grid(row=0,column=1)

getpatientage = Entry(dfl,font=("comicsansms",13),width=55)
getpatientage.grid(row=2,column=1)

getpatientid = Entry(dfl,font=("comicsansms",13),width=55)
getpatientid.grid(row=1,column=1)

getpatientcontact = Entry(dfl,font=("comicsansms",13),width=55)
getpatientcontact.grid(row=4,column=1)

getpatientaddress = Text(dfl,font=("comicsansms",13),width=55,height=2,pady=6)
getpatientaddress.grid(row=5,column=1)

clicked=StringVar()
clicked.set("Gender")
getpatientgender = OptionMenu(dfl,clicked,"Male","Female","Other")
getpatientgender.grid(row = 3, column =1 ,sticky=W)

submitbuttonAddP = Button(dfl,text="SUBMIT",command=submitAddP)
submitbuttonAddP.grid(row = 7, column =1)


####################   BUTTONS FRAME  ##################################

searchpatient = Button(ef,text="Search Patients",width=12,command=searchpatientFN)
searchpatient.grid(row=0,column=0)

addstaff = Button(ef,text="Add Staff",width = 10,command=addstaffFN)
addstaff.grid(row=0,column=1)

searchstaff = Button(ef,text="Search Staff",width = 11,command=searchstaffFN)
searchstaff.grid(row=0,column=2)

updatestaff = Button(ef,text="Update Staff",width = 12,command = updatestaffFN)
updatestaff.grid(row=0,column=3)

deletestaff = Button(ef,text="Delete Staff",width = 12,command = deletestaffFN)
deletestaff.grid(row=0,column=4)

addmedicine = Button(ef,text="Add Medicine",width = 12,command = addmedicineFN)
addmedicine.grid(row=0,column=5)

searchmedicine = Button(ef,text="Search Medicine",width = 12,command = searchmedicineFN)
searchmedicine.grid(row=0,column=6)

updatemedicine = Button(ef,text="Update Medicine",width=12,command = updatemedicineFN)
updatemedicine.grid(row=0,column=7)

deletemedicine = Button(ef,text="Delete Medicine",width=12,command = deletemedicineFN)
deletemedicine.grid(row=0,column=8)

addequipment = Button(ef,text="Add Equipment",width=13,command = addequipmentFN)
addequipment.grid(row=0,column=9)

searchequipment = Button(ef,text="Search Equipment",width=14,command = searchequipmentFN)
searchequipment.grid(row=0,column=10)

updateequipment = Button(ef,text="Update Equipment",width=14,command = updateequipmentFN)
updateequipment.grid(row=0,column=11)

deleteequipment = Button(ef,text="Delete Equipment",width=13,command = deleteequipmentFN)
deleteequipment.grid(row=0,column=12)

root.mainloop()
