import tkinter
import turtle

window = tkinter.Tk()
window.title("My GUI Program.")
window.minsize(width=1000, height=600)
window.config(padx=100, pady=100)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#Label doesn't work without the following command
#my_label.pack(side="top")  #expand=True puts text in center // side = left for instance will put the text on the left of the screen
my_label.grid(column=0, row=0)

#my_label["text"] = "New Text"  --> this version and the one below are equal to set options
my_label.config(text="New Text")

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me!", command=button_clicked)
#button.place(x=100, y=100)  #similiar to .pack but more specific
button.grid(column=1, row=1)   #--> divides screen into a grid and you can place your text with: column= & row= --> however .pack and .grid don't work together

new_button = tkinter.Button(text="I'm another button.")
new_button.grid(column=2, row=0)

input = tkinter.Entry(width=30)
input.grid(column=3, row=2)





window.mainloop()