from tkinter import *
 window = Tk()
 
canvas = Canvas(window, width = 600, height = 600)
canvas.pack()

startx = 0
starty = 0
widthCell = 75
startColor = "white"
for i in range(8):
    for j in range(8):
        canvas.create_rectangle(startx, starty, startx + widthCell, starty + widthCell, fill = startColor)
        if startColor == "white":if startColor == "white":
            startColor = "black"
        else:
             startColor = "white"    
            startColor = "black"
        else:
             startColor = "white"  
    if startColor == "white":
            startColor = "black"
        else:
             startColor = "white"               
window.mainloop()
