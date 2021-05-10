import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = tkinter.Tk()
window.title("First GUI")
window.minsize(height = 300, width = 500)
window.config(padx = 100, pady = 200)

my_label = tkinter.Label(text = "Label text", font = ("Arial", 18, "bold"))
my_label.grid(row = 0, column = 0)

button = tkinter.Button(text = "click here", command = button_clicked)
button.grid(column = 1, row = 1)

new_button = tkinter.Button(text = "click here", command = button_clicked)
new_button.grid(column = 2, row = 0)


input = tkinter.Entry(width = 10)
print(input.get())
input.grid(row = 2, column= 3)



window.mainloop()