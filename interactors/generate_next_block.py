import random

from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class BlockGenerator():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.x_starting_point = self.gameboard.width // 2
        self.y_starting_point = 15
        self.block_width = 25
        self.last_block = None
        self.block_types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']


    def generate_next_block(self):
        temp_block_types = [block for block in self.block_types if block != self.last_block]
        next_block = random.choice(temp_block_types)
        self.last_block = next_block

        return self.generate_block(next_block)
    
    def generate_block(self, block_type):
        if block_type == 'I':
            return self.generate_I_block()
        elif block_type == 'J':
            return self.generate_J_block()
        elif block_type == 'L':
            return self.generate_L_block()
        elif block_type == 'O':
            return self.generate_O_block()
        elif block_type == 'S':
            return self.generate_S_block()
        elif block_type == 'T':
            return self.generate_T_block()
        elif block_type == 'Z':
            return self.generate_Z_block()
        else:
            return None
        
    def generate_I_block(self):

        for i in range(4):
            self.gameboard.game_matrix[i][7] = 1, 'cyan', 'a'

    def generate_J_block(self):

        for i in range(3):
            self.gameboard.game_matrix[i][7] = 1, 'blue', 'a'
        self.gameboard.game_matrix[2][6] = 1, 'blue', 'a'
    
    def generate_L_block(self):

        for i in range(3):
            self.gameboard.game_matrix[i][6] = 1, 'orange', 'a'
        self.gameboard.game_matrix[2][7] = 1, 'orange', 'a'
    
    def generate_O_block(self):

        for i in range(2):
            self.gameboard.game_matrix[i][6] = 1, 'yellow', 'a'
        for i in range(2):
            self.gameboard.game_matrix[i][7] = 1, 'yellow', 'a'
    
    def generate_S_block(self):

        self.gameboard.game_matrix[0][6] = 1, 'green', 'a'
        self.gameboard.game_matrix[1][6] = 1, 'green', 'a'
        self.gameboard.game_matrix[1][7] = 1, 'green', 'a'
        self.gameboard.game_matrix[2][7] = 1, 'green', 'a'

    
    def generate_T_block(self):

        self.gameboard.game_matrix[0][5] = 1, 'purple', 'a'
        self.gameboard.game_matrix[0][6] = 1, 'purple', 'a'
        self.gameboard.game_matrix[0][7] = 1, 'purple', 'a'
        self.gameboard.game_matrix[1][6] = 1, 'purple', 'a'
    
    def generate_Z_block(self):

        self.gameboard.game_matrix[0][6] = 1, 'red', 'a'
        self.gameboard.game_matrix[0][7] = 1, 'red', 'a'
        self.gameboard.game_matrix[1][7] = 1, 'red', 'a'
        self.gameboard.game_matrix[1][8] = 1, 'red', 'a'
    