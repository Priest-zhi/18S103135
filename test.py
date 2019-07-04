import numpy as np
import os
from main import *

def testEAT():
    myChess = Chess("player1", "player2")
    myChess.Board.ShowBoard()
    myChess.Action.EAT("player1",1,1,6,7)
    myChess.Board.ShowBoard()

def testLIFT():
    myGO = Go("player1", "player2")
    myGO.Action.Position("player1","g1",2,3)
    myGO.Action.Position("player1", "g1", 3, 3)
    myGO.Action.Position("player2", "g2", 4, 3)
    myGO.Board.ShowBoard()
    myGO.Action.LIFT("player2",2,3)
    myGO.Board.ShowBoard()

if __name__ == "__main__":
    testEAT()
    testLIFT()