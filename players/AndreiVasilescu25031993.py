from copy import deepcopy

empty_board = [[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0]]
good_move_board = [[0,0,0],[0,0,0,0],[0,1,0],[0,1,1,0],[0,0,0],[0,0,0,0],[0,0,0]]
ending_move_board = [[1,1,1],[1,1,1,1],[1,1,1],[1,1,1,1],[1,1,1],[1,1,1,1],[1,0,1]]
class AndreiVasilescu25031993:
    DEFAULT_SEARCH_DEPTH = 10
    ROW = 0
    COLUMN = 1
    MAX_VALUE = 100000
    MIN_VALUE = 0

    def enum(**enums):
        return type('Enum', (), enums)

    LineOrientation = enum(UNKNOWN = 0, HORIZONTAL = 1, VERTICAL = 2)

    def __init__(self):
        self.name = "Andrei Vasilescu"

    def move(self, board, score):
        return self.findMiniMaxMove(board, self.DEFAULT_SEARCH_DEPTH)

    #OK
    def getPossibleMoves(self, board):
        movesArray = []

        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                if currentRow[column] == 0:
                    movesArray.append((row, column))

        return movesArray

    #OK
    def getPossibleSuccessfullMoves(self, board):
        movesArray = []
        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                if currentRow[column] == 0:
                    currentMove = (row, column)
                    if (self.moveEarnsPoints(board, currentMove)):
                        movesArray.append(currentMove)
        return movesArray

    #OK
    def getPossibleFailingMoves(self, board):
        movesArray = []
        for row in range(len(board)):
            currentRow = board[row]
            for column in range(len(currentRow)):
                if currentRow[column] == 0:
                    currentMove = (row, column)
                    if (self.moveEarnsPoints(board, currentMove) == False):
                        movesArray.append(currentMove)
        return movesArray

    #OK
    def moveEarnsPoints(self, board, playerMove):
        moveOrientation = self.getLineOrientationForMove(playerMove)
        if moveOrientation == self.LineOrientation.HORIZONTAL:
            return self.horizontalMoveEarnsPoints(board, playerMove)
        else:
            return self.verticalMoveEarnsPoints(board, playerMove)

    #OK
    def horizontalMoveEarnsPoints(self, board, playerMove):
        moveRow = playerMove[self.ROW]
        moveColumn = playerMove[self.COLUMN]
        aboveRow = moveRow - 2
        if aboveRow >= 0:
            if board[aboveRow][moveColumn] == 1:
                betweenRow = aboveRow + 1
                if board[betweenRow][moveColumn] == 1 and board[betweenRow][moveColumn + 1] == 1:
                    return True

        belowRow = moveRow + 2
        if belowRow < len(board):
            if board[belowRow][moveColumn] == 1:
                betweenRow = moveRow + 1
                if board[betweenRow][moveColumn] == 1 and board[betweenRow][moveColumn + 1] == 1:
                    return True
        return False

    #OK
    def verticalMoveEarnsPoints(self, board, playerMove):
        moveRow = playerMove[self.ROW]
        moveColumn = playerMove[self.COLUMN]
        leftColumn = moveColumn - 1
        if leftColumn >= 0:
            if board[moveRow][leftColumn] == 1:
                aboveRow = moveRow - 1
                belowRow = aboveRow + 2
                if board[aboveRow][leftColumn] == 1 and board[belowRow][leftColumn] == 1:
                    return True

        rightColumn = moveColumn + 1
        if rightColumn < len(board[moveRow]):
            if board[moveRow][rightColumn] == 1:
                aboveRow = moveRow - 1
                belowRow = aboveRow + 2
                if board[aboveRow][moveColumn] == 1 and board[belowRow][moveColumn] == 1:
                    return True
        return False

    #OK
    def getLineOrientationForMove(self, playerMove):
        row = playerMove[self.ROW]
        if row % 2 == 0:
            return self.LineOrientation.HORIZONTAL
        else:
            return self.LineOrientation.VERTICAL

    #OK
    def getSimulatedMoveBoard(self, board, playerMove):
        simulatedBoard = deepcopy(board)
        return self.performMoveOnBoard(simulatedBoard, playerMove)

    #OK
    def performMoveOnBoard(self, board, playerMove):
        moveRow = playerMove[self.ROW]
        moveColumn = playerMove[self.COLUMN]
        board[moveRow][moveColumn] = 1
        return board

    def findMiniMaxMove(self, board, maxDepth):
        possibleMoves = self.getPossibleSuccessfullMoves(board)
        maxValue = self.MIN_VALUE
        bestMove = (0,0)
        for currentMove in possibleMoves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMinimizerNode(board, maxDepth - 1, maxValue, self.MAX_VALUE)
            if self.moveEarnsPoints(board, currentMove):
                score = score + 1

            if score > maxValue:
                maxValue = score
                bestMove = currentMove

        return bestMove

    def exploreMinimizerNode(self, board, maxDepth, alfa, beta):
        if maxDepth == 0:
            return self.MAX_VALUE

        nodeValue = self.MAX_VALUE
        possibleMoves = self.getPossibleFailingMoves(board)
        if len(possibleMoves) == 0:
            possibleMoves = self.getPossibleMoves(board)

        for currentMove in possibleMoves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMaximizerNode(board, maxDepth - 1, alfa, nodeValue)
            if self.moveEarnsPoints(board, currentMove):
                score = score + 1

            if score < nodeValue:
                nodeValue = score

            if nodeValue < alfa:
                return nodeValue

        return nodeValue

    def exploreMaximizerNode(self, board, maxDepth, alfa, beta):
        if maxDepth == 0:
            return self.MIN_VALUE

        nodeValue = self.MIN_VALUE
        possibleMoves = self.getPossibleSuccessfullMoves(board)
        if len(possibleMoves) == 0:
            possibleMoves = self.getPossibleMoves(board)

        for currentMove in possibleMoves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMinimizerNode(board, maxDepth - 1, nodeValue, beta)
            if self.moveEarnsPoints(board, currentMove):
                score = score + 1

            if score > nodeValue:
                nodeValue = score

            if nodeValue > beta:
                return nodeValue

        return nodeValue
