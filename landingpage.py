from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from PIL import ImageTk

def customerservicepage():
    import customerservicepage
customtkinter.set_appearance_mode("dark")
root = Tk()
root.geometry('1366x768')
root.state('zoomed')

bgimage = ImageTk.PhotoImage(file='landingpage.png')
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

inventoryimage = ImageTk.PhotoImage(file='inventorybutton.png')
inventorybutton = Button(root, image = inventoryimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=inventorypage)
inventorybutton.place(x=60, y=90)

staffschedulingimage = ImageTk.PhotoImage(file='staffschedulingbutton.png')
staffschedulingbutton = Button(root, image = staffschedulingimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=staffschedulingpage)
staffschedulingbutton.place(x=470, y=90)

customerserviceimage = ImageTk.PhotoImage(file='customerservicebutton.png')
customerservicebutton = Button(root, image = customerserviceimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0, command=customerservicepage)
customerservicebutton.place(x=880, y=90)

menuimage = ImageTk.PhotoImage(file='menubutton.png')
menubutton = Button(root, image = menuimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=menupage)
menubutton.place(x=60, y=375)

staffsalaryimage = ImageTk.PhotoImage(file='staffsalarybutton.png')
staffsalarybutton = Button(root, image = staffsalaryimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=staffsalarypage)
staffsalarybutton.place(x=470, y=375)

kitchenimage = ImageTk.PhotoImage(file='kitchenbutton.png')
kitchenbutton = Button(root, image = kitchenimage , fg='white', bg='white', activeforeground='white',
                    activebackground='white', cursor='hand2', bd=0)#, command=kitchenpage)
kitchenbutton.place(x=880, y=375)

root.mainloop()

