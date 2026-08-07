from tkinter import *

window = Tk()
window.title(string ="Mile to Kilometer Converter")
window.minsize(width = 300, height = 100)
window.config(padx = 20, pady = 20)

input = Entry(width = 10)
input.grid(column = 1, row = 0)

miles = Label(text = "Miles")
miles.grid(column = 2, row = 0)

equal_to = Label(text = "is equal to")
equal_to.grid(column=0, row=1)

answer = Label(text = 0)
answer.grid(column=1, row=1)

kilometres = Label(text = "Kilometres")
kilometres.grid(column=2, row=1)

def calculate():
    miles_in_number = float(input.get())
    kilometres_in_number = miles_in_number * 1.609344
    answer.config(text = round(kilometres_in_number))

calculate = Button(text = "Calculate", command = calculate)
calculate.grid(column = 1, row = 2)


window.mainloop()