from tkinter import *
from tkinter import messagebox


def handel_button():
    email = email_input.get()
    password = password_input.get()
    if '@' in email and int or str in password:
        messagebox.showinfo('Login Sucessfully')
    else:
        messagebox.showerror('Invalid Input')


root = Tk()

root.geometry('300x500')
root.title('Login')

icon = PhotoImage(file='earth.png')

root.iconphoto(False, icon)

root.config(bg='gray')

text_label = Label(root, text='Login Form', bg='gray')
text_label.pack(pady=(50, 10))
text_label.config(font=('verdana', 30), highlightcolor='cyan')

email_label = Label(root, text='Email', bg='gray')
email_label.pack(pady=(50, 10))
email_label.config(font=('verdana', 15), highlightcolor='cyan')

email_input = Entry(root, width=30)
email_input.pack(pady=(0, 0), padx=(5, 5))

password_label = Label(root, text='Password', bg='gray')
password_label.pack(pady=(10, 10))
password_label.config(font=('verdana', 15), highlightcolor='cyan')

password_input = Entry(root, width=30)
password_input.pack(pady=(0, 0), padx=(5, 5))

login_btn = Button(root, text='Login Now', width=10, height=0, command=handel_button)
login_btn.pack(pady=(30, 10))
login_btn.config(font=('verdana', 12))

root.mainloop()
