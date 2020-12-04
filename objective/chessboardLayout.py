import pygame
import numpy as np
from figures import *
# todo: coloring field which user clicked,

class Chessboard:
    def __init__(self, surface, x_offset, y_offset, square_length):
        self.blackFigures, self.whiteFigures = self.initFigures()
        self.surface = surface
        self.figurePos = {}
        self.n = 8  # board 8x8
        self.x_offset = x_offset  # x_offset_of_Board
        self.y_offset = y_offset  # y_offset_of_Board
        self.square_length = square_length
        self.fields = self.generateFieldNames()
        self.chessboardFields = self.chessboardSquareNotation(self.n,self.square_length, self.fields)

    def generateFieldNames(self, swap=False):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = [8, 7, 6, 5, 4, 3, 2, 1]
        if swap is True:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        listWithFieldNames = np.ndarray(shape=(8, 8), dtype='object')
        for rows in range(0, len(listWithFieldNames)):
            for col in range(0, len(listWithFieldNames)):
                listWithFieldNames[rows][col] = letters[rows] + str(numbers[col])
        return listWithFieldNames

    def insertFiguresIntoChessboard(self, chessboard, sq_size):
        whiteFigurePosition = {}
        blackFigurePosition = {}
        w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = self.whiteFigures
        for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
            self.surface.blit(pygame.transform.scale(w_pawn, (50, 50)), (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
            dictTmp = {field: 'w_pawn'}
            whiteFigurePosition.update(dictTmp)

        figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
        w_figureNames = ["w_rook", "w_horse", "w_bishop", "w_queen", "w_king", "w_bishop", "w_horse", "w_rook"]
        for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
            self.surface.blit(pygame.transform.scale(figures[i], (50, 50)), (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
            dictTmp = {fields: w_figureNames[i]}
            whiteFigurePosition.update(dictTmp)

        self.figurePos.update(whiteFigurePosition)

        for i in range(3, 6):
            for j in range(0, 8):
                dictTmp = {self.fields[j][i]: None}
                self.figurePos.update(dictTmp)

        b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = self.blackFigures
        b_figureNames = ["b_rook", "b_horse", "b_bishop", "b_queen", "b_king", "b_bishop", "b_horse", "b_rook"]
        for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
            self.surface.blit(pygame.transform.scale(b_pawn, (50, 50)), (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
            dictTmp = {field: 'b_pawn'}
            blackFigurePosition.update(dictTmp)

        figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
        for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
            self.surface.blit(pygame.transform.scale(figures[i], (50, 50)), (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
            dictTmp = {fields: b_figureNames[i]}
            blackFigurePosition.update(dictTmp)

        self.figurePos.update(blackFigurePosition)

        return whiteFigurePosition, blackFigurePosition

    def moveFigure(self, oldPos, newPos, figureName):
        path = 'C:/Users/Admin/PycharmProjects/TicTacToePython/figures/'
        if self.figurePos[oldPos] is not None:
            self.figurePos[oldPos] = ''
            self.figurePos[newPos] = figureName
            self.surface.blit(pygame.transform.scale(pygame.image.load(path+figureName+".png"), (50, 50)), (self.chessboardFields[newPos][1] + (self.square_length / 2), self.chessboardFields[newPos][0] + (self.square_length / 2)))
        else:
            print("no figure here: " + oldPos)

    def chessboardSquareNotation(self, n, sq_len, listWithFieldNames, swap=False):
        chessBoard = {}
        if swap is True:
            for row in range(self.n):  # Draw each row of the board.
                for col in range(self.n):  # Run through cols drawing squares
                    the_square = (col * sq_len + self.x_offset, row * sq_len + self.y_offset, sq_len, sq_len)
                    dictTmp = {listWithFieldNames[n - row - 1][n - col - 1]: the_square}
                    chessBoard.update(dictTmp)
        else:
            for row in range(self.n):  # Draw each row of the board.
                for col in range(self.n):  # Run through cols drawing squares
                    the_square = (col * sq_len + self.x_offset, row * sq_len + self.y_offset, sq_len, sq_len)
                    dictTmp = {listWithFieldNames[row][col]: the_square}
                    chessBoard.update(dictTmp)

        return chessBoard

    def getNameOfField(self, pos):
        clickedField = ""
        for i in range(0, len(self.fields)):
            for j in range(0, len(self.fields)):
                if self.x_offset + self.square_length  * i < pos[0] < self.x_offset + self.square_length  * (i + 1) and pos[1] > self.y_offset + self.square_length  * j and pos[1] < self.y_offset + self.square_length  * (j + 1):
                    clickedField = self.fields[i][j]

        return clickedField


    def initFigures(self):
        path = 'C:/Users/Admin/PycharmProjects/TicTacToePython/'
        b_bishop = pygame.image.load(path+"figures/b_bishop.png")
        b_horse = pygame.image.load(path+"figures/b_horse.png")
        b_king = pygame.image.load(path+"figures/b_king.png")
        b_queen = pygame.image.load(path+"figures/b_queen.png")
        b_pawn = pygame.image.load(path+"figures/b_pawn.png")
        b_rook = pygame.image.load(path+"figures/b_rook.png")
        w_bishop = pygame.image.load(path+"figures/w_bishop.png")
        w_horse = pygame.image.load(path+"figures/w_horse.png")
        w_king = pygame.image.load(path+"figures/w_king.png")
        w_queen = pygame.image.load(path+"figures/w_queen.png")
        w_pawn = pygame.image.load(path+"figures/w_pawn.png")
        w_rook = pygame.image.load(path+"figures/w_rook.png")
        return [b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king], [w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king]


class ChessPiece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
