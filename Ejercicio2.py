from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("700x600")
raiz.configure(background="gray40")

ttk.Label(raiz,text="Product management",font=("verdana",30,"bold"),foreground="white",background="gray40").grid(column=0,row=0,padx=80,sticky=(W))

id = int()
name = StringVar()
descrip= StringVar()
price =int ()
quan = int ()




Frame1 = ttk.Frame(raiz,background="gray2")
Frame1.grid(column=0,row=1,sticky=(W,N))

Frame2 = ttk.Frame(Frame1,background="#482525")
Frame2.grid(column=0,row=0,padx=50,pady=10,)

Frame3 = ttk.Frame(Frame2,background="#482525")
Frame3.grid(column=0,row=0,padx=20,pady=15)


imagen = PhotoImage(file="carrito2.png")
imagenC = ttk.Label(raiz,background="gray40")
imagenC.grid(column=0,row=0,sticky=(W))
imagenC['image'] = imagen

imagen1 = PhotoImage(file="Limpiar.png")
imagenl = ttk.Button(Frame3,background="#482525",pady=6,relief="flat")
imagenl.grid(column=3,row=0)
imagenl['image'] = imagen1

imagen2 = PhotoImage(file="Lupa.png")
imagenp = ttk.Button(Frame3,background="#482525",relief="flat")
imagenp.grid(column=3,row=0,sticky=(W),padx=40,pady=6)
imagenp['image'] = imagen2

ttk.Label(Frame3,text="Id product:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=0,sticky=(W,N),pady=15)
ttk.Label(Frame3,text="Name:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=1,sticky=(W,N))
ttk.Label(Frame3,text="Description:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=2,sticky=(W,N),pady=8)
ttk.Label(Frame3,text="Quantity:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=3,sticky=(W,N))
ttk.Label(Frame3,text="Price:",font=("verdana",13,"bold"),foreground="white",background="#482525").grid(column=0,row=4,sticky=(W,N))
ttk.Button(Frame3,text="Back",font=("verdana",13,"bold"),foreground="purple1",background="#482525",relief="flat").grid(column=3,row=0,sticky=(E),padx=30)

IdEntry = ttk.Entry(Frame3,width=30,textvariable=id,background="#482525")
IdEntry.grid(column=1,row=0)
nameEntry = ttk.Entry(Frame3,width=30,textvariable=id,background="#482525")
nameEntry.grid(column=1,row=1)
descripEntry = ttk.Entry(Frame3,width=30,textvariable=id,background="#482525")
descripEntry.grid(column=1,row=2)
quanEntry = ttk.Entry(Frame3,width=30,textvariable=id,background="#482525")
quanEntry.grid(column=1,row=3)
priceEntry = ttk.Entry(Frame3,width=30,textvariable=id,background="#482525")
priceEntry.grid(column=1,row=4)

ttk.Button(Frame3,text="Save",font=("verdana",13,"bold"),fg="white",background="green4",width=15,height=1).grid(column=3,row=1,padx=30)
ttk.Button(Frame3,text="Delete",font=("verdana",13,"bold"),fg="white",background="red2",width=15,height=1).grid(column=3,row=2,padx=30,pady=8)
ttk.Button(Frame3,text="Update",font=("verdana",13,"bold"),fg="white",background="DarkOrange2",width=15,height=1).grid(column=3,row=3,padx=30)

#---------------Frame Tabla---------------
TablaP = ttk.Frame(Frame3,width=20,height=20)
TablaP.grid(column=0,row=6,columnspan=5,pady=30)


# Crear encabezado de la tabla
ttk.Label(TablaP, text="ID", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(TablaP, text="Nombre", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(TablaP, text="Descripción", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(TablaP, text="Cantidad", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(TablaP, text="Precio", width=10, bg="gray", fg="white").grid(row=0, column=4)

# Crear datos de la tabla
data = [
    ("1", "Producto 1", "Descripción del producto 1", "10", "$100"),
    ("2", "Producto 2", "Descripción del producto 2", "5", "$50"),
    ("3", "Producto 3", "Descripción del producto 3", "20", "$200")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(TablaP, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j)


raiz.mainloop()