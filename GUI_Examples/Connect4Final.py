from tkinter import *
# Merle Crutchfield
# Connect4Final.py
# 5/1/2022

# ConnectFour board class
class ConnectFour:
    def __init__(self):
        self.grid = [[] for i in range(7)]
        self.playerOneTurn = True
        self.gameOver = False

    def dropPiece(self, column):
        if self.gameOver or column < 0 or column >= 7 or len(self.grid[column]) == 6:
            return False
        if self.playerOneTurn:
            self.grid[column].append('x')
        else:
            self.grid[column].append('o')
        if self.checkWin() == 'going':
            self.playerOneTurn = not self.playerOneTurn
        else:
            self.gameOver = self.checkWin()
        return True

    def checkWin(self):
        count = 0
        grid2 = self.grid
        for c in self.grid:
            col = ''.join(c)
            if 'xxxx' in col or 'oooo' in col:
                return 'win'
        temp = []
        for r in range(6):
            row = ''
            val = []
            for c in range(7):
                if len(self.grid[c]) > r:
                    row += self.grid[c][r]
                    val.append(self.grid[c][r])
                else:
                    row += ' '
                    val.append(' ')
            if 'xxxx' in row or 'oooo' in row:
                return 'win'
            temp.append(val)
        diag1 = [[] for i in range(12)]
        diag2 = [[] for j in range(12)]
        for x in range(7):
            for y in range(6):
                diag1[x+y].append(temp[y][x])
                diag2[x-y+5].append(temp[y][x])
        for val in diag1:
            diag = ''.join(val)
            if 'xxxx' in diag or 'oooo' in diag:
                return 'win'
        for val in diag2:
            diag = ''.join(val)
            if 'xxxx' in diag or 'oooo' in diag:
                return 'win'
        for x in temp:
            for y in x:
                if y == 'x' or y == 'o':
                    count += 1
        if count == 42:
            return 'draw'
        return 'going'

# GUI class
class GUI:
    redWins = 0
    yellowWins = 0
    ties = 0
    isGameOver = False
    turn = 'yellow'

    def __init__(self, master):
        self.master = master
        master.title('Connect Four GUI')
        label = Label(master, text="(: Connect Four :)", font = ("Helvetica", 50), bg='white')
        label.grid(row=0)
        button = Button(master, text="New Game", fg='white', bg='blue', command=self.newGame, font = ("Helvetica", 20))
        button2 = Button(master, text="Leaderboard", fg='white', bg='blue', command=self.showScores, font = ("Helvetica", 20))
        button.grid(row=1, column=0, sticky=W)
        button2.grid(row=1, column=0, sticky=E)
        self.canvas = Canvas(master, width=20, height=50, background='blue', highlightthickness=0)
        self.canvas.grid(row=2)
        self.playerVar = StringVar(self.master, value="Current player: Yellow")
        self.playerLabel = Label(self.master, textvariable=self.playerVar, font = ("Helvetica", 20), anchor=W, fg=self.turn, bg='white')
        self.playerLabel.grid(row=1)
        self.canvas.bind('<Button-1>', self.click)
        self.newGame()

    def drawGame(self):
        for c in range(7):
            for r in range(6):
                x0 = c*100
                y0 = r*100
                x1 = (c+1)*100
                y1 = (r+1)*100
                self.canvas.create_oval(x0+3,self.canvas.winfo_height()-(y0+3),x1-3,self.canvas.winfo_height()-(y1-3),fill='white',outline='white')
        for c in range(7):
            for r in range(6):
                if not (r >= len(self.game.grid[c])):
                    x0 = c*100
                    y0 = r*100
                    x1 = (c+1)*100
                    y1 = (r+1)*100
                    if self.game.grid[c][r] == 'x':
                        fill = 'yellow'
                    else:
                        fill = 'red'
                    self.canvas.create_oval(x0+3,self.canvas.winfo_height()-(y0+3),x1-3,self.canvas.winfo_height()-(y1-3),fill=fill,outline='white')

    def newGame(self):
        self.playerOne = 'Yellow'
        self.playerTwo = 'Red'
        self.game = ConnectFour()
        self.canvas.delete(ALL)
        self.canvas.config(width=700,height=600)
        self.master.update()
        self.drawGame()
        self.changePlayer()
        self.isGameOver = True

    def showScores(self):
        self.isGameOver = False
        val1 = "Red Wins:    " + str(self.redWins)
        val2 = "Yellow Wins: " + str(self.yellowWins)
        val3 = "Ties:        " + str(self.ties)
        self.canvas.delete(ALL)
        self.playerVar.set('')
        self.canvas.create_text(190,100,fill="red",font = ("Helvetica", 40),text=val1)
        self.canvas.create_text(200,200,fill="yellow",font = ("Helvetica", 40),text=val2)
        self.canvas.create_text(160,300,fill="white",font = ("Helvetica", 40),text=val3)

    def changePlayer(self):
        if self.game.playerOneTurn:
            p = self.playerOne
            self.turn = 'yellow'
        else:
            p = self.playerTwo
            self.turn = 'red'
        self.playerVar.set('Current player: ' + p)
        self.playerLabel = Label(self.master, textvariable=self.playerVar, font = ("Helvetica", 20), anchor=W, fg=self.turn, bg='white')
        self.playerLabel.grid(row=1)

    def click(self, event):
        if not self.isGameOver or self.game.gameOver:
            return
        spot = event.x // 100
        if spot >= 0 and spot < 7:
            self.game.dropPiece(spot)
            self.drawGame()
            self.changePlayer()
        if self.game.gameOver:
            x = self.canvas.winfo_width() // 2
            y = self.canvas.winfo_height() // 2
            if self.game.gameOver == 'draw':
                t = 'It\'s a tie!'
                self.ties += 1
            else:
                if self.game.playerOneTurn:
                    winner = self.playerOne
                else:
                    winner = self.playerTwo
                if self.game.playerOneTurn:
                    self.yellowWins += 1
                else:
                    self.redWins += 1
                t = winner + ' won!'
            self.canvas.create_rectangle(x-190, y-50, x+190, y+50, fill="Grey")
            self.canvas.create_text(x, y, text=t, font=("Helvetica", 50), fill="Black")

# Starts game
root = Tk()
root.configure(background = 'white')
app = GUI(root)
root.mainloop()
