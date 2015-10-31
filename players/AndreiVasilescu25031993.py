from copy import deepcopy

class AndreiVasilescu25031993:
    DEFAULT_SEARCH_DEPTH = 10
    ROW = 0
    COLUMN = 1
    MAX_VALUE = 100000
    MIN_VALUE = -100000

    def enum(self, **enums):
        return type('Enum', (), enums)

    LineOrientation = enum(UNKNOWN = 0, HORIZONTAL = 1, VERTICAL = 2)

    def __init__(self):
        self.name = "Andrei Vasilescu"

    def move(self, board, score):
        return findMiniMaxMove(self, board, score, DEFAULT_SEARCH_DEPTH)

    def getPossibleMoves(self, board):
        movesArray = []

        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                if currentRow[column] == 0:
                    movesArray.append((row, column))

        return movesArray

    def getPossibleSuccessfullMoves(self, board):
        movesArray = []
        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                currentMove = (row, column)
                if (moveEarnsPoints(board, playerMove)):
                    movesArray.append(currentMove)
        return movesArray

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

    def getSimulatedMoveBoard(self, board, playerMove):
        simulatedBoard = deepcopy(board)
        return performMoveOnBoard(simulatedBoard, playerMove)

    def performMoveOnBoard(self, board, playerMove):
        moveRow = playerMove[ROW]
        moveColumn = playerMove[COLUMN]
        board[moveRow][moveColumn] = 1
        return board

    def findMiniMaxMove(self, board, maxDepth):
        possibleMoves = getPossibleSuccessfullMoves(board)
        maxValue = MIN_VALUE
        bestMove = (0,0)
        for currentMove in possibleMoves:
            simulatedBoard = getSimulatedMoveBoard(board, currentMove)
            score = exploreMinimizerNode(board, maxDepth, MIN_VALUE, MAX_VALUE)
            if score > maxValue:
                maxValue = score
                bestMove = currentMove

        return bestMove

    def exploreMinimizerNode(self, board, maxDepth, alfa, beta):
        if maxDepth == 0:
            return MAX_VALUE

        nodeValue = MAX_VALUE
        possibleMoves = getPossibleMoves(board)
        for currentMove in possibleMoves:
            simulatedBoard = getSimulatedBoard(board, currentMove)
            score = exploreMaximizerNode(board, maxDepth, alfa, nodeValue)
            if score[0] < nodeValue:
                nodeValue = score[0]

            if nodeValue < alfa:
                return nodeValue

        return nodeValue

    def exploreMaximizerNode(self, board, maxDepth, alfa, beta):
        if maxDepth == 0:
            return MIN_VALUE

        nodeValue = MIN_VALUE
        possibleMoves = getPossibleSuccessfullMoves(board)
        for currentMove in possibleMoves:
            simulatedBoard = getSimulatedBoard(board, currentMove)
            score = exploreMinimizerNode(board, maxDepth - 1, nodeValue, beta)
            if score > nodeValue:
                nodeValue = score

            if nodeValue > beta:
                return nodeValue

        return nodeValue
