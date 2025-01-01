from tkinter import *
from mains import Face_Recognition_System


root = Tk()
root.title('LOGIN')
root.geometry("999x590+0+0")
root.configure(bg='blue')
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        new_window = Toplevel(root)
        app = Face_Recognition_System(new_window)


frame = Frame(root, width=350, height=350, bg='skyblue')
frame.place(x=350, y=70)

heading = Label(frame, text='sign in', fg='#57a1f8', bg='white', font=("Microsoft Yahei UI Light", 23, 'bold'))
heading.place(x=100, y=5)

def on_enter_username(e):
    user.delete(0, END)
def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, "username")

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

def on_enter_password(e):
    code.delete(0, END)
def on_leave_password(e):
    name = code.get()
    if name == '':
        code.insert(0, "password")

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', fg='#57a1f8', bg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account", fg='black', bg='White', font=("Microsoft Yahei UI Light", 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign in', fg='#57a1f8', bg='white', border=0, cursor='hand2')
sign_up.place(x=215, y=270)

root.mainloop()
