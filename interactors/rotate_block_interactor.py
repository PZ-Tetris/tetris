from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class RotateBlockInteractor():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard

    def rotate_block(self, block: Block):
        print('rotate')