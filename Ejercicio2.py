from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("700x600")
raiz.configure(background="gray40")

#Frame base titulo

mainframe = ttk.Frame(raiz,background="gray2")
mainframe.grid(column=0,row=1,sticky=(W,N))

mainframe2 = ttk.Frame(mainframe,background="#482525")
mainframe2.grid(column=0,row=0,padx=50,pady=10,)

mainframe3 = ttk.Frame(mainframe2,background="#482525")
mainframe3.grid(column=0,row=0,padx=20,pady=15)

mainframeTabla = ttk.Frame(mainframe3,width=20,height=20)
mainframeTabla.grid(column=0,row=6,columnspan=5,pady=30)

#Titulo

ttk.Label(raiz,text="Product management",font=("verdana",30,"bold"),foreground="white",background="gray40").grid(column=0,row=0,padx=80,sticky=(W))

imagen = PhotoImage(file="carrito2.png")
imagenC = ttk.Label(raiz,background="gray40")
imagenC.grid(column=0,row=0,sticky=(W))
imagenC['image'] = imagen

#Declaraciones

id = int()
name = StringVar()
description= StringVar()
quantity = int ()
price =int ()

#Texto

ttk.Label(mainframe3,text="Id product:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=0,sticky=(W,N),pady=15)
ttk.Label(mainframe3,text="Name:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=1,sticky=(W,N))
ttk.Label(mainframe3,text="Description:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=2,sticky=(W,N),pady=8)
ttk.Label(mainframe3,text="Quantity:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=3,sticky=(W,N))
ttk.Label(mainframe3,text="Price:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=4,sticky=(W,N))

#Rayas enmedio
IdEntry = ttk.Entry(mainframe3,width=30,textvariable=id,background="#482525")
IdEntry.grid(column=1,row=0)
nameEntry = ttk.Entry(mainframe3,width=30,textvariable=id,background="#482525")
nameEntry.grid(column=1,row=1)
descriptionEntry = ttk.Entry(mainframe3,width=30,textvariable=id,background="#482525")
descriptionEntry.grid(column=1,row=2)
quantityEntry = ttk.Entry(mainframe3,width=30,textvariable=id,background="#482525")
quantityEntry.grid(column=1,row=3)
priceEntry = ttk.Entry(mainframe3,width=30,textvariable=id,background="#482525")
priceEntry.grid(column=1,row=4)

#Imagenes y back
imagen1 = PhotoImage(file="Limpiar.png")
imagenl = ttk.Button(mainframe3,background="#482525",pady=6,relief="flat")
imagenl.grid(column=3,row=0)
imagenl['image'] = imagen1

imagen2 = PhotoImage(file="Lupa.png")
imagenp = ttk.Button(mainframe3,background="#482525",relief="flat")
imagenp.grid(column=3,row=0,sticky=(W),padx=40,pady=6)
imagenp['image'] = imagen2

ttk.Button(mainframe3,text="Back",font=("verdana",13,"bold"),foreground="purple1",background="#482525",relief="flat").grid(column=3,row=0,sticky=(E),padx=30)

# Botones colores 

ttk.Button(mainframe3,text="Save",font=("verdana",13,"bold"),fg="white",background="green4",width=15,height=1).grid(column=3,row=1,padx=30)
ttk.Button(mainframe3,text="Delete",font=("verdana",13,"bold"),fg="white",background="red2",width=15,height=1).grid(column=3,row=2,padx=30,pady=8)
ttk.Button(mainframe3,text="Update",font=("verdana",13,"bold"),fg="white",background="DarkOrange2",width=15,height=1).grid(column=3,row=3,padx=30)

# Crear encabezado de la tabla
ttk.Label(mainframeTabla, text="idproduit", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(mainframeTabla, text="namep", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(mainframeTabla, text="description", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(mainframeTabla, text="quantity", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(mainframeTabla, text="unite_price", width=10, bg="gray", fg="white").grid(row=0, column=4)

# Crear datos de la tabla
data = [
      ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "bamoud boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat","80","50.0"),
    ("5", "Aroma", "cafe","60","80.0"),
    ("6", "Facto", "Facto","7000","600.0")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(mainframeTabla, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j)


raiz.mainloop()