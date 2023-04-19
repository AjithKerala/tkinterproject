
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="allbase"
)

root=Tk()
root.geometry("1450x800")

def rest():
    mementry.delete(0,tkinter.END)
    refentry.delete(0,tkinter.END)
    title.delete(0,END)
    fnentry.delete(0,END)
    lnentry.delete(0,END)
    adentry.delete(0,END)
    pcentry.delete(0,tkinter.END)
    phno.delete(0,tkinter.END)
    bookidentry.delete(0,END)
    booktitleentry.delete(0,END)
    authorentry.delete(0,END)
    dateofissentry.delete(0,tkinter.END)
    duedatentry.delete(0,END)
    returndate.delete(0,tkinter.END)
    refineentry.delete(0,tkinter.END)
    priceentry.delete(0,tkinter.END)


def DELETE(table):


    dbCursor = database.cursor()
    curItem = table.focus()
    contents = (table.item(curItem))
    selecteditem = contents['values']
    table.delete(curItem)
    delq = "DELETE FROM tkmainproject WHERE ref='%s'" % selecteditem[0]
    dbCursor.execute(delq)
    database.commit()
    database.close()
    mb.showinfo("success", "data deleted successfully")


def exit():
    if mb.askyesno("verify",'Are you Leave'):
        mb.showwarning('Yes',quit())
    else:
        mb.showinfo('No',"Quit has been cancelled")
def addvalue():
    member=mementry.get()
    ref=refentry.get()
    tit=title.get()
    fnam=fnentry.get()
    lnam=lnentry.get()
    addres=adentry.get()
    pcode=pcentry.get()
    ph=phno.get()
    bkid=bookidentry.get()
    bktitle=booktitleentry.get()
    aut=authorentry.get()
    daissu=dateofissentry.get()
    due=duedatentry.get()
    refine=refineentry.get()
    redate=returndate.get()
    pri=priceentry.get()
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="allbase"
    )

    dbCursor = database.cursor()
    sql = "insert into tkmainproject values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(member,ref,tit,fnam,lnam,addres,pcode,bktitle,daissu,due,ph,pri,redate)
    dbCursor.execute(sql,values)
    database.commit()
    database.close()
    tabel.insert("",tkinter.END,text=member,values=(ref,tit,fnam,lnam,addres,pcode,bktitle,daissu,due,ph,pri,redate))



def show(event):
    value=listbox.get(tkinter.ACTIVE)
    if value=="RanddamUzham":

        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0,tkinter.END)
        bookidentry.insert(0,1231)
        authorentry.delete(0,tkinter.END)
        authorentry.insert(0,"Ravipilla")

        import datetime
        e=datetime.datetime.now()
        date=(e.date())
        dateofissentry.delete(0,tkinter.END)
        dateofissentry.insert(0,date)
        duedatentry.delete(0,END)
        duedatentry.insert(0,15)
        refineentry.delete(0,tkinter.END)
        refineentry.insert(0,50)
        returndate.delete(0,tkinter.END)
        returndate.insert(0,"15daysback")
        priceentry.delete(0,END)
        priceentry.insert(0,"100")

    elif value== "Nallukettu":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Rajamowli")


        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "150")
    elif value=="Mayyazhippuzhayude Theeragalill":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Appukuttan")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "200")

    elif value=="Brave New World":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Anandhu")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "300")
    elif value=="The Great Gatsby":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Bharth")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "250")
    elif value== "The Catcher in thr Rye":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Rahul")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "50")
    elif  value=="Great Expectation":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Nandhu")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "250")
    elif value== "The Adventures of Hukleberry Finn":
        booktitleentry.delete(0, tkinter.END)
        booktitleentry.insert(0, value)
        bookidentry.delete(0, tkinter.END)
        bookidentry.insert(0, 246)
        authorentry.delete(0, tkinter.END)
        authorentry.insert(0, "Kannan")

        import datetime
        e = datetime.datetime.now()
        date = (e.date())
        dateofissentry.delete(0, tkinter.END)
        dateofissentry.insert(0, date)
        duedatentry.delete(0, END)
        duedatentry.insert(0, 15)
        refineentry.delete(0, tkinter.END)
        refineentry.insert(0, 50)
        returndate.delete(0, tkinter.END)
        returndate.insert(0, "15daysback")
        priceentry.delete(0, END)
        priceentry.insert(0, "350")






frame1=tkinter.Frame(root,width=100,height=100,borderwidth=15,relief="ridge")
frame1.grid(row=0,column=0)
frame2=tkinter.Frame(frame1,bg="cyan",width=1400,height=60,borderwidth=10)
frame2.grid(row=0,column=0,padx=10)
tet=tkinter.Label(frame2,text="Libary Management System",bg="cyan",fg="red",font=('Helvetica bold',30))
tet.place(x=500,y=0)
frame3=tkinter.Frame(root,width=100,height=100,borderwidth=10,relief="ridge",padx=10,)
frame3.place(x=100,y=100)
frame4=tkinter.LabelFrame(frame3,text="Libary Membership info",width=700,height=400,relief="ridge",borderwidth=10)
frame4.grid(row=0,column=0)
member=tkinter.Label(frame4,text="MemberType",padx=17,pady=5)
member.grid(row=0,column=0)
refel=tkinter.Label(frame4,text="ref",padx=17,pady=2)
refel.grid(row=1,column=0,sticky=W)


Title=tkinter.Label(frame4,text="Title",padx=17,pady=2)
Title.grid(row=2,column=0,sticky=W)

fname=tkinter.Label(frame4,text="FirstName",padx=17,pady=2)
fname.grid(row=3,column=0,sticky=W)
lname=tkinter.Label(frame4,text="LastName",padx=17,pady=2)
lname.grid(row=4,column=0,sticky=W)
Addr=tkinter.Label(frame4,text="Address",padx=17,pady=2)
Addr.grid(row=5,column=0,sticky=W)
pcode=tkinter.Label(frame4,text="PostCode",padx=17,pady=2)
pcode.grid(row=6,column=0,sticky=W)
phno=tkinter.Label(frame4,text="PhoneNo",padx=17,pady=2)
phno.grid(row=7,column=0,sticky=W)
mementry=ttk.Combobox(frame4,values=["Student","Teachers","Workers"],width=30)
mementry.grid(row=0,column=1)
refentry=tkinter.Entry(frame4,width=33)
refentry.grid(row=1,column=1)
title=ttk.Combobox(frame4,values=["Mr","Mrs","Dr"],width=30)
title.grid(row=2,column=1)

fnentry=tkinter.Entry(frame4,width=33)
fnentry.grid(row=3,column=1)
lnentry=tkinter.Entry(frame4,width=33)
lnentry.grid(row=4,column=1)
adentry=tkinter.Entry(frame4,width=33)
adentry.grid(row=5,column=1)
pcentry=tkinter.Entry(frame4,width=33)
pcentry.grid(row=6,column=1)
phno=tkinter.Entry(frame4,width=33)
phno.grid(row=7,column=1)
bookid=tkinter.Label(frame4,text="BookID")
bookid.grid(row=0,column=2,sticky=W,padx=10)
booktitle=tkinter.Label(frame4,text="BookTitle")
booktitle.grid(row=1,column=2,sticky=W,padx=10)
author=tkinter.Label(frame4,text="Author",padx=10)
author.grid(row=2,column=2,sticky=W)
dateofisssued=tkinter.Label(frame4,text="Dateofisssued",padx=10)
dateofisssued.grid(row=3,column=2,sticky=W)
Duedate=tkinter.Label(frame4,text="DueDate",padx=10)
Duedate.grid(row=4,column=2,sticky=W)
Returndate=tkinter.Label(frame4,text="ReturnFine",padx=10)
Returndate.grid(row=5,column=2,sticky=W)
Returnfine=tkinter.Label(frame4,text="ReturnDate",padx=10)
Returnfine.grid(row=6,column=2,sticky=W)
price=tkinter.Label(frame4,text="Price",padx=10)
price.grid(row=7,column=2,sticky=W)

bookidentry=tkinter.Entry(frame4,width=35)
bookidentry.grid(row=0,column=3,padx=10)
booktitleentry=tkinter.Entry(frame4,width=35)
booktitleentry.grid(row=1,column=3,padx=10)
authorentry=tkinter.Entry(frame4,width=35)
authorentry.grid(row=2,column=3,padx=10)
dateofissentry=tkinter.Entry(frame4,width=35)
dateofissentry.grid(row=3,column=3,padx=10)

duedatentry=tkinter.Entry(frame4,width=35)
duedatentry.grid(row=4,column=3,padx=10)
refineentry=tkinter.Entry(frame4,width=35)
refineentry.grid(row=5,column=3,padx=10)
returndate=tkinter.Entry(frame4,width=35)
returndate.grid(row=6,column=3,padx=10)
priceentry=tkinter.Entry(frame4,width=35)
priceentry.grid(row=7,column=3,padx=10)




listbook=["RanddamUzham","Nallukettu","Mayyazhippuzhayude Theeragalill","Brave New World","The Great Gatsby","The Catcher in thr Rye","Great Expectation","The Adventures of Hukleberry Finn"]


#RIGHTSIDE FIRST
rightside=tkinter.LabelFrame(frame3,text="BookDetails",borderwidth=10,relief="ridge",padx=5)
rightside.grid(row=0,column=1)
#LISTBOX
listbox=Listbox(rightside,width=25,height=13)
listbox.bind("<<ListboxSelect>>",show)

listbox.grid(row=0,column=0,padx=10)
listscrollbar=Scrollbar(rightside)
listscrollbar.grid(row=0,column=1,sticky="ns")



#insert value Listbox
for items in listbook:
    listbox.insert(END,items)




tex=tkinter.Text(rightside,width=25,height=10,bg="white")
tex.grid(row=0,column=2)

            ##BUTTONS
btnframe=Frame(root,borderwidth=10,relief="ridge")
btnframe.place(x=150,y=410)
add=Button(btnframe,text="Add Data",width=25,bg="cyan",command=addvalue)
add.grid(row=0,column=0,padx=5)
delt=Button(btnframe,text="Delete",width=25,bg="cyan",command=lambda:DELETE(tabel))
delt.grid(row=0,column=1,padx=5)
'''show=Button(text="Show Data",width=25,bg="cyan")
show.grid(row=0,column=2,padx=5)'''
upd=Button(btnframe,text="Update",width=25,bg="cyan")
upd.grid(row=0,column=3,padx=5)
rest=Button(btnframe,text="Reset",width=25,bg="cyan",command=rest)
rest.grid(row=0,column=4,padx=5)
exit=Button(btnframe,text="Exit",width=25,bg="cyan",command=exit)
exit.grid(row=0,column=5,padx=5)


tableframe=Frame(root,borderwidth=10,relief="ridge")
tableframe.place(x=60,y=500)
tabel=ttk.Treeview(tableframe,columns=("Ref","Title","FirstName","LastName","Address","postcode","Booktitle","DateIssued","DueDate","phonenumber","price","Returndate"))
tabel.heading("#0",text="MemberType")
tabel.heading("Ref",text="Ref")
tabel.heading("Title",text="Title")
tabel.heading("FirstName",text="FirstName")
tabel.heading("LastName",text="LastName")
tabel.heading("Address",text="Address")
tabel.heading("postcode",text="PostCode")
tabel.heading("Booktitle",text="BookTitle")
tabel.heading("DateIssued",text="DateIssued")
tabel.heading("DueDate",text="DueDate")
tabel.heading("phonenumber",text="Mobileno")
tabel.heading("price",text="Price")
tabel.heading("Returndate",text="Return")
tabel.pack(padx=10,pady=10)
tabel.column("#0",width=100)
tabel.column("Ref",width=100)
tabel.column("Title",width=100)
tabel.column("FirstName",width=100)
tabel.column("LastName",width=100)
tabel.column("Address",width=100)
tabel.column("postcode",width=100)
tabel.column("Booktitle",width=100)
tabel.column("DateIssued",width=100)
tabel.column("DueDate",width=100)
tabel.column("phonenumber",width=100)
tabel.column("price",width=100)
tabel.column("Returndate",width=100)


dbCursor = database.cursor()
sq="Select * from tkmainproject"
dbCursor.execute(sq)
result=dbCursor.fetchall()
for i in result:
    a=i[1]
    b=i[2]
    c=i[3]
    d=i[4]
    e=i[5]
    f=i[6]
    g=i[7]
    h=i[8]
    j=i[9]
    k=i[10]
    l=i[11]
    m=i[12]
    tabel.insert("",END,text=i[0],values=(a,b,c,d,e,f,g,h,j,k,l,m))

root.mainloop()