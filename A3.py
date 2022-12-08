from tkinter import *

""""-------------------------------------------------------------
Vertices and edges GUI tool
File: A3.py
Author: Merle Crutchfield
Purpose: This is a GUI program that allows the user to middle
click to create a vertex, right click to change the color, and
then middle click two different vertices to draw a straight
edge between the two. It saves all of the vertex locations and
each other vertex they are connected to in a dictionary called
vert_dict.
--------------------------------------------------------------"""

# Important global variables
vert_center_list = []
vert_dict = {}
action = False
action_loc = [-50, -50]
colors = ["red", "green", "blue", "yellow", "white"]
colors_index = 0
lines_list = []


def drawOval(event):
    '''
    This function draws the oval when the middle
    click is pressed. It also adds the center of
    the circle coordinates to a list, as well as
    a dicationary.
    '''
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x + 50, y + 50, outline="#000", fill="#fff", width=2)
    vert_center_list.append([x+25, y+25])
    if not (x+25, y+25) in vert_dict:
        vert_dict[(x+25, y+25)] = []


def xy(event):
    '''
    This function is used for the left click to draw a line
    between two vertices. It checks to see if the click location
    is in the range of the vertex and then checks to see if another
    circle has been clicked. If both are true then it will add the
    line between the two.
    '''
    global lastx, lasty, action, action_loc
    lastx = event.x
    lasty = event.y
    for pos in vert_center_list:
        if lastx >= pos[0] - 25 and lastx <= pos[0] + 25 and lasty >= pos[1] - 25 and lasty <= pos[1] + 25:
            if not action:
                action = True
                action_loc = pos
            else:
                canvas.create_line(action_loc[0], action_loc[1], pos[0], pos[1], width=3)
                lines_list.append([action_loc[0], action_loc[1], pos[0], pos[1]])
                val_exists = False
                # Making sure not to readd positions to values
                for val in vert_dict[tuple(pos)]:
                    if action_loc == val:
                        val_exists = True
                if not val_exists:
                    vert_dict[tuple(action_loc)] += [[pos[0], pos[1]]]
                    vert_dict[(pos[0], pos[1])] += [action_loc]
                action = False
                # Uncomment if you want to check the dictionary :)
                print(vert_dict)


def changeColor(event):
    '''
    This function is used for the changing color option for
    the vertices. It cycles through a list of colors so that
    there are options to choose from.
    '''
    global lastx, lasty, action_loc, colors_index
    lastx = event.x
    lasty = event.y
    for pos in vert_center_list:
        if lastx >= pos[0] - 25 and lastx <= pos[0] + 25 and lasty >= pos[1] - 25 and lasty <= pos[1] + 25:
            canvas.create_oval(pos[0] - 25, pos[1] - 25, pos[0] + 25, pos[1] + 25, outline="#000", fill=colors[colors_index], width=2)
            if colors_index == 4:
                colors_index = 0
            else:
                colors_index += 1
                # Has to redraw lines to make it look pretty
            for line in lines_list:
                canvas.create_line(line[0], line[1], line[2], line[3], width=3)


#----------------------------------------------------------------------
# window and GUI widgets
root = Tk()
root.title("Vertices and Edges Tool")

#---- drawing canvas
canvas = Canvas(root, width=750, height=750)
canvas.bind("<Button-2>", drawOval)
canvas.bind("<Button-1>", xy)
canvas.bind("<Button-3>", changeColor)

# exit option
btn = Button(root, text = 'Click to exit', command = root.destroy)
btn.place(x=680, y=0)

canvas.grid(row=0, column=0)

#----------------------------------------------------------------------
# start main event loop
root.mainloop()