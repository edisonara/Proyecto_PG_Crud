from tkinter import PhotoImage
import tkinter as tk
from BaseDato import *
class BDOperaciones():
    _pro = 0
    _can = 0
    _par = 0
    _cole= 0

    def __init__(self):
        self.PROV_COD
        self.CANT_COD
        self.PARR_COD
        self.COLE_COD
        
    @property
    def PROV_COD(self):
        return self._pro
    
    @PROV_COD.setter
    def PROV_COD(self, valor):
        self._pro = valor

        

    @property
    def CANT_COD(self):
        self._can
    
    @CANT_COD.setter
    def CANT_COD(self, valor):
        self._can = valor

    @property
    def PARR_COD(self):
        self._par
    
    @PARR_COD.setter
    def PARR_COD(self, valor):
        self._par = valor
    
    @property
    def COLE_COD(self):
        self._cole
    
    @COLE_COD.setter
    def COLE_COD(self, valor):
        self._cole= valor


datos = BDOperaciones()
datos.CANT_COD = 20
print(type(datos.CANT_COD))


def Salir():
    print('Salir con exito. ')
    exit()



# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting root window:
root = tk.Tk()
root.title("Curd de MIES")
root.config(bg="gray17")
root.geometry("400x600+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")


# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="E", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="Programa de\nCURD\ndel Mies", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)  ## switch
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

##=======================================
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
date = BDOperaciones()
def insert():
    root2 = tk.Toplevel()
    tk.Entry(root2, textvariable=var1 , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=0,row=0)
    tk.Entry(root2, textvariable=var2 , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=0,row=1)
    tk.Entry(root2, textvariable=var3 , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=0,row=2)
    tk.Entry(root2, textvariable=var4 , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=0,row=3)
    tk.Button(root2,command= agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=3,row=6, pady=10, padx=4)

def agregar_datos():
    date.PROV_COD = var1.get()
    date.CANT_COD = var2.get()
    date.PARR_COD = var3.get()
    date.COLE_COD = var4.get()
    datos = Entidades()
    datos.inserta(numero(), date.PROV_COD, date.CANT_COD,date.PARR_COD,date.COLE_COD )
    print(date.PROV_COD)
    print(date.CANT_COD)
    print(date.PARR_COD)
    print(date.COLE_COD)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback"]
tk.Button(navRoot, text="Insertar Data",command=insert, font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=60)
tk.Button(navRoot, text="Buscar Data", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=100)
tk.Button(navRoot, text="Modificar Data", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=140)
tk.Button(navRoot, text="Eliminar Data", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=180)
tk.Button(navRoot, text="Salir", command= Salir, font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=220)


# Navbar Option Buttons:
#for i in range(5):
#    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
#    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()
