import os
import tempfile
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


tk = Tk()
tk.geometry("500x300")
tk.title ("RETAIL BILLING SYSTEM")
tk['bg'] ="white"



Label(tk,text="RETAIL BILLING SYSTEM",font="arial 30 bold",fg="yellow",bg="black",height=2 ).pack(fill="x")


frame1=LabelFrame(tk,text="CUATOMER DETAIL",fg="red",bg="white",font="arial 15 bold",height=75,width=1900).place(x=2,y=100)
Label(frame1,text="NAME:",bg="white",fg="black",font="arial 15 bold").place(x=8,y=130)
Entry(frame1,bg="white",bd=4,font="arial 10 bold").place(x=90,y=130)
Label(frame1,text="PHONE NO:",bg="white",fg="black",font="arial 15 bold").place(x=300,y=130)
Entry(frame1,bg="white",bd=4,font="arial 10 bold").place(x=425,y=130)
Label(frame1,text="BILL NO:",bg="white",fg="black",font="arial 15 bold").place(x=650,y=130)
Entry(frame1,bg="white",bd=4,font="arial 10 bold").place(x= 750,y=130)

Button(frame1,text="Search",fg="black",bg="light blue",bd=4,font="arial 15 bold").place(x=1000,y=120)

frame2=LabelFrame(tk,text="COSMETICS",fg="red",bg="white",font="arial 15 bold",height=280,width=280).place(x=2,y=180)
Label(frame2,text="BATH SOPE:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=210)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=210)
Label(frame2,text="FACE CREAM:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=250)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=250)
Label(frame2,text="FASH WASH:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=290)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=290)
Label(frame2,text="HAIR SPRAY:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=330)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=330)
Label(frame2,text="HAIR GEL:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=370)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=370)
Label(frame2,text="BODY LOTION:",bg="white",fg="black",font="arial 10 bold").place(x=8,y=410)
Entry(frame2,bg="white",bd=4,font="arial 10 bold").place(x=110,y=410)


frame3=LabelFrame(tk,text="GRECERY",fg="red",bg="white",font="arial 15 bold",height=280,width=250).place(x=290,y=180)
Label(frame3,text="RICE:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=210)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=210)
Label(frame3,text="OIL:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=250)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=250)
Label(frame3,text="DAAL:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=290)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=290)
Label(frame3,text="WHEAT:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=330)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=330)
Label(frame3,text="SUGAR:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=370)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=370)
Label(frame3,text="TEA:",bg="white",fg="black",font="arial 10 bold").place(x=300,y=410)
Entry(frame3,bg="white",bd=4,font="arial 10 bold").place(x=360,y=410)


frame4=LabelFrame(tk,text="COLD DRINK",fg="red",bg="white",font="arial 15 bold",height=280,width=260).place(x=548,y=180)
Label(frame4,text="MAZA:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=210)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=210)
Label(frame4,text="PEPSI:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=250)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=250)
Label(frame4,text="SPRITE:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=290)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=290)
Label(frame4,text="DEEW:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=330)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=330)
Label(frame4,text="FROOTI:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=370)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=370)
Label(frame4,text="STING:",bg="white",fg="black",font="arial 10 bold").place(x=560,y=410)
Entry(frame4,bg="white",bd=4,font="arial 10 bold").place(x=630,y=410)

frame5=LabelFrame(tk,text="BILL RECORD",fg="red",bg="white",font="arial 15 bold",height=170,width=1900).place(x=8,y=470)
Label(frame5,text="COSMETIC PRICE:",bg="white",fg="black",font="arial 10 bold").place(x=10,y=500)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=150,y=500)
Label(frame5,text="GLOCARY PRICE:",bg="white",fg="black",font="arial 10 bold").place(x=10,y=550)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=150,y=550)
Label(frame5,text="COLD DRINK PRICE:",bg="white",fg="black",font="arial 10 bold").place(x=10,y=600)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=150,y=600)

Label(frame5,text="COSMETIC TAX:",bg="white",fg="black",font="arial 10 bold").place(x=320,y=500)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=450,y=500)
Label(frame5,text="GLOCARY TAX:",bg="white",fg="black",font="arial 10 bold").place(x=320,y=550)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=450,y=550)
Label(frame5,text="COLD DRINK TAX:",bg="white",fg="black",font="arial 10 bold").place(x=320,y=600)
Entry(frame5,bg="white",bd=4,font="arial 10 bold").place(x=450,y=600)

Label(frame5,text="TOTAL BILL:",bg="white",fg="black",font="arial 20 bold").place(x=650,y=500)
Entry(frame5,bg="white",bd=4,width=15,font="arial 15 bold").place(x=650,y=550)

frame5=LabelFrame(tk,fg="red",bg="white",font="arial 15 bold",height=110,width=420).place(x=850,y=500)

Button(frame1,text="TOTAL",fg="black",bg="light blue",bd=4,font="arial 15 bold").place(x=870,y=530)
Button(frame1,text="BILL",fg="black",bg="light blue",bd=4,font="arial 15 bold").place(x=970,y=530)
Button(frame1,text="EMAIL",fg="black",bg="light blue",bd=4,font="arial 15 bold").place(x=1050,y=530)
Button(frame1,text="PRINT",fg="black",bg="light blue",bd=4,font="arial 15 bold").place(x=1150,y=530)


tk.mainloop()