""" File: battleship.py
    Author: Merle Crutchfield
    Purpose: This code is used to learn about classes and the relationship
    between multiple ones. We create three classes, the board, the ship,
    and the position class. The board is a 2D list that represents a board
    for playing the game battleship on. The ship class represents the ships
    being put on the board, and the position represents an x, y coordinate
    on the board. All together, functions within each class are used to
    add ships to the board, check if a spot has been used, try to move, some
    setters and getters, and print functions. NOTE: I use the word acronym
    but I believe the spec calls it the condition of the ship.
"""

class Board:
    def __init__(self, size):
        '''
        Constructs the Board object, first asserting the size input is valid.
        The grid is initialized as a 2D list of '.' empty. The ship_info and
        ships_list variables are not initialized until ships are added.
        '''
        assert size > 0
        self.size = size
        self.grid = []
        # Iterate through each spot on the board
        for i in range(0, size):
            line = []
            for j in range(0, size):
                line.append(".")
            self.grid.append(line)
        # Dictionary containing name of each ship as the key and the positions
        # as the values.
        self.ship_info = {}
        # List of each of the ships
        self.ships_list = []

    def get_size(self):
        ''' Getter for the ship size
        '''
        return self.size

    def add_ship(self, ship, position):
        '''
        Function that adds a ship to the board. It takes the ship argument
        as a Ship object and the position as a Position object. Adds ship
        to list, and then goes through each value in the ships shape which
        are coordinates. Runs assertions to make sure the position is  valid
        and then adds first letter to the board. Adds name and position info
        to the dictionary, then changes the x and y positions of the ship
        to the spot on the board, not just 0's, 1's and -1's.
        '''
        self.ships_list.append(ship)
        shapes = []
        # Iterate through coordinates
        for val in ship.get_shape():
            # Finds x and y coordinate on the board
            x_coord = val.get_x() + position.get_x()
            y_coord = val.get_y() + position.get_y()
            # Asserts valid positions
            assert x_coord >= 0 and x_coord < self.get_size()
            assert y_coord >= 0 and y_coord < self.get_size()
            # Assert spot hasn't been used yet
            assert self.grid[x_coord][y_coord] == "."
            # Changes grid spot
            self.grid[x_coord][y_coord] = ship.get_name()[0]
            # Adding coordinate to ship name dictionary
            if ship.get_name() in self.ship_info:
                self.ship_info[ship.get_name()].append([x_coord, y_coord])
            else:
                self.ship_info[ship.get_name()] = [[x_coord, y_coord]]
            # Adding coordinate to list to change corresponding spot on board
            shapes.append(Pos(x_coord, y_coord))
        ship.set_shape(shapes)

    def print(self):
        '''
        This function prints out the Board object. It first checks if the
        board size is above 10 so that the spacing can be done right. If
        it is above 10, then extra white spaces are added though if
        statements. It prints out the top and bottom parts based on the
        size, and then prints out the numbers of each index in the
        corresponding part.
        '''
        # Adds extra space at begining
        if self.get_size() > 10:
            print(" ", end="")
        # Prints out top of board
        print("  +-" + (2 * self.get_size() - 1) * "-" + "-+")
        # Prints out each spot of the grid
        for j in range(self.get_size() - 1, -1, -1):
            if self.get_size() > 10 and j < 10:
                print(" ", end="")
            print(str(j) + " | ", end="")
            for i in range(0, self.get_size()):
                print(self.grid[i][j] + " ", end="")
            print("|")
        if self.get_size() > 10:
            print(" ", end="")
        # Prints out bottom of board
        print("  +-" + (2 * self.get_size() - 1) * "-" + "-+")
        # Prints out the first index number if more than ten
        if self.get_size() > 10:
            print(" " * 25, end="")
            for i in range(10, self.get_size()):
                print(str(i)[0], end=" ")
            print()
        print("    ", end="")
        if self.get_size() > 10:
            print(" ", end="")
        # Prints out the last index number always
        for i in range(0, self.get_size()):
            print(str(i)[-1], end=" ")
        print()

    def has_been_used(self, pos):
        '''
        This function checks a position on the board to see if
        it has been shot at before. It checks the position on
        the grid to see if it has been shot at before as spots
        that have been shot at will either be missed, partially
        sunk, or sunk.
        '''
        if self.grid[pos.get_x()][pos.get_y()] in "o*X":
            return True
        return False

    def attempt_move(self, pos):
        '''
        This function attempts to shoot at a spot on the board. It
        takes the position argument as a Pos object, and returns
        the string of the result. It runs assertions to make sure
        the spot was valid, and then checks the grid to see if it
        is a '.' meaning there is no ship there. Then, it goes
        through and checks if the shot that hit sunk the ship. If
        it did then it returns 'Sunk' but if not then it returns
        'Hit'.
        '''
        # Asserts valid spot and hasn't been shot at before
        assert pos.get_x() >= 0 and pos.get_x() < self.get_size()
        assert pos.get_y() >= 0 and pos.get_y() < self.get_size()
        assert not self.has_been_used(pos)
        # Checking miss condition
        if self.grid[pos.get_x()][pos.get_y()] in ".":
            self.grid[pos.get_x()][pos.get_y()] = "o"
            return 'Miss'
        # Hit condition
        else:
            fully_sunk = True
            self.grid[pos.get_x()][pos.get_y()] = "*"
            # Finding the ship in dictionary for coordinates
            for key in self.ship_info:
                if [pos.get_x(), pos.get_y()] in self.ship_info[key]:
                    name = key
            # Changing ship acronym for hit parts
            for ship in self.ships_list:
                if ship.get_name() == name:
                    for i in range(0, len(ship.get_shape())):
                        if (pos.get_x(), pos.get_y()) == (
                              ship.get_shape()[i].get_x(),
                              ship.get_shape()[i].get_y()):
                            ship.acronym[i] = "*"
            # Checking to see if ship is fully sunk
            for coord in self.ship_info[name]:
                if self.grid[coord[0]][coord[1]] == name[0]:
                    fully_sunk = False
            # Fully sinking ship with 'X' and returning sunk
            if fully_sunk:
                for coord in self.ship_info[name]:
                    self.grid[coord[0]][coord[1]] = "X"
                return 'Sunk (' + name + ')'
            # Returning hit
            else:
                return 'Hit'


class Ship:
    def __init__(self, name, shape):
        '''
        Constructs the Ship object. It is made with a string for the
        name and the shape being a list of Position objects. It also
        contains acronym which is the first letter the length of the
        ship for printing out the current state of the ship. Acronym
        changes as the ship gets hit.
        '''
        self.name = name
        self.shape = shape
        self.acronym = []
        for i in range(0, len(self.get_shape())):
            self.acronym.append(self.get_name()[0])

    def get_shape(self):
        ''' Returns the shape of the ship (Getter).
        '''
        return self.shape

    def set_shape(self, shape):
        ''' Sets the shape of the ship (Setter).
        '''
        self.shape = shape

    def get_name(self):
        ''' Returns the name of the ship (Getter).
        '''
        return self.name

    def is_sunk(self):
        '''
        Returns True if the ship is sunk and False if not. This function
        goes through the acronym and checks if the spot is not '*',
        meaning it was not hit. If not, then the ship was not sunk and
        so it returns False.
        '''
        # Iterates through each spot
        for spot in self.acronym:
            if spot != "*":
                return False
        return True

    def print(self):
        '''
        Prints out the ship acronym and the ship's name. It uses a loop
        to add the values in the acronym list to a string, and then
        figures out how many spaces are needed for the spacing. It then
        prints out the info.
        '''
        current = ""
        # Adds list values to a string
        for val in self.acronym:
            current += val
        # Gets spaces to make it to 10 spots
        spaces = 10 - len(current)
        # Prints out information
        print(current + (" " * spaces) + self.name)


class Pos:
    def __init__(self, x, y):
        '''
        Constructs the Pos object. The two parameters passed are x and
        y coordinates. They are used to represent spots on the board
        that the ship parts go to. The rotate function rotates the ship
        in values of 90 degrees.
        '''
        self.x = x
        self.y = y

    def get_x(self):
        ''' Returns the x value (Getter).
        '''
        return self.x

    def get_y(self):
        ''' Returns the y value (Getter)
        '''
        return self.y

    def rotate(self, rot):
        '''
        Function that rotates the position. It first asserts that the input
        is between 0 and 3. It checks if 0 to return the same object. If 1
        then it rotates by 90 degrees, 2 then 180 degrees, and 3 by 270
        degrees.
        '''
        # Asserts valid input
        assert rot >= 0 and rot <= 3
        # Rotates by 0 degrees
        if rot == 0:
            return self
        # Rotates by 90 degrees
        elif rot == 1:
            self.x, self.y = self.y, (-1 * self.x)
            return self
        # Rotates by 180 degrees
        elif rot == 2:
            self.x, self.y = (-1 * self.x), (-1 * self.y)
            return self
        # Rotates by 270 degrees
        else:
            self.x, self.y = (-1 * self.y), self.x
            return self
