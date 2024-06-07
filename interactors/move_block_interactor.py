from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class MoveBlockInteractor():
    """Move block logic interactor
    """
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard

    def move_block_down(self, block: Block):
        """Move the block down

        Args:
            block (Block): block element
        """
        # Find the lowest active blocks in each column
        lowest_active_blocks = []
        for j in range(self.gameboard.game_matrix_width):
            for i in reversed(range(self.gameboard.game_matrix_height)):
                if self.gameboard.game_matrix[i][j][2]:
                    lowest_active_blocks.append((i, j))
                    break  # Break the inner loop when you find an active block

        # Check if any move is possible
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
        else:
            # Set the active blocks to inactive
            for i, j in active_blocks:
                value, block_type, status = self.gameboard.game_matrix[i][j]
                self.gameboard.game_matrix[i][j] = (value, block_type, False)

    def move_block_left(self, block: Block):
        """Move the block to the left

        Args:
            block (Block): block element
        """
        # Find the most left active blocks in each row
        leftmost_active_blocks = []
        for i in range(self.gameboard.game_matrix_height):
            for j in range(self.gameboard.game_matrix_width):
                if self.gameboard.game_matrix[i][j][2]:
                    leftmost_active_blocks.append((i, j))
                    break  # Break the inner loop when you find an active block

        # Check if any move is possible
        can_move = all(j - 1 >= 0 and not self.gameboard.game_matrix[i][j - 1][0]
                    for i, j in leftmost_active_blocks)
        
        active_blocks = [(i, j) for i in range(self.gameboard.game_matrix_height) 
                                for j in range(self.gameboard.game_matrix_width) 
                                if self.gameboard.game_matrix[i][j][2]]
        if can_move:
            # Move blocks to the left
            for i, j in active_blocks:
                if j - 1 >= 0:  # We add a condition to prevent exceeding the left boundary
                    value, block_type, status = self.gameboard.game_matrix[i][j]
                    # Move the block to the left
                    self.gameboard.game_matrix[i][j - 1] = self.gameboard.game_matrix[i][j]
                    self.gameboard.game_matrix[i][j] = (False, '', False)  # Remove the old block

    def move_block_right(self, block: Block):
        """Move block to the right

        Args:
            block (Block): block element
        """
        # Find the most right active blocks in each row
        rightmost_active_blocks = []
        for i in range(self.gameboard.game_matrix_height):
            for j in reversed(range(self.gameboard.game_matrix_width)):
                if self.gameboard.game_matrix[i][j][2]:
                    rightmost_active_blocks.append((i, j))
                    break  # Break the inner loop when you find an active block

        # Check if any move is possible
        can_move = all(j + 1 < self.gameboard.game_matrix_width and not self.gameboard.game_matrix[i][j + 1][0]
                    for i, j in rightmost_active_blocks)

        active_blocks = [(i, j) for i in range(self.gameboard.game_matrix_height) 
                        for j in range(self.gameboard.game_matrix_width) 
                        if self.gameboard.game_matrix[i][j][2]]

        if can_move:
            # Move blocks to the right
            for i in range(self.gameboard.game_matrix_height):
                for j in reversed(range(self.gameboard.game_matrix_width)):  # We move from right to left
                    if self.gameboard.game_matrix[i][j][2] and j + 1 < self.gameboard.game_matrix_width:  # We add a condition to prevent exceeding the right boundary
                        value, block_type, status = self.gameboard.game_matrix[i][j]
                        # Move the block to the right
                        self.gameboard.game_matrix[i][j + 1] = self.gameboard.game_matrix[i][j]
                        self.gameboard.game_matrix[i][j] = (False, '', False)  # Remove the old block