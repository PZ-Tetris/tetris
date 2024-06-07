import os

from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class DropBlockInteractor():
    """Interactor for drop block game logic
    """
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard

    def drop_block(self, block: Block):
        """Drop the block to the game view

        Args:
            block (Block): block element
        """
        # Check if any move is possible
        can_move = True
        while can_move:
            lowest_active_blocks = []
            for j in range(self.gameboard.game_matrix_width):
                for i in reversed(range(self.gameboard.game_matrix_height)):
                    if self.gameboard.game_matrix[i][j][2]:
                        lowest_active_blocks.append((i, j))
                        break  # Break the inner loop when you find an active block

            can_move = all(i + 1 < self.gameboard.game_matrix_height and not self.gameboard.game_matrix[i + 1][j][0]
                        for i, j in lowest_active_blocks)

            active_blocks = [(i, j) for i in range(self.gameboard.game_matrix_height) 
                            for j in range(self.gameboard.game_matrix_width) 
                            if self.gameboard.game_matrix[i][j][2]]
            if can_move:
                # Move blocks down
                for j in range(self.gameboard.game_matrix_width):
                    for i in reversed(range(self.gameboard.game_matrix_height)):  # We move from bottom to top
                        if self.gameboard.game_matrix[i][j][2] and i + 1 < self.gameboard.game_matrix_height:  # We add a condition to prevent exceeding the lower boundary
                            value, block_type, status = self.gameboard.game_matrix[i][j]
                            # Move the block down
                            self.gameboard.game_matrix[i + 1][j] = self.gameboard.game_matrix[i][j]
                            self.gameboard.game_matrix[i][j] = (False, '', False)  # Remove the old block

        # Set the active blocks to inactive
        for i, j in active_blocks:
            value, block_type, status = self.gameboard.game_matrix[i][j]
            self.gameboard.game_matrix[i][j] = (value, block_type, False)