import random

from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class BlockGenerator():
    def __init__(self, gameboard):
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
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='cyan', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='cyan', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width * 2, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 3,
                                                         fill='cyan', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width * 3, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 4,
                                                         fill='cyan', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_J_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='blue', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='blue', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width * 2, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 3,
                                                         fill='blue', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2 * 3,
                                                         self.y_starting_point + self.block_width * 2, 
                                                         self.x_starting_point - self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 3,
                                                         fill='blue', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_L_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='orange', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='orange', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width * 2, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 3,
                                                         fill='orange', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point + self.block_width // 2,
                                                         self.y_starting_point + self.block_width * 2, 
                                                         self.x_starting_point + self.block_width // 2 * 3, 
                                                         self.y_starting_point + self.block_width * 3,
                                                         fill='orange', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_O_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width,
                                                         self.y_starting_point, 
                                                         self.x_starting_point, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='yellow', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='yellow', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='yellow', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='yellow', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_S_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='green', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='green', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2 * 3,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point - self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='green', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point + self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2 * 3, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='green', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_T_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='purple', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='purple', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2 * 3,
                                                         self.y_starting_point, 
                                                         self.x_starting_point - self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='purple', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point + self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2 * 3, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='purple', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)
    
    def generate_Z_block(self):
        first_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='red', outline='black', width=5)
        second_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='red', outline='black', width=5)
        third_block_id = self.gameboard.create_rectangle(self.x_starting_point + self.block_width // 2,
                                                         self.y_starting_point + self.block_width, 
                                                         self.x_starting_point + self.block_width // 2 * 3, 
                                                         self.y_starting_point + self.block_width * 2,
                                                         fill='red', outline='black', width=5)
        forth_block_id = self.gameboard.create_rectangle(self.x_starting_point - self.block_width // 2 * 3,
                                                         self.y_starting_point, 
                                                         self.x_starting_point - self.block_width // 2, 
                                                         self.y_starting_point + self.block_width,
                                                         fill='red', outline='black', width=5)

        return Block(first_block_id, second_block_id, third_block_id, forth_block_id)