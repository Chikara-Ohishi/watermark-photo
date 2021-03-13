from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import os
import pathlib

MAX_IMAGE_SIZE = 900

WATER_MARK_COLOR = "#FFFFFF"
WATER_MARK_FONT_NAME = "Montserrat-Light.ttf"
WATER_MARK_FONT_SIZE = 30
WATER_MARK_POS_X = 0.05
WATER_MARK_POS_Y = 0.1
WATER_MARK_TEXT = "Watermark Text"

class WatermarkImage:
    def __init__(self):
        self.image = None
        self.file_name = None

    def load_image_file(self, file_name):
        self.file_name = file_name
        print(f"load_image_file: {file_name}")

        if file_name:
            with open(file_name, 'rb') as file:
                self.image = Image.open(file)
                self.resize_image()
                self.draw_watermark()

    def open_image_file(self):
        initial_folder = os.path.abspath(os.path.expanduser('~'))
        file_name = filedialog.askopenfilename(initialdir=initial_folder)

        self.load_image_file(file_name)

    def resize_image(self):
        img_max = max(self.image.width, self.image.height)
        self.image = self.image.resize((self.image.width * MAX_IMAGE_SIZE // img_max,
                                      self.image.height * MAX_IMAGE_SIZE // img_max))

    def draw_watermark(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(WATER_MARK_FONT_NAME, WATER_MARK_FONT_SIZE)
        draw.text((self.image.width * WATER_MARK_POS_X, self.image.height * ( 1 - WATER_MARK_POS_Y)),
                   WATER_MARK_TEXT, font=font)

    def save_image_file(self):
        if self.file_name:
            path = pathlib.PurePath(self.file_name)
            save_file = path.parent / f"{path.stem}_watermark{path.suffix}"
            print(f"save_image_file: {os.fspath(save_file)}")
            self.image.save(os.fspath(save_file))