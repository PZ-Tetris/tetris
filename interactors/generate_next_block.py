import random

from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class BlockGenerator():
    """Block generator
    """
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.x_starting_point = self.gameboard.width // 2
        self.y_starting_point = 15
        self.block_width = 25
        self.last_block = None
        self.block_types = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']


    def generate_next_block(self):
        """Generate the next, random block

        Returns:
            _type_: Random block
        """
        temp_block_types = [block for block in self.block_types if block != self.last_block]
        next_block = random.choice(temp_block_types)
        self.last_block = next_block

        return self.generate_block(next_block)
    
    def generate_block(self, block_type):
        """Method for generating blocks

        Args:
            block_type (str): block type (I, J, L, O, S, T or Z)

        Returns:
            _type_: block
        """
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
        """Generate I block
        """
        for i in range(4):
            self.gameboard.game_matrix[0][5 + i] = True, 'cyan', True

    def generate_J_block(self):
        """Generate J block
        """
        for i in range(3):
            self.gameboard.game_matrix[1][6 + i] = True, 'blue', True
        self.gameboard.game_matrix[0][6] = True, 'blue', True
    
    def generate_L_block(self):
        """Generate L block
        """
        for i in range(3):
            self.gameboard.game_matrix[1][6 + i] = True, 'orange', True
        self.gameboard.game_matrix[0][8] = True, 'orange', True
    
    def generate_O_block(self):
        """Generate O block
        """
        for i in range(2):
            self.gameboard.game_matrix[i][6] = True, 'yellow', True
        for i in range(2):
            self.gameboard.game_matrix[i][7] = True, 'yellow', True
    
    def generate_S_block(self):
        """Generate S block
        """
        self.gameboard.game_matrix[1][6] = True, 'green', True
        self.gameboard.game_matrix[1][7] = True, 'green', True
        self.gameboard.game_matrix[0][7] = True, 'green', True
        self.gameboard.game_matrix[0][8] = True, 'green', True

    
    def generate_T_block(self):
        """Generate T block
        """
        self.gameboard.game_matrix[0][7] = True, 'purple', True
        self.gameboard.game_matrix[1][6] = True, 'purple', True
        self.gameboard.game_matrix[1][7] = True, 'purple', True
        self.gameboard.game_matrix[1][8] = True, 'purple', True
    
    def generate_Z_block(self):
        """Generate Z block
        """
        self.gameboard.game_matrix[0][6] = True, 'red', True
        self.gameboard.game_matrix[0][7] = True, 'red', True
        self.gameboard.game_matrix[1][7] = True, 'red', True
        self.gameboard.game_matrix[1][8] = True, 'red', True
    