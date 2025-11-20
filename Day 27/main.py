import tkinter

window = tkinter.Tk()
window.title("My miles/kilometer calculator.")
window.minsize(width=400, height=250)
window.config(padx=10, pady=10)

first_label = tkinter.Label(text="is equal to")
first_label.grid(column=0, row=1)

first_input = tkinter.Entry()
first_input.grid(column=1, row=0)
first_input.config(width=5)

second_label = tkinter.Label(text="0")
second_label.grid(column=1, row=1)

third_label = tkinter.Label(text="Miles")
third_label.grid(column=2, row=0)

fourth_label = tkinter.Label(text="Km")
fourth_label.grid(column=2, row=1)


def button_clicked():
    miles = float(first_input.get())
    new_value = miles*1.609
    second_label.config(text=new_value)

button = tkinter.Button(text="Calculate!", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()