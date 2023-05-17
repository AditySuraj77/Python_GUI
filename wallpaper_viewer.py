from tkinter import *
from PIL import ImageTk ,Image
import os

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter = counter + 1



counter = 1
root = Tk()

root.geometry('400x700')

root.title('WallpaperViewer')
root.configure(background='black')


files = os.listdir('Wallpaper')

img_array = []

for file in files:
    img = Image.open(os.path.join('Wallpaper',file))
    resized_img = img.resize((350,500))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(10,10))

img_button = Button(root,text='Next',width=30,height=2,command=rotate_img)
img_button.pack(pady=(15,10))
img_button.config(font=('verdana',10))







root.mainloop()