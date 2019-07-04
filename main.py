import numpy as np
import os

class Game:
    def __init__(self, type, child, p1, p2):
        self.gtype = type
        self.child = child
        self.p1 = p1
        self.p2 = p2

    def GetPieceID(self, piece):
        if piece == 0:
            return
        return int(piece[-1])

    def IsSafePosition(self, x ,y):
        if self.gtype == "chess":
            return not (x < 0 or x > 7 or y < 0 or y > 7)
        elif self.gtype == "go":
            return not (x < 0 or x > 18 or y < 0 or y > 18)

class Go(Game):
    def __init__(self, p1, p2):
        super(Go, self).__init__("go",self, p1, p2)
        myBoard = Board(self.gtype, p1, p2)
        self.Board = myBoard
        myPiece1 = Piece(self.gtype)
        myPlayer1 = Player(self.gtype, p1, myPiece1, 1)
        self.player1 = myPlayer1

        myPiece2 = Piece(self.gtype)
        myPlayer2 = Player(self.gtype, p2, myPiece1, 2)
        self.player2 = myPlayer2

        myAction = Action(self.gtype, p1, p2, go=self)
        self.Action = myAction

    def GetPlayer(self, playername):
        if self.player1.playername == playername:
            return self.player1
        elif self.player2.playername == playername:
            return self.player2
        else:
            return

    def GetPlayerbyID(self, ID):
        if self.player1.playerID == ID:
            return self.player1
        elif self.player2.playerID == ID:
            return self.player2
        else:
            return


class Chess(Game):
    def __init__(self, p1, p2):
        super(Chess, self).__init__("chess", self, p1, p2)
        myBoard = Board(self.gtype, p1, p2)
        self.Board = myBoard
        myPiece1 = Piece(self.gtype)
        myPlayer1 = Player(self.gtype, p1, myPiece1, 1)
        self.player1 = myPlayer1

        myPiece2 = Piece(self.gtype)
        myPlayer2 = Player(self.gtype, p2, myPiece1, 2)
        self.player2 = myPlayer2

        myAction = Action(self.gtype, p1, p2, chess=self)
        self.Action = myAction

    def GetPlayer(self, playername):
        if self.player1.playername == playername:
            return self.player1
        elif self.player2.playername == playername:
            return self.player2
        else:
            return

    def GetPlayerbyID(self, ID):
        if self.player1.playerID == ID:
            return self.player1
        elif self.player2.playerID == ID:
            return self.player2
        else:
            return

class Player():
    def __init__(self, gtype, playername, piece, playerID):
        self.gtype = gtype
        self.playername = playername
        self.piece = piece
        self.playerID = playerID

class Board(Game):
    def __init__(self, gtype, p1, p2):
        super(Board, self).__init__(gtype, self, p1, p2)
        if gtype == "chess":
            #board = [[""]*8]*8
            board = np.zeros((8, 8), dtype=object)
            board[0][0] = 'r1'
            board[0][1] = 'knight1'
            board[0][2] = 'b1'
            board[0][3] = 'king1'
            board[0][4] = 'q1'
            board[0][5] = 'b1'
            board[0][6] = 'knight1'
            board[0][7] = 'r1'
            for i in range(8):
                board[1][i] = "p1"

            board[7][0] = 'r2'
            board[7][1] = 'knight2'
            board[7][2] = 'b2'
            board[7][3] = 'king2'
            board[7][4] = 'q2'
            board[7][5] = 'b2'
            board[7][6] = 'knight2'
            board[7][7] = 'r2'
            for i in range(8):
                board[6][i] = "p2"
            self.board = board
        elif gtype == "go":
            board = np.zeros((19, 19), dtype=object)
            self.board = board
    def GetPiece(self,x , y):
        return self.board[x][y]

    def SetPiece(self, piece, x ,y):
        self.board[x][y] = piece

    def ClearPiece(self, x, y):
        self.board[x][y] = 0

    def ShowBoard(self):
         print(self.board)

class Piece():
    def __init__(self, gtype):
        self.gtype = gtype
        if self.gtype == "go":
            data = {"g": 19*19}
            self.data = data
        elif self.gtype == 'chess':
            data = {"king" : 1,
                    "q" : 1,
                    "r" : 2,
                    "b" : 2,
                    "knight" : 2,
                    "p" : 8}
            self.data = data
            # self.king = 1
            # self.q = 1
            # self.r = 2
            # self.b = 2
            # self.knight = 2
            # self.p = 8

    def lose(self, piece):
        self.data[piece[:-1]] -= 1
        if self.data[piece[:-1]] < 0:
            print("error")

class Position():
    def __init__(self, gtype):
        pass

class Action(Game):
    def __init__(self, gtype, p1, p2, chess=None, go=None):
        super(Action, self).__init__(gtype, self, p1, p2)
        self.chess = chess
        self.go = go

    def CountPiece(self):
        if self.gtype == "chess":
            obj = self.chess
        elif self.gtype == "go":
            obj = self.go
        myboard = obj.Board.board
        pl1 = pl2 = 0
        for row in myboard:
            for col in row:
                if 1 == self.GetPieceID(col):
                    pl1+=1
                elif 2 == self.GetPieceID(col):
                    pl2+=1
        strp1 = self.p1 + ": " + str(pl1)
        strp2 = self.p2 + ": " + str(pl2)
        print(strp1)
        print(strp2)

    def GetPosInfo(self, x , y):
        if self.gtype == "chess":
            obj = self.chess
        elif self.gtype == "go":
            obj = self.go
        if not self.IsSafePosition(x, y):
            return False
        piece = obj.Board.GetPiece(x, y)
        if piece == 0:
            print("Empty")
            return
        playerID = int(self.GetPieceID(piece))
        playerobj = obj.GetPlayerbyID(playerID)
        print(piece)
        print(playerobj.playername)


    def Position(self, player, piece, x, y):
        if self.gtype == "go":
            player = self.go.GetPlayer(player)
            if player.playerID != self.GetPieceID(piece):
                return False
            if not self.IsSafePosition(x, y):
                return False
            if self.go.Board.GetPiece(x,y) != 0:
                return False
            self.go.Board.SetPiece(piece, x, y)
        elif self.gtype == 'chess':
            player = self.chess.GetPlayer(player)
            if player.playerID != self.GetPieceID(piece):
                return False
            if not self.IsSafePosition(x, y):
                return False
            if self.chess.Board.GetPiece(x,y) != 0:
                return False
            self.chess.Board.SetPiece(piece, x, y)
    def MOVE(self, player, x1, y1, x2, y2):
        #chess only
        if not (self.IsSafePosition(x1, y1) and self.IsSafePosition(x2, y2)):
            return
        if self.chess.Board.GetPiece(x2, y2) != 0:
            return
        if self.chess.Board.GetPiece(x1, y1) == 0:
            return
        if x1==x2 and y1 ==y2:
            return
        playerobj = self.chess.GetPlayer(player)
        piece = self.chess.Board.GetPiece(x1,y1)
        if playerobj.playerID != int(self.GetPieceID(piece)):
            return
        self.chess.Board.SetPiece(piece, x2, y2)
        self.chess.Board.ClearPiece(x1, y1)

    def LIFT(self, player, x , y):
        #go only
        if not self.IsSafePosition(x, y):
            return False
        if self.go.Board.GetPiece(x, y) == 0:
            return False
        player = self.go.GetPlayer(player)
        piece = self.go.Board.GetPiece(x,y)
        if player.playerID == int(self.GetPieceID(piece)):
            return False
        self.go.Board.ClearPiece(x, y)

    def EAT(self, player, x1, y1, x2, y2):
        #chess only
        if not (self.IsSafePosition(x1, y1) and self.IsSafePosition(x2, y2)):
            return
        if self.chess.Board.GetPiece(x2, y2) == 0:
            return
        if self.chess.Board.GetPiece(x1, y1) == 0:
            return
        if x1 == x2 and y1 == y2:
            return
        player1 = self.chess.GetPlayer(player)
        piece1 = self.chess.Board.GetPiece(x1,y1)
        piece2 = self.chess.Board.GetPiece(x2, y2)
        if player1.playerID !=int(self.GetPieceID(piece1)):
            return
        if player1.playerID ==int(self.GetPieceID(piece2)):
            return
        self.chess.Board.SetPiece(piece1, x2, y2)
        self.chess.Board.ClearPiece(x1, y1)

        player2 = self.chess.GetPlayerbyID(int(self.GetPieceID(piece2)))
        player2.piece.lose(piece2)



if __name__ == "__main__":
    GameType = input('Game: chess or go: ')
    pl1, pl2 = input("player1 and player2's name: ").split(' ')
    if pl1 == pl2:
        os._exit(0)
    if GameType == "chess":
        myGame = Chess(pl1, pl2)
    elif GameType == "go":
        myGame = Go(pl1, pl2)
    if myGame:
        i = 0
        while True:
            if i % 2 == 0:
                mystr = pl1 + " please input: "
                player = pl1
            elif i % 2 == 1:
                mystr = pl2 + " please input: "
                player = pl2
            command = input(mystr)
            if command.upper() == "END":
                break
            i += 1
            decomm = command.split(' ')
            if decomm[0].upper() == "EAT":
                myGame.Action.EAT(player, int(decomm[1]), int(decomm[2]), int(decomm[3]), int(decomm[4]))
            elif decomm[0].upper() == "MOVE":
                myGame.Action.MOVE(player, int(decomm[1]), int(decomm[2]), int(decomm[3]), int(decomm[4]))
            elif decomm[0].upper() == "LIFT":
                myGame.Action.LIFT(player, int(decomm[1]), int(decomm[2]))
            elif decomm[0].upper() == "POS":
                myGame.Action.Position(player, int(decomm[1]), int(decomm[2]), int(decomm[3]))
            elif decomm[0].upper() == "INFO":
                myGame.Action.GetPosInfo(int(decomm[1]), int(decomm[2]))
                i -= 1
            elif decomm[0].upper() == "COUNT":
                myGame.Action.CountPiece()
                i -= 1
            else:
                continue
            myGame.Board.ShowBoard()



