from copy import deepcopy
import threading

class AndreiVasilescu25031993:
    DEFAULT_SEARCH_DEPTH = 2
    ROW = 0
    COLUMN = 1
    MAX_VALUE = 100000
    MIN_VALUE = 0

    def enum(**enums):
        return type('Enum', (), enums)

    LineOrientation = enum(UNKNOWN = 0, HORIZONTAL = 1, VERTICAL = 2)

    threadResults = [(0,0),(0,0)]

    def __init__(self):
        self.name = "Andrei Vasilescu"

    def move(self, board, score):
        nextMove = self.findMiniMaxMove(board, self.DEFAULT_SEARCH_DEPTH, score)
        return nextMove

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
                else:
                    orientation = self.getLineOrientationForMove((row, column))
                    if orientation == self.LineOrientation.HORIZONTAL:
                        movesArray.extend(self.getPossibleMovesForHorizontalPosition((row, column), board))
                    else:
                        movesArray.extend(self.getPossibleMovesForVerticalPosition((row, column), board))
        movesArray = list(set(movesArray))
        return movesArray

    def getPossibleMovesForHorizontalPosition(self, position, board):
        moves = []
        belowRow = position[0] + 2
        betweenRow = position[0] + 1
        column = position[1]
        rightColumn = column + 1

        if betweenRow < len(board):
            if board[betweenRow][column] == 0:
                moves.append((betweenRow, column))
            if board[betweenRow][rightColumn] == 0:
                moves.append((betweenRow, rightColumn))

        if belowRow < len(board):
            if board[belowRow][column] == 0:
                moves.append((belowRow, column))

        return moves

    def getPossibleMovesForVerticalPosition(self, position, board):
        moves = []

        aboveRow = position[0] - 1
        belowRow = position[0] + 1
        row = position[0]
        column = position[1]
        leftColumn = position[1] - 1
        rightColumn = position[1] + 1
        if aboveRow >= 0:
            if column < len(board[aboveRow]):
                if board[aboveRow][column] == 0:
                    moves.append((aboveRow, column))

            if leftColumn >= 0:
                if board[aboveRow][leftColumn] == 0:
                    moves.append((aboveRow, leftColumn))

        if belowRow < len(board):
            if column < len(board[aboveRow]):
                if board[belowRow][column] == 0:
                    moves.append((belowRow, column))
            if leftColumn > 0:
                if board[belowRow][leftColumn] == 0:
                    moves.append((belowRow, leftColumn))

        if leftColumn > 0:
            if board[row][leftColumn] == 0:
                moves.append((row, leftColumn))

        if rightColumn < len(board[row]):
            if board[row][rightColumn] == 0:
                moves.append((row, rightColumn))

        return moves

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

    def splitArray(self, array):
        half = len(array) / 2
        return array[:half], array[half:]

    def findMiniMaxMove(self, board, maxDepth, playersScore):
        possibleMoves = self.getPossibleSuccessfullMoves(board)
        if len(possibleMoves) == 0:
            possibleMoves = self.getPossibleMoves(board)

        maxValue = playersScore

        possibleMoves0, possibleMoves1 = self.splitArray(possibleMoves)

        thread = threading.Thread(target=self.getBestMoveFromMoves, args=(board,
            maxDepth, playersScore, possibleMoves1, 1))

        thread.start()
        self.getBestMoveFromMoves(board, maxDepth, playersScore, possibleMoves0, 0)

        thread.join()

        result0 = self.threadResults[0]
        result1 = self.threadResults[1]

        if result0[1][0] > result1[1][0]:
            return result0[0]
        else:
            return result1[0]

    def getBestMoveFromMoves(self, board, maxDepth, playersScore, moves, tid):
        bestMove = (0,0)
        maxValue = playersScore

        for currentMove in moves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMinimizerNode(board, maxDepth - 1, playersScore, maxValue, self.MAX_VALUE)

            if self.moveEarnsPoints(board, currentMove):
                score = (score[0] + 1, score[1])

            if score[0] >= maxValue[0]:
                maxValue = score
                bestMove = currentMove

        self.threadResults[tid] = (bestMove, maxValue)

    def exploreMinimizerNode(self, board, maxDepth, playersScore, alfa, beta):
        if maxDepth == 0:
            return playersScore

        nodeValue = playersScore
        possibleMoves = self.getPossibleSuccessfullMoves(board)
        if len(possibleMoves) == 0:
            possibleMoves = self.getPossibleMoves(board)

        if len(possibleMoves) == 0:
            if playersScore[1] > playersScore[0]:
                return (playersScore[0] - 1000, playersScore[1] + 1000)

        for currentMove in possibleMoves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMaximizerNode(board, maxDepth - 1, playersScore, alfa, self.MAX_VALUE)
            if self.moveEarnsPoints(board, currentMove):
                score = (score[0], score[1] + 1)

            if score[1] < nodeValue[1]:
                nodeValue = score

            if nodeValue[0] <= alfa:
                return nodeValue

        return nodeValue

    def exploreMaximizerNode(self, board, maxDepth, playersScore, alfa, beta):
        if maxDepth == 0:
            return playersScore

        nodeValue = playersScore
        possibleMoves = self.getPossibleSuccessfullMoves(board)
        if len(possibleMoves) == 0:
            possibleMoves = self.getPossibleMoves(board)

        if len(possibleMoves) == 0:
            if playersScore[1] > playersScore[0]:
                return (playersScore[0] + 1000, playersScore[1] - 1000)

        for currentMove in possibleMoves:
            simulatedBoard = self.getSimulatedMoveBoard(board, currentMove)
            score = self.exploreMinimizerNode(board, maxDepth - 1, playersScore, nodeValue[0], beta)
            if self.moveEarnsPoints(board, currentMove):
                score = (score[0] + 1, score[1])

            if score[0] >= nodeValue[0]:
                nodeValue = score

            if nodeValue[1] >= beta:
                return nodeValue

        return nodeValue
