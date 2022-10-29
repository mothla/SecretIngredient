#importing library
import time
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image

splash_root = Tk()
splash_root.title("SecreteIngredient")
# screen size
splash_root.geometry("925x500+300+200")
splash_root.config(bg="#FFFFFF")
# splash screen content
splash = ImageTk.PhotoImage(Image.open("h2.png"))
splashLogo= Label(splash_root, image=splash).place(x=300, y=30)


label2=Label(splash_root, text='Loading...', fg='white', bg='#ff9a00') #decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=500)

#making animation

image_a=ImageTk.PhotoImage(Image.open('Ellipse1.png'))
image_b=ImageTk.PhotoImage(Image.open('Ellipse2.png'))



for i in range(3): #5loops


    l1=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=420, y=400)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
    l2=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=440, y=400)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
    l3=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=460, y=400)
    l4=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

    l1=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
    l2=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
    l3=Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
    l4=Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=480, y=400)
    splash_root.update_idletasks()
    time.sleep(0.5)

#new window to open
def new_win():

    home = Tk()
    home.title('HOME PAGE')
    home.geometry("925x500+300+200")
    home.config(bg="#FFFFFF")
    # anything we need to appear in main page write in this function
    # Load the image
    image = Image.open('h2.png')
    # Resize the image in the given (width, height)
    img = image.resize((150, 150))
    # Conver the image in TkImage
    my_img = ImageTk.PhotoImage(img)
    # Display the image with label
    label = Label(home, image=my_img)
    label.pack(pady=9)

    # Create profile Button
    myFont = Font(family='Courier', size=10, weight='bold')
    profile_button = Button(home, text="Profile", bg="#ff7400", fg='#ffffff', width=25, height=3 , activebackground='white')
    profile_button['font'] = myFont
    profile_button.pack(pady=20)

    # Create QR Button
    QR_button = Button(home, text="Search", bg="#ff7400", fg='#ffffff', width=25, height=3, activebackground='white')
    QR_button['font'] = myFont
    QR_button.pack(pady=24)
    home.mainloop()








splash_root.destroy()
new_win()
splash_root.mainloop()
