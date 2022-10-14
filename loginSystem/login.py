# import opencv
import tkinter as tk
from tkinter import ttk
from tkinter import Entry, Toplevel, Canvas
from tkinter import Frame, Entry, Radiobutton, Checkbutton, Text, Listbox, Tk, Label, StringVar, Menu, IntVar
# import tkMessageBox as messagebox
 from PIL import Image, ImageDraw, ImageTk, ImageFont
import json
import pickle


class bookingApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, "bOOk!nG.CoM")
        Tk.iconbitmap(self, "logo.ico")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = Menu(container)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Home", command=lambda: self.show_frame(StartPage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, RegisterPage, LoginPage, WelcomePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open("logo.jpg")
        background_image = ImageTk.PhotoImage(image)
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        label1 = Label(self, text="bOOk!nG.CoM", font=("Ravie", 26), bg="black", fg="darkorange2")
        label1.pack(padx=10, pady=50)

        text1 = "New user?\nRegister here"
        button1 = tk.Button(self, text=text1, font=("Calisto MT", 12),
                            command=lambda: controller.show_frame(RegisterPage), activebackground="white",
                            relief=tk.RAISED, width=15, bg="darkorange3")
        button1.pack()

        text2 = "Existing user?\nLog In"
        button2 = tk.Button(self, text=text2, font=("Calisto MT", 12), command=lambda: controller.show_frame(LoginPage),
                            activebackground="white",
                            relief=tk.RAISED, width=15, bg="darkorange3")
        button2.pack()


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        rows = 0
        while rows < 50:
            #     self.grid_rowconfigure(rows,weight=6)
            self.grid_columnconfigure(rows, weight=1)
            rows += 1

        label = Label(self, text="SIGN UP", font=("Calisto MT", 28, "bold", "underline"), bg="gray94", fg="black")
        label.grid(row=0, column=23, columnspan=3, rowspan=3)

        Label(self, text="\n\n\n\n").grid(row=3)
        label1 = Label(self, text="First Name", font=("Calisto MT", 18))
        label1.grid(row=6, column=23)
        label2 = Label(self, text="Last Name", font=("Calisto MT", 18))
        label2.grid(row=7, column=23)
        Label(self, text="E-mail Id", font=("Calisto MT", 18)).grid(row=8, column=23)
        Label(self, text="Password", font=("Calisto MT", 18)).grid(row=9, column=23)
        Label(self, text="Confirm Password", font=("Calisto MT", 18)).grid(row=10, column=23)

        e1 = Entry(self, font=("Calisto MT", 16))
        e2 = Entry(self, font=("Calisto MT", 16))
        e1.grid(row=6, column=24)
        e2.grid(row=7, column=24)
        e3 = Entry(self, font=("Calisto MT", 16))
        e3.grid(row=8, column=24)
        ep1 = Entry(self, font=("Calisto MT", 16), show="*")
        ep1.grid(row=9, column=24)
        ep2 = Entry(self, font=("Calisto MT", 16), show="*")
        ep2.grid(row=10, column=24)
        dict_ent = {"FirstName": e1, "LastName": e2, "E-mail": e3, "Password": ep1, "ConfPassword": ep2}

        var1 = IntVar()
        cb1 = Checkbutton(self, text="Show Password", variable=var1, command=lambda: cb_change(var1, ep1))
        cb1.grid(row=9, column=25)

        Label(self, text="\n\n").grid(row=11)

        button1 = tk.Button(self, text="Submit", font=("Calisto MT", 12),
                            command=lambda: self.reg_status(controller, dict_ent),
                            activebackground="light cyan", relief=tk.RAISED, width=15)
        button1.grid(row=13, column=23)

        button2 = tk.Button(self, text="Reset", font=("Calisto MT", 12),
                            command=lambda: reset_field([e1, e2, e3, ep1, ep2]), activebackground="light cyan",
                            relief=tk.RAISED, width=15)
        button2.grid(row=13, column=24)
        button2 = tk.Button(self, text="Already registered? Log in Here", font=("Calisto MT", 12),
                            command=lambda: [controller.show_frame(LoginPage), reset_field([e1, e2, e3, ep1, ep2])],
                            activebackground="light cyan",
                            relief=tk.RAISED, width=25)
        button2.grid(row=14, column=23, columnspan=2)

    def reg_status(self, controller, dict_ent):
        dict_out = {}
        jsonObj = []
        dict_out = collect_ent(dict_ent)

        for key in dict_out:
            if dict_out[key] == "":
                popupmsg("Fill all the fields")
                return

        varE = self.exist_email(dict_out)
        if (varE == 1):
            popupmsg("E-mail Id already exists!!")
            return
        if (len(dict_out["Password"]) < 8):
            popupmsg("Password too short!")
            return

        if (dict_out["Password"] != dict_out["ConfPassword"]):
            popupmsg("Passwords don't match!!")
            return

        else:
            jsonObj.append(dict_out)
            fw = open("database.txt", "a")
            fw.write(json.dumps(jsonObj))
            fw.write("\n")
            fw.close()
            controller.show_frame(LoginPage)
            ent_lst = []
            for key in dict_ent:
                ent_lst.append(dict_ent[key])
            reset_field(ent_lst)
        # fr.close()

    def exist_email(self, dict_):
        lst = read_filejson()
        for dict1 in lst:
            if dict1['E-mail'] == dict_['E-mail']:
                return 1
        return 0


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        rows = 0
        while rows < 21:
            #     self.grid_rowconfigure(rows,weight=6)
            self.grid_columnconfigure(rows, weight=1)
            rows += 1

        label = Label(self, text="SIGN IN", font=("Calisto MT", 28, "bold", "underline"), bg="gray94", fg="black")
        label.grid(row=0, column=10, columnspan=2, rowspan=3)

        Label(self, text="\n\n\n\n").grid(row=3)
        label1 = Label(self, text="E-mail", font=("Calisto MT", 18))
        label1.grid(row=6, column=10)
        label2 = Label(self, text="Password", font=("Calisto MT", 18))
        label2.grid(row=7, column=10)

        e1 = Entry(self, font=("Calisto MT", 16))
        e2 = Entry(self, font=("Calisto MT", 16), show="*")
        e1.grid(row=6, column=11)
        e2.grid(row=7, column=11)
        ldict_ent = {"E-mail": e1, "Password": e2}

        var1 = IntVar()
        cb1 = Checkbutton(self, text="Show Password", variable=var1, command=lambda: cb_change(var1, e2))
        cb1.grid(row=7, column=12)

        Label(self, text="\n\n").grid(row=8)

        button1 = tk.Button(self, text="Login", font=("Calisto MT", 12),
                            command=lambda: self.log_status(controller, ldict_ent), activebackground="light cyan",
                            relief=tk.RAISED, width=15)
        button1.grid(row=10, column=11)

        button2 = tk.Button(self, text="New User? Register", font=("Calisto MT", 12),
                            command=lambda: controller.show_frame(RegisterPage), activebackground="light cyan",
                            relief=tk.RAISED, width=15)
        button2.grid(row=10, column=10)

    def log_status(self, controller, ent):
        dict_out = {}
        dict_out = collect_ent(ent)
        # print(dict_out)
        for key in dict_out:
            if dict_out[key] == "":
                popupmsg("Incomplete Fields!!")
                return

        varE = self.match_det(dict_out)
        if (varE == 0):
            popupmsg("Invalid Email or Password!!")
            return

        else:
            controller.show_frame(WelcomePage)
            ent_lst = []
            for key in ent:
                ent_lst.append(ent[key])
            reset_field(ent_lst)

    def match_det(self, dict_):
        lst = read_filejson()
        # print(dict_)
        for dict1 in lst:
            # print(dict1)
            if dict1['E-mail'] == dict_['E-mail']:
                if dict1['Password'] == dict_['Password']:
                    return 1
        return 0


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        rows = 0
        image = Image.open("bg3.gif")
        background_image = ImageTk.PhotoImage(image)
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        rows = 0
        while rows < 10:
            #     self.grid_rowconfigure(rows,weight=6)
            self.grid_columnconfigure(rows, weight=1)
            rows += 1

        button1 = ttk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=9)


def quit():
    app.destroy()


def reset_field(lst):
    for ent in lst:
        ent.delete(0, tk.END)


def popupmsg(msg):
    popup = Tk()

    def leavemini():
        popup.destroy()

    popup.wm_title("!")
    popup.iconbitmap("logo.ico")

    label = Label(popup, text=msg, font=("Verdana", 12, "bold"))
    label.pack(side="top", fill="x", pady=10)
    button1 = ttk.Button(popup, text="Okay", command=leavemini)
    button1.pack()

    popup.mainloop()


def cb_change(var1, ep1):
    if (var1.get()):
        ep1.config(show="")
    else:
        ep1.config(show="*")


def collect_ent(dict):
    dict_temp = {}
    for key in dict:
        dict_temp[key] = dict[key].get()
    return dict_temp


def read_filejson():
    lst = []
    fr = open("database.txt", "r")
    for line in fr:
        data = json.loads(line)
        # dict1 = data[0]
        # print(data[0])
        lst.append(data[0])
    fr.close()
    return lst


app = bookingApp()
app.geometry("1280x720")
app.mainloop()
