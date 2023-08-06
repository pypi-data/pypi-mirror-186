import pygame as pyg
import os
import sys
import math

class Pawn:
    def __init__(self, PieceColor : str, x : int, y : int):
        if PieceColor == 'b':
            self.spriteImage = pyg.transform.scale(pyg.image.load("Assets/PawnBlackImage.png"), (60, 60))
        else:
            self.spriteImage = pyg.transform.scale(pyg.image.load("Assets/PawnWhiteImage.png"), (60, 60))
        self.spriteRect = self.spriteImage.get_rect()
        self.spriteRect.center = (x, y)
