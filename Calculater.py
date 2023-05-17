from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('300x500')
root.resizable(0, 0)
result_label = Label(root, text='', bg='white', fg='black')
result_label.grid(row=0, column=0, pady=(50, 20), sticky='w', columnspan=5)
result_label.configure(font=('verdana', 40, 'bold'))

button_7 = Button(root, text='7', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(7))
button_7.grid(row=2, column=0)
button_7.configure(font=('verdana', 20))

button_8 = Button(root, text='8', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(8))
button_8.grid(row=2, column=2)
button_8.configure(font=('verdana', 20))

button_9 = Button(root, text='9', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(9))
button_9.grid(row=2, column=3)
button_9.configure(font=('verdana', 20))

button_add = Button(root, text='+', bg='white', fg='black', width=4, height=0, command=lambda: get_operator('+'))
button_add.grid(row=2, column=4)
button_add.configure(font=('verdana', 20))

button_4 = Button(root, text='4', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(4))
button_4.grid(row=3, column=0)
button_4.configure(font=('verdana', 20))

button_5 = Button(root, text='5', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(5))
button_5.grid(row=3, column=2)
button_5.configure(font=('verdana', 20))

button_6 = Button(root, text='6', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(6))
button_6.grid(row=3, column=3)
button_6.configure(font=('verdana', 20))

button_sub = Button(root, text='-', bg='white', fg='black', width=4, height=0, command=lambda: get_operator('-'))
button_sub.grid(row=3, column=4)
button_sub.configure(font=('verdana', 20))

button_1 = Button(root, text='1', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(1))
button_1.grid(row=4, column=0)
button_1.configure(font=('verdana', 20))

button_2 = Button(root, text='2', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(2))
button_2.grid(row=4, column=2)
button_2.configure(font=('verdana', 20))

button_3 = Button(root, text='3', bg='white', fg='black', width=4, height=0, command=lambda: get_digit(3))
button_3.grid(row=4, column=3)
button_3.configure(font=('verdana', 20))

button_mul = Button(root, text='*', bg='white', fg='black', width=4, height=0, command=lambda: get_operator('*'))
button_mul.grid(row=4, column=4)
button_mul.configure(font=('verdana', 20))

button_div = Button(root, text='/', bg='white', fg='black', width=4, height=0, command=lambda: get_operator('/'))
button_div.grid(row=5, column=4)
button_div.configure(font=('verdana', 20))

button_result = Button(root, text='=', bg='white', fg='black', width=4, height=0)
button_result.grid(row=5, column=2)
button_result.configure(font=('verdana', 20))

button_clear = Button(root, text='C', bg='white', fg='black', width=4, height=0, command=lambda: clear())
button_clear.grid(row=5, column=3)
button_clear.configure(font=('verdana', 20))

first_number = second_number = operator = None


def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')


def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number,2)))


root.mainloop()
