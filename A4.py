from tkinter import *
""""-------------------------------------------------------------
The Guess the Number Game
File: A4.py
Author: Merle Crutchfield
Purpose: This is a view of the vertices graph as well as
display data from a vertices graph tool. The user can choose
if they want to display the graphical version, which shows
the vertices and their edges, or if they want to see information
about them such as their name, temp, and hours since last
replaced. It is structured in an MVC model.
--------------------------------------------------------------"""

# Fake data so we have values to draw
vertices = [('first', 100, 250), ('second', 90, 225), ('third', 93, 210), ('fourth', 56, 180),
            ('fifth', 111, 160), ('sixth', 122, 140), ('seventh', 49, 124), ('eighth', 132, 110),
            ('ninth', 87, 96), ('tenth', 21, 80)]
vertices_info = {(167, 170): [[405, 169]], (491, 320): [[405, 169], [584, 510], [346, 502]],
                (405, 169): [[570, 214], [491, 320], [328, 268], [167, 170]], (180, 370):
                [[328, 268], [299, 402], [163, 546], [346, 502]], (328, 268): [[405, 169],
                [180, 370], [299, 402]], (346, 502): [[299, 402], [491, 320], [163, 546],
                [180, 370]], (584, 510): [[491, 320]], (163, 546): [[299, 402], [180, 370],
                [346, 502]], (299, 402): [[328, 268], [346, 502], [163, 546], [180, 370]],
                (570, 214): [[405, 169]]}
colors = ['red', 'red', 'blue', 'yellow', 'yellow', 'green', 'orange', 'green', 'blue', 'orange']

#----------------------------------------------------------------------
# Model - the data we want to view and control
#----------------------------------------------------------------------
class Model:
    def __init__(self):
        self.view = None
        self._vertices = []
        self._vertices_info = {}

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_vertices_info(self):
        return self._vertices_info

    def set_vertices_info(self, vertices_info):
        self._vertices = vertices_info

    def set_view(self, view):
        self.view = view

#----------------------------------------------------------------------
# View - a frame in the root window and the GUI widgets
#----------------------------------------------------------------------
class View(Canvas):
    def __init__(self, canvas, w, h):
        super().__init__(root, width=w, height=h)

        self.model = None
        self.controller = None

        btn = Button(self, text = 'Click to exit', command = root.destroy)
        btn2 = Button(self, text='GUI View', command = self.draw_graph)
        btn3 = Button(self, text='Data View', command = self.show_data)
        btn.place(x=650, y=0)
        btn2.place(x=0, y=0)
        btn3.place(x=75, y=0)

    def set_model(self, model):
        self.model = model

    def set_controller(self, controller):
        self.controller = controller

    def draw_graph(self):
        index = 0
        self.delete("all")
        for key in vertices_info.keys():
            self.create_oval(key[0] - 25, key[1] - 25, key[0] + 25, key[1] + 25, outline="#000", fill=colors[index], width=2)
            for val in vertices_info[key]:
                self.create_line(key[0], key[1], val[0], val[1], width=3)
            index += 1

    def show_data(self):
        index = 150
        self.delete("all")
        self.create_text(250, 100, text = '\tName\tTemp (Degrees F)\tHours Since Last Replaced', font=('30'))
        for val in vertices:
            string = val[0] + '\t\t' + str(val[1]) + '\t\t' + str(val[2])
            self.create_text(250, index, text=string, font=('30'))
            index += 50


#----------------------------------------------------------------------
# Controller
#----------------------------------------------------------------------
class Controller:
    def __init__(self):
        self.model = None

    def set_model(self, model):
        self.model = model

#----------------------------------------------------------------------
# App - the root window and the MVC objects
#----------------------------------------------------------------------
class App():
    def __init__(self):
        global root
        root = Tk()
        root.title("Vertices and Edges Tool")

        #---- drawing canvas
        #canvas = Canvas(root, width=750, height=750)
        model = Model()

        #---- drawing canvas
        view = View(root, 750, 750)
        view.grid(row=0, column=0)
        #---- create a controller
        controller = Controller()
        # set the model for the controller
        controller.set_model(model)
        # set the controller for the view
        view.set_controller(controller)

    def mainloop(self):
        root.mainloop()

#=========================================================================

app = App()
app.mainloop()