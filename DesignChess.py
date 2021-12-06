# Use Cases
# 1. Initialize the board
# Assign Play 1/2 as White and Black
# Clear Board and each piece should be at the correct places
# 2. Move
# Play send out the move request and check if Valid, and then piece should check if they kill anyone
# 3. Check win/lose/Tie
# Game should check after each move, if there's any result, need to sendout the status notice and clear the board

class ChessGame(object):
    def __init__(self, size):
        self.__board # board
        self.__players # List[player] only allow 2 players
        self.__gameStatus # GameStatus
        self.__size #int

    def initializeBoard(self, size):
        pass
    
    def assignPlayerColor(self):
        pass

    def MovePiece(self, moveRequest): #Move Reqeust
        pass

    def checkGameStatus(self): # return GameStatus
        pass

    def clearGame(self): # return void
        pass
        
class Board(object):
    def __init__(self):
        self.__board # Piece[][]

    def initializeBoard(self, size): #int
        pass

    def MovePiece(self, piece, location): # Piece, int[][]
        pass

    def getPieceLocation(self, piece):  #Piece, return int[][]
        pass 

class Player(object):
    def __init__(self):
        self.__color # Color
    
    def getColor(self):
        pass

    def setColor(self, color): # Color
        pass

    def sendMoveRequest(self, piece, location): # Piece, int[][]
        pass

class MoveRequest(object):
    def __init__(self):
        self.__piece # Piece
        self.__location #int[][]
        self.__player # Player
    
    def getRequest(self):
        pass
    
    def setRequest(self, piece, location, player):
        pass

class Color(enumerate):
    def __init__(self):
        black, white = 1, 2

class GameStatus(enumerate):
    def __init__(self):
        WhiteWin, BlackWin, Tie, Ongoing, NotActive = 1, 2, 3, 4, 5

class InvalidMoveRequestException(Exception):
    pass

class Piece(object):
    def __init__(self):
        self._color # color
        self._location # location
        self._ifKilled # boolean
        self._MoveAllowed # MoveAllowed

    def movePiece(self, location): # int[][] return void
        pass

    def getMoveAllowed(self): # return int[][]
        pass

    def getKilledStatus(self): # return boolean
        pass

class Knight(Piece):
    def __init__(self):
        super().__init__()

class Queen(Piece):
    def __init__(self):
        super().__init__()

class King(Piece):
    def __init__(self):
        super().__init__()

class Pawn(Piece):
    def __init__(self):
        super().__init__()

class Bishop(Piece):
    def __init__(self):
        super().__init__()

class Rooks(Piece):
    def __init__(self):
        super().__init__()

        
    
    



