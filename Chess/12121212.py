from tkinter import *

window = Tk()

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

MenuBttn = Menubutton(frame, text="Колір дошки", relief=RAISED)

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()

Menu1 = Menu(MenuBttn, tearoff=0)

Menu1.add_checkbutton(label="Червоний", variable=Var1)
Menu1.add_checkbutton(label="коричневий", variable=Var2)
Menu1.add_checkbutton(label="синій", variable=Var3)
Menu1.add_checkbutton(label="зелений", variable=Var4)
Menu1.add_checkbutton(label="рожевий", variable=Var5)
Menu1.add_checkbutton(label="стандартний", variable=Var6)

MenuBttn["menu"] = Menu1

def create_board():
    start_x = 0
    start_y = 0
    width_cell = 75
    start_color = "white"
    for i in range(8):
        for j in range(8):
            canvas.create_rectangle(start_x, start_y, start_x + width_cell, start_y + width_cell, fill=start_color)
            start_x = start_x + width_cell
            if start_color == "white":
                start_color = "black"
            else:
                start_color = "white"
        start_y = start_y + width_cell
        start_x = 0
        if start_color == "white":
            start_color = "black"
        else:
            start_color = "white"


is_figure_selected = False
figure_to_move = ""


def l_mouse_button_click(event):
    global figure_to_move
    global is_figure_selected
    if is_figure_selected:
        is_figure_selected = False
    else:
        is_figure_selected = True


canvas = Canvas(window, width=600, height=600)
canvas.pack()

create_board()

window.bind("<Button-1>", l_mouse_button_click)
MenuBttn.pack()

window.mainloop()