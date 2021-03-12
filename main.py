from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter.filedialog

MAX_IMAGE_SIZE = 900
BACK_GROUND_COLOR = "#222831"
COLOR_2 = "#393E46"
BUTTON_COLOR = "#00ADB5"
TEXT_COLOR = "#EEEEEE"
FONT_NAME = "Courier"

def open_file():
    initial_folder = os.path.abspath(os.path.expanduser('~'))
    file_name = tkinter.filedialog.askopenfilename(initialdir=initial_folder)

    image = Image.open(open(file_name, 'rb'))
    image = resize_image(image)

    global canvas_img
    canvas_img = ImageTk.PhotoImage(image)
    global canvas
    canvas.config(width=image.width, height=image.height)
    canvas.itemconfig(image_on_canvas, image=canvas_img)

def resize_image(image):
    img_max = max(image.width, image.height)
    return image.resize((image.width * MAX_IMAGE_SIZE // img_max, image.height * MAX_IMAGE_SIZE // img_max))



# ---------- UI SETUP ----------
window = Tk()
window.title("Watermark Photo")
window.config(padx=20, pady=20, bg=BACK_GROUND_COLOR)

canvas = Canvas(highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=2)

image = Image.open(open('DSC00044.JPG', 'rb'))
image = resize_image(image)
canvas_img = ImageTk.PhotoImage(image)
canvas.config(width=image.width, height=image.height)
image_on_canvas = canvas.create_image(canvas_img.width()/2, canvas_img.height()/2, image=canvas_img)


file_button = Button(text="file", highlightbackground=BUTTON_COLOR, fg=TEXT_COLOR, font=(FONT_NAME, 20),
                     highlightthickness=0, command=open_file)
file_button.grid(column=0, row=0, padx=20, pady=20, sticky=W)


window.mainloop()
