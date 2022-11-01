from tkinter import *
from tkinter import messagebox
import ast
import time
from tkinter.font import Font
from PIL import ImageTk, Image
import oracledb
import cv2
from pyzbar.pyzbar import decode

root= Tk()
root.title('Login')
root.geometry('925x500+100+100')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    file = open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()


    if username in r.keys() and password==r[username]:
        root.destroy()
        home()

    else:
        messagebox.showerror('Invalid','invalid username or password')


def signup_command():

    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if password == conform_password:
            try:
               file=open('datasheet.txt','r+')
               d=file.read()
               r=ast.literal_eval(d)

               dict2= {username:password}
               r.update(dict2)
               file.truncate(0)
               file.close()

               file=open('datasheet.txt','w')
               w=file.write(str(r))

               messagebox.showinfo('Signup','Sucessfully sign up')



            except:
                file = open('datasheet.txt', 'w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()


        else:
            messagebox.showerror('Invalid',"Both Password should match")


    def sign():
        img = PhotoImage(file= 'logo (3).png')
    frame=Frame(root,width=350,height=390,bg="white")
    frame.place(x=480,y=50)


    heading=Label(frame,text='Sign up', fg='#F37D0C',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)


    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')


    user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def on_enter(e):
        conform_code.delete(0, 'end')

    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Conform Password')

    conform_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Conform Password')
    conform_code.bind('<FocusIn>', on_enter)
    conform_code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    Button(frame,width=39,pady=7,text='Sign up',bg='#F37D0C',fg='white',border=0,command=signup).place(x=35,y=280)



img = PhotoImage(file= 'logo (3).png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg='#F37D0C',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame,width=25,border=0,bg="white",fg='black',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code = Entry(frame,width=25,border=0,bg="white",fg='black',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


Button(frame,width=39,pady=7,text='Sign in',bg='#F37D0C',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#F37D0C',command=signup_command)
sign_up.place(x=215,y=270)

def home():
    splash_root = Tk()
    splash_root.title("Secret ingredient")

    splash_root.geometry("925x500+100+100")
    splash_root.config(bg="#FFFFFF")

    splash = ImageTk.PhotoImage(Image.open("h2 (1).png"))
    splashLogo = Label(splash_root, image=splash).place(x=300, y=30)

    splash_root.title("Secret ingredient")
    splash = ImageTk.PhotoImage(Image.open("h2 (1).png"))
    splashLogo = Label(splash_root, image=splash).place(x=300, y=30)

    label2 = Label(splash_root, text='Loading...', fg='white', bg='#ff9a00')  # decorate it
    label2.configure(font=("Calibri", 11))
    label2.place(x=420, y=360)


    image_a = ImageTk.PhotoImage(Image.open('Ellipse1.png'))
    image_b = ImageTk.PhotoImage(Image.open('Ellipse2.png'))

    for i in range(2):

        l1 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=420, y=400)
        l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
        l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
        l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
        splash_root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
        l2 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=440, y=400)
        l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
        l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
        splash_root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
        l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
        l3 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=460, y=400)
        l4 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=480, y=400)
        splash_root.update_idletasks()
        time.sleep(0.5)

        l1 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=420, y=400)
        l2 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=440, y=400)
        l3 = Label(splash_root, image=image_b, border=0, relief=SUNKEN).place(x=460, y=400)
        l4 = Label(splash_root, image=image_a, border=0, relief=SUNKEN).place(x=480, y=400)
        splash_root.update_idletasks()
        time.sleep(0.5)
    splash_root.destroy()
    new_win()
    splash_root.mainloop()


def new_win():

    home = Tk()
    home.title('Home page')
    home.geometry("925x500+100+100")
    home.config(bg="#FFFFFF")

    frame = Frame(home,width=150,height=150)
    frame.pack()
    img = ImageTk.PhotoImage(Image.open("h2.png"))
    label = Label(frame, image=img)
    label.pack()
    # Create profile Button
    myFont = Font(family='Courier', size=10, weight='bold')
    profile_button = Button(home, text="Profile", bg="#ff7400", fg='#ffffff', width=25, height=3,
                                activebackground='white')
    profile_button['font'] = myFont
    profile_button.pack(pady=20)

    QR_button = Button(home, text="Search", bg="#ff7400", fg='#ffffff', width=25, height=3,
                           activebackground='white' , command=Search)
    QR_button['font'] = myFont
    QR_button.pack(pady=24)
    home.mainloop()

def Search():
    oracledb.init_oracle_client(lib_dir=r"C:\Users\Wajd_\Desktop\Oracle\instantclient_21_7")

    root = Tk()

    canvas1 = Canvas(root, width=925, height=500, relief='raised')
    canvas1.pack()

    label2 = Label(root, text='Search or scan the barcode to get all the prices in different places:')
    label2.config(font=('helvetica', 20))
    canvas1.create_window(480, 100, window=label2)  # x,y

    entry1 = Entry(root,width= 38, font='Arial 20')

    canvas1.create_window(500, 200, window=entry1)  # x,y

    def Scanning():
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        flag = False
        value = dict(barcode='NULL')
        while True:
            success, frame = cap.read()
            for code in decode(frame):
                value["barcode"] = code.data.decode('utf-8')
                flag = True
            if flag:
                break
            cv2.imshow('BarcodeScanner', frame)

        try:
            con = oracledb.connect('wajd/wajd1200@laptop-fbns74ci:1521/XE')
            cursor = con.cursor()
            q = "SELECT pro_name,price, v_name FROM product,prices,vendors where (vendors.v_id = prices.v_id AND product.pro_id = prices.pro_id) AND (barcode = :barcode)"
            cursor.execute(q,value)
            con.commit()
            rows = cursor.fetchall()

            supermarket1 = rows[0]
            pro_name = supermarket1[0]
            price = supermarket1[1]
            v_name = supermarket1[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(200, 420, window=label3)

            supermarket2 = rows[1]
            pro_name = supermarket2[0]
            price = supermarket2[1]
            v_name = supermarket2[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(500, 420, window=label3)


            supermarket3 = rows[2]
            pro_name = supermarket3[0]
            price = supermarket3[1]
            v_name = supermarket3[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(790, 420, window=label3)

            supermarket4 = rows[3]
            pro_name = supermarket4[0]
            price = supermarket4[1]
            v_name = supermarket4[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(200, 500, window=label3)

            supermarket5 = rows[4]
            pro_name = supermarket5[0]
            price = supermarket5[1]
            v_name = supermarket5[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(500, 500, window=label3)

            supermarket6 = rows[5]
            pro_name = supermarket6[0]
            price = supermarket6[1]
            v_name = supermarket6[2]


            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR', font=('helvetica', 12))
            canvas1.create_window(800, 500, window=label3)


        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()


    def Searching():
        name = entry1.get()
        try:
            con = oracledb.connect('wajd/wajd1200@laptop-fbns74ci:1521/XE')
            cursor = con.cursor()
            q = "SELECT pro_name,price, v_name FROM product,prices,vendors where (vendors.v_id = prices.v_id AND product.pro_id = prices.pro_id) AND (pro_name like '%{}%')".format(name)
            cursor.execute(q)
            con.commit()
            rows = cursor.fetchall()

            supermarket1 = rows[0]
            pro_name = supermarket1[0]
            price = supermarket1[1]
            v_name = supermarket1[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(200, 420, window=label3)

            supermarket2 = rows[1]
            pro_name = supermarket2[0]
            price = supermarket2[1]
            v_name = supermarket2[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(500, 420, window=label3)


            supermarket3 = rows[2]
            pro_name = supermarket3[0]
            price = supermarket3[1]
            v_name = supermarket3[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(790, 420, window=label3)

            supermarket4 = rows[3]
            pro_name = supermarket4[0]
            price = supermarket4[1]
            v_name = supermarket4[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(200, 500, window=label3)

            supermarket5 = rows[4]
            pro_name = supermarket5[0]
            price = supermarket5[1]
            v_name = supermarket5[2]

            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                                      'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR',
                           font=('helvetica', 12))
            canvas1.create_window(500, 500, window=label3)

            supermarket6 = rows[5]
            pro_name = supermarket6[0]
            price = supermarket6[1]
            v_name = supermarket6[2]


            label3 = Label(root, text='Product name: ' + str(pro_name) + '\n' +
                'Supremarket:' + str(v_name) + '\nPrice:' + str(price) + 'SAR', font=('helvetica', 12))
            canvas1.create_window(800, 500, window=label3)


        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()


    button1 = Button(root,text='Search', command=Searching, bg='#F37D0C', fg='#ffffff', width=15, height=2,
                        font=('helvetica', 11, 'bold'))
    canvas1.create_window(330, 300, window=button1)

    button2 = Button(root, text='Scan', command=Scanning, bg='#F37D0C', fg='#ffffff', width=15, height=2,
                     font=('helvetica', 11, 'bold'))
    canvas1.create_window(680, 300, window=button2)


root.mainloop()
