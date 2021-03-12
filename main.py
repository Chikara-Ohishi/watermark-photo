from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter.filedialog

MAX_IMAGE_SIZE = 900
BACK_GROUND_COLOR = "#222831"
COLOR_2 = "#393E46"
COLOR_3 = "#00ADB5"
COLOR_4 = "#EEEEEE"
WATER_MARK_COLOR = "#FFFFFF"
FONT_NAME = "Courier"

def open_file():
    initial_folder = os.path.abspath(os.path.expanduser('~'))
    file_name = tkinter.filedialog.askopenfilename(initialdir=initial_folder)

    if file_name:
        with open(file_name, 'rb') as file:
            image = Image.open(file)
            image = resize_image(image)
            change_canvas_image(image)

def resize_image(image):
    img_max = max(image.width, image.height)
    return image.resize((image.width * MAX_IMAGE_SIZE // img_max, image.height * MAX_IMAGE_SIZE // img_max))

def change_canvas_image(image):
    canvas.photo = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.itemconfig(image_on_canvas, image=canvas.photo)
    canvas.coords(text_on_canvas, image.width / 2, image.height / 2)


# ---------- UI SETUP ----------
window = Tk()
window.title("Watermark Photo")
window.config(padx=20, pady=20, bg=BACK_GROUND_COLOR)

canvas = Canvas(highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=3)

image = Image.open(open('DSC00044.JPG', 'rb'))
image = resize_image(image)
canvas.photo = ImageTk.PhotoImage(image)
canvas.config(width=image.width, height=image.height)
image_on_canvas = canvas.create_image(0,0, image=canvas.photo, anchor="nw")
text_on_canvas = canvas.create_text(canvas.photo.width() / 2, canvas.photo.height() / 2,
                                    text="Watermark Text", fill=WATER_MARK_COLOR, font=(FONT_NAME, "40"))

button_frame = Frame(bg=BACK_GROUND_COLOR)
open_button = Button(button_frame, text="Open File", font=(FONT_NAME, 20),
                     highlightthickness=0, command=open_file)
open_button.config(padx=5)
save_button = Button(button_frame, text="Save File", font=(FONT_NAME, 20),
                     highlightthickness=0, command=open_file)
save_button.config(padx=5)

button_frame.grid(column=0, row=0, sticky=W)
open_button.grid(column=0, row=0, padx=10, pady=20)
save_button.grid(column=1, row=0, padx=10, pady=20)

window.mainloop()
