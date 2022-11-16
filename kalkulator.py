import tkinter as tk

root = tk.Tk()
root.geometry("1100x500")
text = tk.StringVar
root.title("Kalkulator")
message2 = tk.Label(root, text='Kalkulator ', fg= 'black', font=("bold", 30, "italic"))
message2.grid(row=1 )
message2.place(relx=0.5, rely=0.090, anchor=tk.CENTER)
textbox1 = tk.Entry(root, )
textbox1.place(relx=0.2, rely=0.290, anchor=tk.CENTER, width=256, height= 50)

textbox2 = tk.Entry(root, )
textbox2.place(relx=0.8, rely=0.290, anchor=tk.CENTER, width=256, height= 50)

root.resizable(False, False)    
root.mainloop()





