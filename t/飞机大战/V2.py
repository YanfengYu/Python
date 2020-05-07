import tkinter
import time
import random

step = 0
direction = (1, 1)

x = 0
y = 10


def set_right(e):
    global x
    x += 20


def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title('飞机大战')

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)

window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()



def main():
    bg_img_name = "./Images/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bg_img, tags='bg')

    sp_img_name = './Images/smallplane.gif'
    sp_img = tkinter.PhotoImage(file=sp_img_name)
    window_canvas.create_image(50, 50, anchor=tkinter.CENTER, image=sp_img, tags='sp')

    ap_move()
    tkinter.mainloop()

    # bee_img_name = "./Images/bee.gif"
    # bee_img = tkinter.PhotoImage(file=bee_img_name)
    # window_canvas.create_image(50, 50, anchor=tkinter.CENTER, image=bee_img, tags='bee')


def ap_move():
    global x
    global y
    global step

    y += 20
    print(x, y)
    window_canvas.move("sp", x, y)

    step += 1
    print(step)
    window_canvas.after(1000, ap_move)


if __name__ == '__main__':
    main()
