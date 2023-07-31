import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

def pixelate_image(image_path, pixels_on_greatest_side):
    # Чтение изображения
    img = cv2.imread(image_path)

    # Вычисление соотношения сторон изображения
    aspect_ratio = img.shape[1] / img.shape[0]

    if aspect_ratio >= 1:
        # Горизонтальное или квадратное изображение
        new_width = pixels_on_greatest_side
        new_height = int(pixels_on_greatest_side / aspect_ratio)
    else:
        # Вертикальное изображение
        new_height = pixels_on_greatest_side
        new_width = int(pixels_on_greatest_side * aspect_ratio)

    # Уменьшение размера изображения до желаемого размера пикселей
    small = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Восстановление до оригинального размера
    result = cv2.resize(small, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

    return result

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        pixels_on_greatest_side = int(pixel_entry.get())
        pixelated_img = pixelate_image(file_path, pixels_on_greatest_side)
        pixelated_img = cv2.cvtColor(pixelated_img, cv2.COLOR_BGR2RGB) # Convert to RGB
        im_pil = Image.fromarray(pixelated_img)
        image_tk = ImageTk.PhotoImage(im_pil)
        label_image.configure(image=image_tk)
        label_image.image = image_tk

root = tk.Tk()

pixel_label = tk.Label(root, text="Pixels on greatest side:")
pixel_label.pack()

pixel_entry = tk.Entry(root)
pixel_entry.pack()

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

label_image = tk.Label(root)
label_image.pack()

root.mainloop()
