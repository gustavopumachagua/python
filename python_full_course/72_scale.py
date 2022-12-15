from tkinter import *

def submit():
  print("The temperature is: "+ str(scale.get())+ "degrees C")

window = Tk()

hotImage = PhotoImage(file="logo.jpg")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, from_=1000, to=0, length=600, orient=VERTICAL, font=("Consolas", 20), tickinterval=10, showvalue=0, resolution=5, troughcolor="#69eaff", fg="#ff1c00", bg="#111")
scale.set(((scale["from"]-scale["to"])/2)+scale["to"])
scale.pack()
coldImage = PhotoImage(file="logo.jpg")
coldLabel = Label(image=coldImage)
coldLabel.pack()
button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()