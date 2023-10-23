import os
from tkinter import Tk, ttk
from tkinter import Label
from PIL import Image, ImageTk
import tkinter as tk
import time

def load_images(image_dir):
	images = []
	for file in os.listdir(image_dir):
		if file.endswith('.jpg'):
			image = Image.open(os.path.join(image_dir, file))
			images.append(image)
	return images

def countdown(time):
    if time > -1:
        mins, secs = divmod(time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label['text'] = timer
        root.after(1000, countdown, time-1)
    else:
        label['text'] = '!'
        root.destroy()

root = Tk()
root.title('datatransmittingprocess')
root.geometry('1920x1080')

images = load_images('./img/full')

image_photo = ImageTk.PhotoImage(images[0].resize((1000, 1000)))
label = Label(root, image=image_photo)
label.grid(row=0, column=0)

timer_label = tk.Label(root, font=('Nimbus', 30))
timer_label.grid(row=1, column=0)

#Start countdown from 30 minutes (1800 seconds)

countdown(900)


def update_image():
	update_image.current_image += 1
	if update_image.current_image >= len(images):
		update_image.current_image = 0
	photo = ImageTk.PhotoImage(images[update_image.current_image].resize((1920, 1080)))
	label.config(image=photo)
	label.image = photo
	root.after(1, update_image)

update_image.current_image = 0



update_image()
root.mainloop()
