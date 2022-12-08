###
### Merle Crutchfield
### This code creates the game of one dimensional chess, both in the command
### line and as a visual graphic. Each side has a king and two knights, the
### king moving as far left or right and will only stop at an edge or to take
### a piece, and the knights that move two spaces left or right. The game is
### won by one side taking the opposing sides king. There were several
### functions that we had to create as they were already called in the main
### function. This code uses several global variables for convenience, and
### graphics for the visual game to be shown in life action.
###

from graphics import graphics

W_KNIGHT = "WKn"
W_KING   = "WKi"
B_KNIGHT = "BKn"
B_KING   = "BKi"
EMPTY    = "   "
WHITE    = "White"
BLACK    = "Black"
LEFT     = "l"
RIGHT    = "r"


def is_valid_move(board, position, player):
    """
    This function checks to make sure that the move the user entered is valid.
    If it is, then it will return true, and if it isn't, it will return false.
    It uses the board as input to see the locations of the pieces, the player
    to know whose turn it is, and the position that they enter to check if
    their piece is there. It returns a boolean operator once it passes several
    if statements.
    """
    if (position >= 9 or position < 0):
        return False

    if (board[position] == EMPTY):
        return False

    if (player == WHITE):
        if (board[position] != W_KNIGHT and board[position] != W_KING):
            return False

    if (player == BLACK):
        if (board[position] != B_KNIGHT and board[position] != B_KING):
            return False
    return True

def move_knight(board, position, direction):
    """
    This function takes in the board to know the order of where each piece is,
    the position that the user entered, and the direction it will go in. It
    checks the direction to see if their move is to the left or right, and
    from there will make sure the position it will end in is not out of bounds.
    It uses several if statements to see both the direction, and the location,
    and doesn't print out anything but alters the board list. It also is only
    used to move the black and white knights.
    """
    if (direction == RIGHT):
        if (position + 2 <= 8):
            board[position + 2] = board[position]
            board[position] = EMPTY

    if (direction == LEFT):
        if (position - 2 >= 0):
            board[position - 2] = board[position]
            board[position] = EMPTY

def move_king(board, position, direction):
    """
    This function is very similar to the move_knight function, but is used for
    kings. It has the same inputs of the board list, the position entered by
    the user, and the direction the king should move in. This function uses if
    statements, along with while loops to make sure that there is no out of
    bounds error and that the kings will move the correct amount. The king will
    move as far as possible until either it takes a piece or hits a wall. There
    is nothing printed out, but the board list is altered.
    """
    if (direction == RIGHT):
        end = False
        dis = position + 1
        while dis <= 8 and not end:
            if (board[dis] == EMPTY and dis != 8):
                dis += 1
            else:
                board[dis] = board[position]
                board[position] = EMPTY
                end = True
    else:
        end = False
        dis = position - 1
        while dis >= 0 and not end:
            if (board[dis] == EMPTY and dis != 0):
                dis -= 1
            else:
                board[dis] = board[position]
                board[position] = EMPTY
                end = True

def print_board(board):
    """
    This function only takes in the board as an input, and will print out the
    resulting board in the command line. It prints out the top and bottom
    lines as a constant length, and will print out line dividers with the
    correctly stored pieces in place. It prints them out in order between the
    two lines and in the correct order.
    """
    print("+-----------------------------------------------------+")
    print(
        "| "
        + board[0]
        + " | "
        + board[1]
        + " | "
        + board[2]
        + " | "
        + board[3]
        + " | "
        + board[4]
        + " | "
        + board[5]
        + " | "
        + board[6]
        + " | "
        + board[7]
        + " | "
        + board[8]
        + ' |'
    )
    print("+-----------------------------------------------------+")


def draw_board(board, gui):
    """
    This function is used to draw the chess board in real time after each
    move. It first uses the gui as the already defined canvas, and uses
    graphics.py to call specific functions to print out various parts.
    For example, it will print out 1 Dimensional Chess at the top in green,
    then draw a red rectangle with 9 black squares that get filled with the
    corresponding values from the board list. It uses if statements to see
    which piece needs to be displayed, and then checks which color it should
    be.
    """
    gui.text(200, 25, '1 Dimensional Chess', 'darkgreen', 25)
    gui.rectangle(50, 100, 630, 70, 'red')
    gui.line(50, 100, 680, 100, 'black')
    gui.line(50, 170, 680, 170, 'black')
    i = 50
    j = 0
    while (i <= 680):
        gui.line(i, 100, i, 170, 'black')
        if (j < 9):
            if (board[j] == W_KING):
                gui.text(i+5, 125, 'king', 'white', 20)
            elif (board[j] == W_KNIGHT):
                gui.text(i+5, 125, 'knight', 'white', 20)
            elif (board[j] == B_KING):
                gui.text(i+5, 125, 'king', 'black', 20)
            elif (board[j] == B_KNIGHT):
                gui.text(i+5, 125, 'knight', 'black', 20)
        i += 70
        j += 1

    gui.update_frame(60)


def is_game_over(board):
    """
    This function only uses the board list as an input, so that each of
    the elements can be checked to see if there are a black king and a
    white king present. It uses a while loop to check each value, and
    if it is one of the kings then their accumulater will go up. At the
    end, if one of the accumulaters is zero, then that king is not on
    the board, and it will print out the final board with the side that
    won.
    """
    i = 0
    b_win = 0
    w_win = 0
    while (i < 9):
        if (board[i] == B_KING):
            w_win += 1
        if (board[i] == W_KING):
            b_win += 1
        i += 1
    if (w_win == 0):
        print_board(board)
        print('White wins!')
        return True
    if (b_win == 0):
        print_board(board)
        print('Black wins!')
        return True
    return False


def move(board, position, direction):
    """
    This function takes in the board list as an input, along with the
    position the user enters as well as the direction. It checks to
    see if the piece that is being asked to move is a king or a knight
    and from there calls the next  function. It doesn't use the direction
    input, but instead just passes it along to the next function called.
    There is nothing printed from this function, and this one serves as a
    referal depending on which piece is in the position.
    """
    if (board[position] == W_KING or board[position] == B_KING):
        move_king(board, position, direction)
    else:
        move_knight(board, position, direction)

def main():

    # Create the canvas
    gui = graphics(700, 200, "1 Dimensional Chess")

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [
        W_KING,
        W_KNIGHT,
        W_KNIGHT,
        EMPTY,
        EMPTY,
        EMPTY,
        B_KNIGHT,
        B_KNIGHT,
        B_KING,
    ]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + " enter index:\n"))
        direction = input(player + " enter direction (l or r):\n")

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)

    draw_board(board, gui)


main()