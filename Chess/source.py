from tkinter import *

window = Tk()
delta = 25


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
list_possible_steps = []


"""def show_steps(figure, name):
    if name == "bishop":
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
                step = canvas.create_oval((number_cell * 75) + delta, i * 75 + delta, ((number_cell + 1) * 75) - delta, ((i + 1) * 75) - delta, fill="green")
                list_possible_steps.append(step)"""


def move(figure, name, new_x, new_y):
    if name == "bishop":
        new_row_number = int(new_y / 75)
        new_cell_number = int(new_x / 75)
        print("Row: " + str(new_row_number) + ", Cell: " + str(new_cell_number))
        canvas.coords(figure, new_cell_number * 75 + delta, new_row_number * 75 + delta,
                      (new_cell_number + 1) * 75 - delta, (new_row_number + 1) * 75 - delta)


def clean_steps():
    global list_possible_steps
    iterator = len(list_possible_steps) - 1
    while len(list_possible_steps) > 0:
        canvas.delete(list_possible_steps[iterator])
        list_possible_steps.remove(list_possible_steps[iterator])
        iterator = iterator - 1


def l_mouse_button_click(event):
    global figure_to_move
    global is_figure_selected
    if is_figure_selected:
        move(figure_to_move, "bishop", event.x, event.y)
        clean_steps()
        is_figure_selected = False
    else:
        figures = []
        figures.append(bishop1)
        figures.append(bishop2)
        figures.append(bishop3)
        figures.append(bishop4)

        for i in range(len(figures)):
            figure_coords = canvas.coords(figures[i])
            if event.x > figure_coords[0] and event.x < figure_coords[2] and event.y > figure_coords[1] and event.y < figure_coords[3]:
                figure_to_move = figures[i]
                show_steps(figure_to_move, "bishop")
            is_figure_selected = True


canvas = Canvas(window, width=600, height=600)
canvas.pack()
create_board()

bishop1 = canvas.create_rectangle(150 + delta, 525 + delta, 225 - delta, 600 - delta, tag="bishopBL", fill="red")
bishop2 = canvas.create_rectangle(375 + delta, 525 + delta, 450 - delta, 600 - delta, tag="bishopBL", fill="red")
bishop3 = canvas.create_rectangle(150 + delta, 0 + delta, 225 - delta, 75 - delta, tag="bishopBL", fill="red")
bishop4 = canvas.create_rectangle(375 + delta, 0 + delta, 450 - delta, 75 - delta, tag="bishopBL", fill="red")

window.bind("<Button-1>", l_mouse_button_click)
window.mainloop()