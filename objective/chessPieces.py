from enum import auto


def FieldNumerical(letter, value):
    listWithLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if letter is not None:
        for i in range(len(listWithLetters)):
            if listWithLetters[i] == letter:
                return i
    else:
        return listWithLetters[value] if (value >=0 and value<=7) else None


def PawnbeatingMoves(oldPos, allFigurePosition, coef):
    letterNum = FieldNumerical(oldPos[0], None)
    beatingMovesLetters = [letterNum + 1, letterNum - 1]  # only letters
    beatingMoves = []
    for i in range(len(beatingMovesLetters)):
        if beatingMovesLetters[i] >=0 and beatingMovesLetters[i] < 8:
            move = int(oldPos[-1]) + coef*1
            fieldName = FieldNumerical(None, beatingMovesLetters[i]) + str(move)
            if allFigurePosition[fieldName] is not None:  # if figure on the pointed position exists
                beatingMoves.append(fieldName)

    return beatingMoves


def pawnMoves(IsfirstMove, oldPos, color, allFigurePos):
    possiblePos = []
    coef = 1 if color == "w" else -1
    move1 = int(oldPos[-1]) + coef * 1
    if IsfirstMove:  # Move 1 or 2 field
        if allFigurePos[oldPos[0] + str(move1)] is None:
            possiblePos.append(oldPos[0] + str(move1))
        move2 = int(oldPos[-1]) + coef * 2
        if allFigurePos[oldPos[0] + str(move2)] is None:
            possiblePos.append(oldPos[0] + str(move2))
    else:  # move only for one point
        if allFigurePos[oldPos[0] + str(move1)] is None:
            possiblePos.append(oldPos[0] + str(move1))
    possiblePos.extend(PawnbeatingMoves(oldPos, allFigurePos, coef))

    return possiblePos


def kingMoves(oldPos, figColor, allFigurePos, chessboard_fields):
    iterator = len(chessboard_fields[0])
    possiblePos = []
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    for i in range(iterator):  # rows
        for j in range(iterator):  #cols
            if i == oldPosNumber - 1 and j == oldPosCharNumber:
                if iterator - (i + 1) >= 0:  # right/left moves
                    if j + 1 < iterator:
                        pos = chessboard_fields[iterator - (i + 1)][j + 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # right moves
                    if j - 1 >= 0:
                        pos = chessboard_fields[iterator - (i + 1)][j - 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # left moves
                if iterator - (i + 2) >= 0:  # all upper moves
                    possiblePos.append(chessboard_fields[iterator - (i + 2)][j])  # upper moves
                    if j + 1 < iterator:
                        pos = chessboard_fields[iterator - (i + 2)][j + 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # right upper diagonal moves
                    if j - 1 >= 0:
                        pos = chessboard_fields[iterator - (i + 2)][j - 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # left upper diagonal moves
                if iterator - i >= 0 and iterator-i < iterator:  # all down moves
                    pos = chessboard_fields[iterator - i][j]
                    if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                        possiblePos.append(pos)  # down moves
                    if j - 1 >= 0:
                        pos = chessboard_fields[iterator - i][j - 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # left down diagonal moves
                    if j + 1 < iterator:
                        pos = chessboard_fields[iterator - i][j + 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # right down diagonal moves

    # print(possiblePos)  # to debug positions
    return possiblePos


def horizontalVerticalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, chessboardFigurePos, figureColor):
    possiblePositions = []
    iterator = len(chessboard_fields[0])
    for i in range(iterator):  # rows
        for j in range(iterator):  # cols
            if i == oldPosNumber - 1 and j == oldPosCharNumber:
                if iterator - (i + 1) >= 0:  # right/left moves
                    jTmp = j
                    iTmp = i
                    while jTmp + 1 < iterator and iterator - (iTmp + 1) < iterator:
                        pos = chessboard_fields[iterator - (iTmp + 1)][jTmp + 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)  # right moves
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp += 1
                    jTmp = j
                    iTmp = i
                    while jTmp - 1 >= 0 and iterator - (iTmp + 1) < iterator:
                        pos = chessboard_fields[iterator - (iTmp + 1)][jTmp - 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)  # left moves
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp -= 1
                jTmp = j
                iTmp = i
                while iterator - (iTmp + 2) >= 0 and jTmp < iterator:  # all upper moves
                    pos = chessboard_fields[iterator - (iTmp + 2)][jTmp]
                    if chessboardFigurePos[pos] is None:
                        possiblePositions.append(pos)  # upper moves
                    elif chessboardFigurePos[pos][0] != figureColor:
                        possiblePositions.append(pos)
                        break
                    else: break
                    iTmp += 1
                jTmp = j
                iTmp = i
                while iterator - iTmp >= 0 and iterator-iTmp < iterator and jTmp < iterator:  # all down moves
                    pos = chessboard_fields[iterator - iTmp][jTmp]
                    if chessboardFigurePos[pos] is None:
                        possiblePositions.append(pos)  # down moves
                    elif chessboardFigurePos[pos][0] != figureColor:
                        possiblePositions.append(pos)
                        break
                    else: break
                    iTmp -= 1
    return possiblePositions


def diagonalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, chessboardFigurePos, figureColor):
    possiblePositions = []
    iterator = len(chessboard_fields[0])
    for i in range(iterator):
        for j in range(iterator):
            if i == oldPosNumber - 1 and j == oldPosCharNumber:
                if iterator - (i + 2) >= 0:
                    jTmp = j
                    iTmp = i
                    while jTmp + 1 < iterator and iterator - (iTmp + 2) >= 0:  # right upper diagonal
                        pos = chessboard_fields[iterator - (iTmp + 2)][jTmp + 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp += 1
                        iTmp += 1
                    jTmp = j
                    iTmp = i
                    while jTmp - 1 >= 0 and iterator - (iTmp + 2) >= 0:  # left upper diagonal
                        pos = chessboard_fields[iterator - (iTmp + 2)][jTmp - 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp -= 1
                        iTmp += 1
                if iterator - i >= 0 and iterator - i < iterator:
                    jTmp = j
                    iTmp = i
                    while jTmp - 1 >= 0 and iterator - iTmp >= 0 and iterator - iTmp < iterator:  # left lower diagonal
                        pos = chessboard_fields[iterator - iTmp][jTmp - 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp -= 1
                        iTmp -= 1
                    jTmp = j
                    iTmp = i
                    while jTmp + 1 < iterator and iterator - iTmp >= 0 and iterator - iTmp < iterator:  # right lower diagonal
                        pos = chessboard_fields[iterator - iTmp][jTmp + 1]
                        if chessboardFigurePos[pos] is None:
                            possiblePositions.append(pos)
                        elif chessboardFigurePos[pos][0] != figureColor:
                            possiblePositions.append(pos)
                            break
                        else: break
                        jTmp += 1
                        iTmp -= 1
    return possiblePositions


def bishopMoves(oldPos, figColor, allFigurePos, chessboard_fields):
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    possiblePos = diagonalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, allFigurePos, figColor)
    # print(possiblePos)

    return possiblePos


def queenMoves(oldPos, allFigurePos, chessboard_fields):
    figColor = allFigurePos[oldPos][0]
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    possiblePos0 = horizontalVerticalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, allFigurePos, figColor)
    possiblePos1 = diagonalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, allFigurePos, figColor)
    possiblePos0.extend(possiblePos1)
    # print(possiblePos0)

    return possiblePos0


def rookMoves(oldPos, allFigurePos, chessboard_fields):
    figColor = allFigurePos[oldPos][0]
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    possiblePos = horizontalVerticalMoves(oldPosNumber, oldPosCharNumber, chessboard_fields, allFigurePos, figColor)
    # print(possiblePos)  # for debug
    return possiblePos


def knightMoves(oldPos, figColor, allFigurePos, chessboard_fields):
    iterator = len(chessboard_fields[0])
    possiblePos = []
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    for i in range(iterator):  # rows
        for j in range(iterator):  # cols
            if i == oldPosNumber - 1 and j == oldPosCharNumber:
                if iterator - (i + 2) >= 0:  # right/left moves
                    if j + 2 < iterator:
                        pos = chessboard_fields[iterator - (i + 2)][j + 2]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # upper right move
                    if j - 2 >= 0:
                        pos = chessboard_fields[iterator - (i + 2)][j - 2]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # upper left move
                if iterator - i < iterator:  # right/left moves
                    if j + 2 < iterator:
                        pos = chessboard_fields[iterator - i][j + 2]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # right moves
                    if iterator-i+1 < iterator and j+1 < iterator:
                        pos = chessboard_fields[iterator - i+1][j + 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)
                    if j - 2 >= 0:
                        pos = chessboard_fields[iterator - i][j - 2]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # left
                    if iterator-i+1 < iterator and j-1 >=0:
                        pos = chessboard_fields[iterator - i+1][j - 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)
                if iterator - (i + 3) >= 0:  # right/left moves
                    if j + 1 < iterator:
                        pos = chessboard_fields[iterator - (i + 3)][j + 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)  # upper right move
                    if j - 1 >= 0:
                        pos = chessboard_fields[iterator - (i + 3)][j - 1]
                        if allFigurePos[pos] is None or allFigurePos[pos][0] != figColor:
                            possiblePos.append(pos)

    # print(possiblePos)  # to debug positions
    return possiblePos


class Pawn():
    def __init__(self, color):
        self.firstMove = 2
        self.move = 1
        self.color = color
        self.img = 'C:/Users/Admin/PycharmProjects/TicTacToePython/figures/b_pawn.png'

    def loadImageObject(self, color):
        pass


class ChessPiece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position