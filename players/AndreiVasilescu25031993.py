class AndreiVasilescu25031993:
    DEFAULT_SEARCH_DEPTH = 10
    ROW = 0
    COLUMN = 1

    def enum(self, **enums):
        return type('Enum', (), enums)

    LineOrientation = enum(UNKNOWN = 0, HORIZONTAL = 1, VERTICAL = 2)

    def __init__(self):
        self.name = "Andrei Vasilescu"

    def move(self, board, score):
        return findMiniMaxMove(self, board, score, DEFAULT_SEARCH_DEPTH)

    #ToDo: Needs testing
    def getPossibleMoves(self, board):
        movesArray = []

        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                if currentRow[column] == 0:
                    movesArray.append((row, column))

        return movesArray

    #ToDo: Needs testing
    def getPossibleSuccessfullMoves(self, board):
        movesArray = []
        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                currentMove = (row, column)
                if (moveEarnsPoints(board, playerMove)):
                    movesArray.append(currentMove)
        return movesArray

    #ToDo: Needs testing
    def moveEarnsPoints(self, board, playerMove):
        moveOrientation = getLineOrientationForMove(playerMove)
        if moveOrientation == LineOrientation.HORIZONTAL:
            return horizontalMoveEarnsPoints(board, playerMove)
        else:
            return verticalMoveEarnsPoints(board, playerMove)

    def horizontalMoveEarnsPoints(self, board, playerMove):
        moveRow = playerMove[ROW]
        moveColumn = playerMove[COLUMN]
        aboveRow = moveRow - 2
        if aboveRow >= 0:
            if board[aboveRow][moveColumn] == 1:
                betweenRow = aboveRow + 1
                if board[betweenRow][moveColumn] == 1 and
                    board[betweenRow][moveColumn + 1] == 1:
                    return True

        belowRow = moveRow + 2
        if belowRow < len(board):
            if board[belowRow][moveColumn] == 1:
                betweenRow = moveRow + 1
                if board[betweenRow][moveColumn] == 1 and
                    board[betweenRow][moveColumn + 1] == 1:
                    return True
        return False

    def verticalMoveEarnsPoints(self, board, playerMove):
        moveRow = playerMove[ROW]
        moveColumn = playerMove[COLUMN]
        leftColumn = moveColumn - 1
        if leftColumn >= 0:
            if board[moveRow][leftColumn] == 1:
                aboveRow = moveRow - 1
                belowRow = aboveRow + 2
                if board[aboveRow][leftColumn] == 1 and
                    board[belowRow][leftColumn] == 1:
                    return True

        rightColumn = moveColumn + 1
        if rightColumn < len(board[moveRow]):
            if board[moveRow][rightColumn] == 1:
                aboveRow = moveRow - 1
                belowRow = aboveRow + 2
                if board[aboveRow][rightColumn] == 1 and
                    board[belowRow][rightColumn] == 1:
                        return True
        return False

    def getLineOrientationForMove(self, playerMove):
        row = playerMove[ROW]
        if row % 2 == 0:
            return LineOrientation.HORIZONTAL
        else:
            return LineOrientation.VERTICAL

    def getSimulatedMoveBoard(self, board):
        #ToDo:
        return board

    def findMiniMaxMove(self, board, score, maxDepth):
        #ToDo:
        return (0,0)

    def exploreAlfaBetaNode(self, board, score, maxDepth, alfa, beta):
        #ToDo:
        return None
