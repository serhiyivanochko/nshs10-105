from tkinter import *

window = Tk()
delta = 25

is_figure_selected = False
figure_to_move = ""
list_possible_steps = []


def show_steps(figure, name):
    if name == "rook":
        figures = canvas.coords(figure)
        number_row = int(figures[1] / 75)
        number_cell = int(figures[0] / 75)
        # print("Row: " + str(number_row) + ", Cell: " + str(number_cell))
        for i in range(8):
            if i != number_cell:
                step = canvas.create_oval(i * 75 + delta, (number_row / 75) + delta, ((i + 1) * 75) - delta,
                                          ((number_row + 1) / 75) - delta, fill="green")
                list_possible_steps.append(step)
        for i in range(8):
            if i != number_row:
                step = canvas.create_oval((number_cell * 75) + delta, i * 75 + delta, ((number_cell + 1) * 75) - delta,
                                          ((i + 1) * 75) - delta, fill="green")
                list_possible_steps.append(step)

    if name == "khight":
        figures = canvas.coords(figure)
        number_row = int(figures[1] / 75)
        number_cell = int(figures[0] / 75)
        # print("Row: " + str(number_row) + ", Cell: " + str(number_cell))
        for i in range(8):
            if i != number_cell:
                step = canvas.create_oval(i * 75 + delta, (number_row * 75) + delta, ((i + 1) * 75) - delta,
                                          ((number_row + 1) * 75) - delta, fill="green")
                list_possible_steps.append(step)
        for i in range(8):
            if i != number_row:
                step = canvas.create_oval((number_cell * 75) + delta, i * 75 + delta, ((number_cell + 1) * 75) - delta,
                                          ((i + 1) * 75) - delta, fill="green")
                list_possible_steps.append(step)



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
