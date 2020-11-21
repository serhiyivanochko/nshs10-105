from tkinter import *

window = Tk()

def show_possible_step(rect, figure_type):
    global rect_x
    global rect_y
    rect["tag"]

    if figure_type == "rook":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x, rect_y - 75, rect_x + 75, rect_y - 150, fill="green")
        canvas.create_oval(rect_x, rect_y - 150, rect_x + 75, rect_y - 225, fill="green")
        canvas.create_oval(rect_x, rect_y - 225, rect_x + 75, rect_y - 300, fill="green")
        canvas.create_oval(rect_x, rect_y - 300, rect_x + 75, rect_y - 375, fill="green")
        canvas.create_oval(rect_x, rect_y - 375, rect_x + 75, rect_y - 450, fill="green")
        canvas.create_oval(rect_x, rect_y - 450, rect_x + 75, rect_y - 525, fill="green")
        canvas.create_oval(rect_x, rect_y - 525, rect_x + 75, rect_y - 150, fill="green")

        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y, rect_x + 150, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y, rect_x + 225, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 225, rect_y, rect_x + 300, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 300, rect_y, rect_x + 375, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 375, rect_y, rect_x + 450, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 450, rect_y, rect_x + 525, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 525, rect_y, rect_x + 600, rect_y - 75, fill="green")

    if figure_type == "khight":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y - 150, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y - 150, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y + 150, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y + 150, rect_x + 75, rect_y - 75, fill="green")


    if figure_type == "bishop":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y - 75, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y - 150, rect_x + 150, rect_y - 150, fill="green")
        canvas.create_oval(rect_x + 225, rect_y - 225, rect_x + 225, rect_y - 225, fill="green")
        canvas.create_oval(rect_x + 300, rect_y - 300, rect_x + 300, rect_y - 300, fill="green")
        canvas.create_oval(rect_x + 375, rect_y - 375, rect_x + 375, rect_y - 375, fill="green")
        canvas.create_oval(rect_x + 450, rect_y - 450, rect_x + 450, rect_y - 450, fill="green")

        canvas.create_oval(rect_x - 75, rect_y - 75, rect_x - 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 150, rect_y - 150, rect_x - 150, rect_y - 150, fill="green")
        canvas.create_oval(rect_x - 225, rect_y - 225, rect_x - 225, rect_y - 225, fill="green")
        canvas.create_oval(rect_x - 300, rect_y - 300, rect_x - 300, rect_y - 300, fill="green")
        canvas.create_oval(rect_x - 375, rect_y - 375, rect_x - 375, rect_y - 375, fill="green")
        canvas.create_oval(rect_x - 450, rect_y - 450, rect_x - 450, rect_y - 450, fill="green")

        canvas.create_oval(rect_x - 75, rect_y + 75, rect_x - 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x - 150, rect_y + 150, rect_x - 150, rect_y + 150, fill="green")
        canvas.create_oval(rect_x - 225, rect_y + 225, rect_x - 225, rect_y + 225, fill="green")
        canvas.create_oval(rect_x - 300, rect_y + 300, rect_x - 300, rect_y + 300, fill="green")
        canvas.create_oval(rect_x - 375, rect_y + 375, rect_x - 375, rect_y + 375, fill="green")
        canvas.create_oval(rect_x - 450, rect_y + 450, rect_x - 450, rect_y + 450, fill="green")

        canvas.create_oval(rect_x + 75, rect_y + 75, rect_x + 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y + 150, rect_x + 150, rect_y + 150, fill="green")
        canvas.create_oval(rect_x + 225, rect_y + 225, rect_x + 225, rect_y + 225, fill="green")
        canvas.create_oval(rect_x + 300, rect_y + 300, rect_x + 300, rect_y + 300, fill="green")
        canvas.create_oval(rect_x + 375, rect_y + 375, rect_x + 375, rect_y + 375, fill="green")
        canvas.create_oval(rect_x + 450, rect_y + 450, rect_x + 450, rect_y + 450, fill="green")


    if figure_type == "pawns":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x, rect_y - 75, rect_x, rect_y - 75, fill="green")
        canvas.create_oval(rect_x, rect_y - 150, rect_x, rect_y - 75, fill="green")


    if figure_type == "king":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y - 75, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y + 75, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y + 75, rect_x + 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y - 75, rect_x - 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y - 75, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y - 75, rect_x - 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 75, rect_y + 75, rect_x - 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y + 75, rect_x + 75, rect_y + 75, fill="green")


    if figure_type == "gueen":
        canvas.coords(rect)
        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x, rect_y - 75, rect_x + 75, rect_y - 150, fill="green")
        canvas.create_oval(rect_x, rect_y - 150, rect_x + 75, rect_y - 225, fill="green")
        canvas.create_oval(rect_x, rect_y - 225, rect_x + 75, rect_y - 300, fill="green")
        canvas.create_oval(rect_x, rect_y - 300, rect_x + 75, rect_y - 375, fill="green")
        canvas.create_oval(rect_x, rect_y - 375, rect_x + 75, rect_y - 450, fill="green")
        canvas.create_oval(rect_x, rect_y - 450, rect_x + 75, rect_y - 525, fill="green")
        canvas.create_oval(rect_x, rect_y - 525, rect_x + 75, rect_y - 150, fill="green")

        canvas.create_oval(rect_x, rect_y, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 75, rect_y, rect_x + 150, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y, rect_x + 225, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 225, rect_y, rect_x + 300, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 300, rect_y, rect_x + 375, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 375, rect_y, rect_x + 450, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 450, rect_y, rect_x + 525, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 525, rect_y, rect_x + 600, rect_y - 75, fill="green")

        canvas.create_oval(rect_x + 75, rect_y - 75, rect_x + 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y - 150, rect_x + 150, rect_y - 150, fill="green")
        canvas.create_oval(rect_x + 225, rect_y - 225, rect_x + 225, rect_y - 225, fill="green")
        canvas.create_oval(rect_x + 300, rect_y - 300, rect_x + 300, rect_y - 300, fill="green")
        canvas.create_oval(rect_x + 375, rect_y - 375, rect_x + 375, rect_y - 375, fill="green")
        canvas.create_oval(rect_x + 450, rect_y - 450, rect_x + 450, rect_y - 450, fill="green")

        canvas.create_oval(rect_x - 75, rect_y - 75, rect_x - 75, rect_y - 75, fill="green")
        canvas.create_oval(rect_x - 150, rect_y - 150, rect_x - 150, rect_y - 150, fill="green")
        canvas.create_oval(rect_x - 225, rect_y - 225, rect_x - 225, rect_y - 225, fill="green")
        canvas.create_oval(rect_x - 300, rect_y - 300, rect_x - 300, rect_y - 300, fill="green")
        canvas.create_oval(rect_x - 375, rect_y - 375, rect_x - 375, rect_y - 375, fill="green")
        canvas.create_oval(rect_x - 450, rect_y - 450, rect_x - 450, rect_y - 450, fill="green")

        canvas.create_oval(rect_x - 75, rect_y + 75, rect_x - 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x - 150, rect_y + 150, rect_x - 150, rect_y + 150, fill="green")
        canvas.create_oval(rect_x - 225, rect_y + 225, rect_x - 225, rect_y + 225, fill="green")
        canvas.create_oval(rect_x - 300, rect_y + 300, rect_x - 300, rect_y + 300, fill="green")
        canvas.create_oval(rect_x - 375, rect_y + 375, rect_x - 375, rect_y + 375, fill="green")
        canvas.create_oval(rect_x - 450, rect_y + 450, rect_x - 450, rect_y + 450, fill="green")

        canvas.create_oval(rect_x + 75, rect_y + 75, rect_x + 75, rect_y + 75, fill="green")
        canvas.create_oval(rect_x + 150, rect_y + 150, rect_x + 150, rect_y + 150, fill="green")
        canvas.create_oval(rect_x + 225, rect_y + 225, rect_x + 225, rect_y + 225, fill="green")
        canvas.create_oval(rect_x + 300, rect_y + 300, rect_x + 300, rect_y + 300, fill="green")
        canvas.create_oval(rect_x + 375, rect_y + 375, rect_x + 375, rect_y + 375, fill="green")
        canvas.create_oval(rect_x + 450, rect_y + 450, rect_x + 450, rect_y + 450, fill="green")





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
        # Here add call to your func
        is_figure_selected = False
    else:
        # Next row should be in any 'if' condition after setting rectangle which will be used for move
        is_figure_selected = True


canvas = Canvas(window, width=600, height=600)
canvas.pack()

create_board()

window.bind("<Button-1>", l_mouse_button_click)

window.mainloop()
