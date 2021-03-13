from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import ImageTk
from watermark_image import WatermarkImage

BACK_GROUND_COLOR = "#222831"
COLOR_2 = "#393E46"
COLOR_3 = "#00ADB5"
COLOR_4 = "#EEEEEE"
FONT_NAME = "Montserrat-Light.ttf"

def change_canvas_image(image):
    canvas.photo = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    global image_on_canvas
    if image_on_canvas == None:
        image_on_canvas = canvas.create_image(0,0, image=canvas.photo, anchor="nw")
    else:
        canvas.itemconfig(image_on_canvas, image=canvas.photo)

def open_image_file():
    wmi.open_image_file()
    change_canvas_image(wmi.image)

def save_image_file():
    wmi.save_image_file()
    tkmsg.showinfo(message="Watermarked Image Saved")

wmi = WatermarkImage()

# ---------- UI SETUP ----------
window = Tk()
window.title("Watermark Photo")
window.config(padx=20, pady=20, bg=BACK_GROUND_COLOR)

canvas = Canvas(highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=3)
image_on_canvas = None
wmi.load_image_file('DSC00044.JPG')
change_canvas_image(wmi.image)

button_frame = Frame(bg=BACK_GROUND_COLOR)
open_button = Button(button_frame, text="Open File", font=(FONT_NAME, 20),
                     highlightthickness=0, command=open_image_file)
open_button.config(padx=5)
save_button = Button(button_frame, text="Save File", font=(FONT_NAME, 20),
                     highlightthickness=0, command=save_image_file)
save_button.config(padx=5)

button_frame.grid(column=0, row=0, sticky=W)
open_button.grid(column=0, row=0, padx=10, pady=20)
save_button.grid(column=1, row=0, padx=10, pady=20)

window.mainloop()
