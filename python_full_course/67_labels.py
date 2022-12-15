from tkinter import *
window = Tk()
photo = PhotoImage(file="./logo.jpg")
label = Label(window, text = "Hello World", font=("Arial", 40, "bold"), fg="#00Ff00", bg="black", relief=RAISED, bd=10, padx=20, pady=20, image=photo, compound="bottom")
label.pack()
label.place(x = 100, y = 100)
window.mainloop()