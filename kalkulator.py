import tkinter as tk

root = tk.Tk()
root.geometry("1100x500")
zmienna1 = tk.IntVar()
zmienna2 = tk.IntVar()

def printinput(*args):
   print(zmienna1.get())
def printinput(*args):
   print(zmienna2.get())
text = tk.StringVar
root.title("Kalkulator")
message2 = tk.Label(root, text='Kalkulator ',  fg= 'black', font=("bold", 30, "italic"))
message2.grid(row=1 )
message2.place(relx=0.5, rely=0.090, anchor=tk.CENTER)
textbox1 = tk.Entry(root, textvariable=zmienna1 , font=('Times', 24))
textbox1.place(relx=0.2, rely=0.290, anchor=tk.CENTER, width=256, height= 50)
opcje = ['+','-','*','/']
textbox2 = tk.Entry(root, textvariable=zmienna2 , font=('Times', 24) )
textbox2.place(relx=0.8, rely=0.290, anchor=tk.CENTER, width=256, height= 50)

zmienna3 =tk.StringVar(root)
def display_selected(choice):
    choice = zmienna3.get()
    print(choice)

dropdown = tk.OptionMenu(root, zmienna3, *opcje, command=display_selected)
dropdown.pack()
dropdown.grid(row=5,column=4)
dropdown.place(relx=0.5, rely=0.300, anchor=tk.CENTER, width=256, height= 50)
dropdown.config(font=('Times', 24))
message3 = tk.Label(root,   fg= 'black', font=("bold", 30, "italic"))
message3.grid(row=1 )
message3.place(relx=0.5, rely=0.530, anchor=tk.CENTER)
def print_answers():
    message3.config(text=format(zmienna3.get()))
    return None

def wybrana_metoda():
    if zmienna3.get() == "":
          message3.config(text="Wybierz co chcesz zrobić z liczba")
    if zmienna3.get() == "+":
     sumation = zmienna1.get() + zmienna2.get()
     message3.config(text="Oto liczba twoja " + str(sumation))
    elif zmienna3.get() == "-":
     sumation = zmienna1.get() - zmienna2.get()
     message3.config(text="Oto liczba twoja " + str(sumation))
    elif zmienna3.get() == "*":
     sumation = zmienna1.get() * zmienna2.get()
     message3.config(text="Oto liczba twoja " + str(sumation))
    elif zmienna3.get() =="/" and zmienna2.get() ==0:
        message3.config(text="OK, nie dziel przez zero")

    elif zmienna3.get() == "/":
        
     sumation = zmienna1.get() / zmienna2.get()
     
     
     

     message3.config(text="Oto liczba twoja " + str(sumation))

    

def display_selected(choice):
    choice = zmienna3.get()
    print(choice)
def change_table():
    zmienna3 = dropdown.get()
    message3.config(text="Oto liczba twoja " + str(zmienna3))
Przycisk = tk.Button(root, text=("Oblicz"), command=wybrana_metoda , font=('Times', 24))
Przycisk.grid(row=2, column=1)
Przycisk.place(relx=0.5, rely=0.700, anchor=tk.CENTER, width=256, height= 50)


root.resizable(False, False)    

root.mainloop()





