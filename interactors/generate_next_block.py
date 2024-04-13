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

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 3],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 3, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 4]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='cyan', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)

    def generate_J_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 3],
            [self.x_starting_point - self.block_width // 2 * 3, self.y_starting_point + self.block_width * 2, self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 3]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='blue', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)
    
    def generate_L_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 3],
            [self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2, self.x_starting_point + self.block_width // 2 * 3, self.y_starting_point + self.block_width * 3]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='orange', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)
    
    def generate_O_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width, self.y_starting_point, self.x_starting_point, self.y_starting_point + self.block_width],
            [self.x_starting_point, self.y_starting_point, self.x_starting_point + self.block_width, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width, self.y_starting_point + self.block_width, self.x_starting_point, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width, self.y_starting_point + self.block_width * 2]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='yellow', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)
    
    def generate_S_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2 * 3, self.y_starting_point + self.block_width, self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point + self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2 * 3, self.y_starting_point + self.block_width]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='green', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)

    
    def generate_T_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2 * 3, self.y_starting_point + self.block_width, self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2 * 3, self.y_starting_point + self.block_width * 2]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='purple', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)
    
    def generate_Z_block(self):

        blocks_coords = [
            [self.x_starting_point - self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width],
            [self.x_starting_point - self.block_width // 2 * 3, self.y_starting_point + self.block_width, self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point - self.block_width // 2, self.y_starting_point + self.block_width, self.x_starting_point + self.block_width // 2, self.y_starting_point + self.block_width * 2],
            [self.x_starting_point + self.block_width // 2, self.y_starting_point, self.x_starting_point + self.block_width // 2 * 3, self.y_starting_point + self.block_width]
        ]

        blocks_ids = [self.gameboard.create_rectangle(*block_coord, fill='red', outline='black', width=5) for block_coord in blocks_coords]
        return Block(blocks_ids)
    