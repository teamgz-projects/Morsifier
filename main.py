import tkinter
from tkinter import *
import tkinter.font as tkFont
from code import morse, specials
import time

# Set time of a single tick
tick = .2
follower_color = 'red'
blink_color = 'blue'


def dot():
    global tick
    canvas.itemconfig(rect, fill=blink_color)
    canvas.update()
    time.sleep(tick)


def dash():
    global tick
    canvas.itemconfig(rect, fill=blink_color)
    canvas.update()
    time.sleep(tick * 3)


def gap(multiplier):
    global tick
    canvas.itemconfig(rect, fill='white')
    canvas.update()
    duration = tick * multiplier
    time.sleep(duration)


# Does the work
def process(event):
    text = my_entry.get().upper()
    label.delete('1.0', END)
    label.insert(tkinter.END, convert_morse(text))
    blink_morse(text)


# Blink out the morse code for given text
def blink_morse(text):
    global tick
    active_pos = 0
    for character in text:
        label.tag_remove("active", 1.0, tkinter.END)
        if character == ' ':
            gap(7)
            active_pos += 2
            continue

        if character in morse:
            for bip in morse[character]:
                active_pos += 1
                label.tag_remove("active", 1.0, tkinter.END)
                label.tag_add('active', f'1.{active_pos}')
                if bip == '.':
                    dot()
                elif bip == '-':
                    dash()

                gap(1)
        active_pos += 1
        gap(3)

    canvas.itemconfig(rect, fill='white')
    label.tag_remove("active", 1.0, tkinter.END)


# Convert given text into readable morse code
def convert_morse(text):
    separator = " "
    space_separator = " +"

    result = ""
    for character in text:
        if character == " ":
            result = result + space_separator

        if character in morse:
            if character in specials:
                result = result + separator + "(" + morse[character] + ")"
            else:
                result = result + separator + morse[character]

    return result


# Set up window
root = Tk()
root.title("Dylan's Morsifier")
root.geometry("600x500")

frame = Frame(root)
frame.pack()

entry_label = Label(frame, text="Enter text")
entry_label.pack()

my_entry = Entry(frame, width=30)
my_entry.pack(padx=5)
my_entry.focus()

button = Button(frame, text="Morsify", command=lambda: process(None))
button.pack(pady=5)

# Label to hold morse text
fontstyle = tkFont.Font(family="Lucida Grande", size=30)
active_style = tkFont.Font(family='Lucida Grande', size=30, weight='bold')
label = Text(frame, width=20, height=3, font=fontstyle)
# color of the follower
label.tag_configure('active', foreground=follower_color, font=active_style)
label.pack(pady=10)

w = 500
h = 200
canvas = Canvas(root, width=w, height=h)
canvas.pack()
rect = canvas.create_rectangle(0, 0, w, h, fill="white")

root.bind('<Return>', process)
root.mainloop()
