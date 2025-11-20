import requests, tkinter


def get_quote():
    response = requests.get(url="http://api.kanye.rest")
    data = response.json()["quote"]
    canvas.itemconfig(text, text=data)

window = tkinter.Tk()
window.title("Ye Quotes")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=400, width=400)
photoimage = tkinter.PhotoImage(file="./Day 33/background.png")
canvas.create_image(200, 200, image=photoimage)
text = canvas.create_text(200, 200, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15))
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="./Day 33/kanye.png")
ye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
ye_button.grid(row=1, column=0)






window.mainloop()