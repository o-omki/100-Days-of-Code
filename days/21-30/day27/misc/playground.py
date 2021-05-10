# def adds(*args):
    
#     print(args[1])
#     sum = 0
#     for num in args:
#         sum += num

#     print(sum)

# adds(1, 2, 3,  4)

# def calc(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
    
#     print(n)


# calc(3, add = 2, multiply = 4)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")

car = Car(make = "merc", model = "abc")
print(car.colour)



import tkinter

window = tkinter.Tk()
window.title("first GUI program")
window.minsize(height = 300, width = 500)

my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label.pack()



def button_clicked():
    my_label.config(text = "I got clicked")

button = tkinter.Button(text = "click me", command = button_clicked)
button.pack()


input = tkinter.Entry(width =20)
input.insert(tkinter.END, string = "Some default text")
print(input.get())
input.pack()


text = tkinter.Text(height = 6, width = 25)
text.focus()
text.insert(tkinter.END, "Example of a multiline text box")
print(text.get("1.2", tkinter.END))
text.pack()


def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_ = 0, to = 10, width = 5, command = spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)

scale = tkinter.Scale(from_ = 0, to = 100, command = scale_used)
scale.pack()


def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text = "Is On?", variable = checked_state, command = checkbutton_used)
checked_state.get()
checkbutton.pack()


def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text = "Opt1", value = 1, variable = radio_state, command = radio_used)
radiobutton2 = tkinter.Radiobutton(text = "Opt2", value = 2, variable = radio_state, command = radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height = 4)
fruits = ["apple",  "Pear", "Banana", "Mango"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop() 