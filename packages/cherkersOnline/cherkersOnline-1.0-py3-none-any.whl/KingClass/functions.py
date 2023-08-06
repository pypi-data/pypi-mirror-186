import pygame as pyg
import os
import sys
import math

class King:
    def __init__(self, PieceColor : str, x : int, y : int):
        if PieceColor == 'b':
            self.spriteImage = pyg.image.load("Assets/KingBlackImage.png")
        else:
            self.spriteImage = pyg.image.load("Assets/KingWhiteImage.png")
        self.spriteRect = self.spriteImage.get_rect()
        self.spriteRect.center = (x, y)
