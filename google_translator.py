from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from googletrans import LANGUAGES, Translator

def cange(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 =dest
    trans = Translator()
    trans_1 = trans.translate(text,src=src1,dest=dest1)
    return trans_1.text

def data():
    s = comb_sor.get()
    d = comb_sor1.get()
    msg = sor_text.get(1.0,END)
    textget = cange(text=msg,src=s,dest=d)
    sor_text1.delete(1.0,END)
    sor_text1.get(END,textget)

a = Tk()
a.title("TRANSLATOR")
a.geometry("500x800")
a.config(bg="Purple")

lb = Label(a,text="TRANSLATOR",font=("Times New Roman",40,"bold"),bg="Purple")
lb.place(x=60,y=40,height=50,width=400)

frame = Frame(a).pack(side=BOTTOM)

lb = Label(a,text="SOURCE TEXT",font=("Times New Roman",20,"bold"),fg="Black",bg="Purple")
lb.place(x=60,y=120,height=20,width=400)

sor_text = Text(frame,font=("Times New Roman",40,"bold"),wrap=WORD)
sor_text.place(x=10,y=150,height=200,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=380,height=80,width=140)
comb_sor.set("English")

button_change = Button(frame,text="Translator",relief=RAISED,bg="Orange",font=("Times New Roman",20,"bold"),command=data)
button_change.place(x=180,y=380,height=80,width=150)

comb_sor1 = ttk.Combobox(frame,value=list_text)
comb_sor1.place(x=350,y=380,height=80,width=140)
comb_sor1.set("English")

lb = Label(a,text="RESULT TEXT",font=("Times New Roman",20,"bold"),fg="Black",bg="Purple")
lb.place(x=60,y=470,height=20,width=400)

sor_text1 = Text(frame,font=("Times New Roman",40,"bold"),wrap=WORD)
sor_text1.place(x=10,y=500,height=200,width=480)
a.mainloop()
