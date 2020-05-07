from tkinter import *

root = Tk()
root.geometry("250x380")

root.title("大爷的计算器")

frame_show = Frame(width=300, height=150, bg='#dddddd')

sv = StringVar()
sv.set('0')

show_label = Label(frame_show, textvariable=sv, bg='green', width=12, height=1, font=("黑体", 20, 'bold'), justify=LEFT,
                   anchor='e')
show_label.pack(padx=10, pady=10)

frame_show.pack()

frame_bord = Frame(width=400, height=350, bg='#cccccc')

num1 = ""
num2 = ""
operator = ""


def delete():
    global num1, num2, operator
    if not operator:
        num1 = num1[:-1]
        sv.set(num1)
    else:
        num2 = num2[:-1]
        sv.set(num1 + operator + num2)


def clear_all():
    global num1, num2, operator
    sv.set('0')
    num1 = ""
    num2 = ""
    operator = ""


def clear():
    global num1, num2, operator
    if not operator:
        sv.set('0')
        num1 = ""
        num2 = ""
        operator = ""
    else:
        num2 = ""
        sv.set(num1 + operator )


def fan():
    global num1, num2, operator
    if not operator:
        num1 = float(num1) * (-1)
        num1 = str(num1)
        sv.set(num1)
    else:
        num2 = float(num2) * (-1)
        num2 = str(num2)
        sv.set(num1 + operator + '(' + num2 + ')' )


def bai():
    global num1, num2, operator
    if not operator:
        num1 = float(num1) * 0.01
        num1 = str(num1)
        sv.set(num1)
    else:
        num2 = float(num2) * 0.01
        num2 = str(num2)
        sv.set(num1 + operator + num2)


Button(frame_bord, text='←', width=5, height=1, command=delete).grid(row=0, column=0)
Button(frame_bord, text='C', width=5, height=1, command=clear_all).grid(row=0, column=1)
Button(frame_bord, text='±', width=5, height=1, command=fan).grid(row=0, column=2)
Button(frame_bord, text='CE', width=5, height=1, command=clear).grid(row=0, column=3)


def change(num):
    global num1, num2, operator
    if not operator:
        num1 = num1 + num
        sv.set(num1)
    else:
        num2 = num2 + num
        sv.set(num1 + operator + num2)


def operation(op):
    global operator
    rst = 0
    if op in ['+', '-', 'x', '/']:
        operator = op
        sv.set(num1+operator)
    else:
        if operator == '+':
            rst = float(num1) + float(num2)
        elif operator == '-':
            rst = float(num1) - float(num2)
        elif operator == 'x':
            rst = float(num1) * float(num2)
        elif operator == '/':
            rst = float(num1) / float(num2)
        sv.set(str(rst))


Button(frame_bord, text='1', width=5, height=2, command=lambda: change("1")).grid(row=1, column=0)
Button(frame_bord, text='2', width=5, height=2, command=lambda: change("2")).grid(row=1, column=1)
Button(frame_bord, text='3', width=5, height=2, command=lambda: change("3")).grid(row=1, column=2)
Button(frame_bord, text='4', width=5, height=2, command=lambda: change("4")).grid(row=2, column=0)
Button(frame_bord, text='5', width=5, height=2, command=lambda: change("5")).grid(row=2, column=1)
Button(frame_bord, text='6', width=5, height=2, command=lambda: change("6")).grid(row=2, column=2)
Button(frame_bord, text='7', width=5, height=2, command=lambda: change("7")).grid(row=3, column=0)
Button(frame_bord, text='8', width=5, height=2, command=lambda: change("8")).grid(row=3, column=1)
Button(frame_bord, text='9', width=5, height=2, command=lambda: change("9")).grid(row=3, column=2)
Button(frame_bord, text='0', width=5, height=2, command=lambda: change("0")).grid(row=4, column=1)

Button(frame_bord, text='+', width=5, height=2, command=lambda: operation('+')).grid(row=1, column=3)
Button(frame_bord, text='-', width=5, height=2, command=lambda: operation('-')).grid(row=2, column=3)
Button(frame_bord, text='x', width=5, height=2, command=lambda: operation('x')).grid(row=3, column=3)
Button(frame_bord, text='/', width=5, height=2, command=lambda: operation('/')).grid(row=4, column=3)

Button(frame_bord, text='=', width=5, height=2, command=lambda: operation("=")).grid(row=4, column=2)

Button(frame_bord, text='%', width=5, height=2, command=bai).grid(row=4, column=0)

frame_bord.pack(padx=10, pady=10)

root.mainloop()
