from entities.gameboard_entity import Gameboard
from entities.block_entity import Block
import math


class RotateBlockInteractor():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.rotation_count = 0
        self.block_type = ''

    def rotate_block(self, block: Block):
        # Find the active blocks using the gameboard's attributes
        active_blocks = [(i, j) for i in range(self.gameboard.game_matrix_height)
                         for j in range(self.gameboard.game_matrix_width)
                         if self.gameboard.game_matrix[i][j][2]]

        self.block_type = self.check_type_of_block(active_blocks[0])

        # Rotate block based on its type
        if self.block_type == 'I':
            self.rotate_I_block(active_blocks)
        elif self.block_type == 'J':
            self.rotate_J_block(active_blocks)
        elif self.block_type == 'L':
            self.rotate_L_block(active_blocks)
        elif self.block_type == 'S':
            self.rotate_S_block(active_blocks)
        elif self.block_type == 'T':
            self.rotate_T_block(active_blocks)
        elif self.block_type == 'Z':
            self.rotate_Z_block(active_blocks)

    def check_type_of_block(self, cords):
        block_color = self.gameboard.game_matrix[cords[0]][cords[1]][1]
        if block_color == 'cyan':
            return 'I'
        elif block_color == 'blue':
            return 'J'
        elif block_color == 'orange':
            return 'L'
        elif block_color == 'yellow':
            return 'O'
        elif block_color == 'green':
            return 'S'
        elif block_color == 'purple':
            return 'T'
        elif block_color == 'red':
            return 'Z'
        else:
            return None

    def rotate_I_block(self, active_blocks):
        if self.rotation_count == 0:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[1][0] - 1][active_blocks[1][1] + 1 + y_value] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[2][0] - 2][active_blocks[2][1] - 1 + y_value] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[3][0] - 3][active_blocks[3][1] - 2 + y_value] = True, 'cyan', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 3 + x_value][active_blocks[0][1] + 2] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[1][0] + 2 + x_value][active_blocks[1][1] + 1] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1]] = True, 'cyan', True
            self.gameboard.game_matrix[active_blocks[3][0] + 1 + x_value][active_blocks[3][1] - 1] = True, 'cyan', True
            self.rotation_count = 0

    def rotate_J_block(self, active_blocks):
        if self.rotation_count == 0:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1] + 1 + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[2][0] - 2][active_blocks[2][1] + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[3][0] - 1][active_blocks[3][1] - 1 + y_value] = True, 'blue', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + x_value][active_blocks[0][1] + 1] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[1][0] - 1 + x_value][active_blocks[1][1]] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1] - 1] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[3][0] + 1 + x_value][active_blocks[3][1] - 2] = True, 'blue', True
            self.rotation_count = 2

        elif self.rotation_count == 2:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 1 + y_value] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[3][0] - 2][active_blocks[3][1] - 1 + y_value] = True, 'blue', True
            self.rotation_count = 3

        elif self.rotation_count == 3:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 2 + x_value][active_blocks[0][1] + 1] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[1][0] + 2 + x_value][active_blocks[1][1] + 1] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1]] = True, 'blue', True
            self.gameboard.game_matrix[active_blocks[3][0] + x_value][active_blocks[3][1]] = True, 'blue', True
            self.rotation_count = 0

    def rotate_L_block(self, active_blocks):
        if self.rotation_count == 0:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[1][0] - 1][active_blocks[1][1] - 1 + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[2][0] - 1][active_blocks[2][1] - 1 + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[3][0] - 2][active_blocks[3][1] + y_value] = True, 'orange', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + x_value][active_blocks[0][1]] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[1][0] + x_value][active_blocks[1][1]] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[2][0] + 2 + x_value][active_blocks[2][1] - 1] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[3][0] + x_value][active_blocks[3][1] + 1] = True, 'orange', True
            self.rotation_count = 2

        elif self.rotation_count == 2:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1] + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + 1 + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + y_value] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[3][0] - 1][
                active_blocks[3][1] + 1 + y_value] = True, 'orange', True
            self.rotation_count = 3

        elif self.rotation_count == 3:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + x_value][active_blocks[0][1] - 1] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[1][0] + 1 + x_value][active_blocks[1][1] + 1] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1]] = True, 'orange', True
            self.gameboard.game_matrix[active_blocks[3][0] + 1 + x_value][active_blocks[3][1]] = True, 'orange', True
            self.rotation_count = 0

    def rotate_S_block(self, active_blocks):
        if self.rotation_count == 0:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + y_value] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[2][0] - 1][active_blocks[2][1] + y_value] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[3][0] - 1][active_blocks[3][1] - 2 + y_value] = True, 'green', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + x_value][active_blocks[0][1]] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[1][0] + 1 + x_value][active_blocks[1][1]] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[2][0] + 1 + x_value][active_blocks[2][1] + 2] = True, 'green', True
            self.gameboard.game_matrix[active_blocks[3][0] + x_value][active_blocks[3][1]] = True, 'green', True
            self.rotation_count = 0

    def rotate_T_block(self, active_blocks):
        if self.rotation_count == 0:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 1 + x_value][active_blocks[0][1]] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[1][0] + x_value][active_blocks[1][1]] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[2][0] + 2 + x_value][active_blocks[2][1] - 1] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[3][0] + x_value][active_blocks[3][1]] = True, 'purple', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[3][0] - 1][
                active_blocks[3][1] + 1 + y_value] = True, 'purple', True
            self.rotation_count = 2

        elif self.rotation_count == 2:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + x_value][active_blocks[0][1]] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[1][0] + 1 + x_value][
                active_blocks[1][1] + 1] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1]] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[3][0] + x_value][active_blocks[3][1]] = True, 'purple', True
            self.rotation_count = 3

        elif self.rotation_count == 3:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[2][0] - 1][active_blocks[2][1] + y_value] = True, 'purple', True
            self.gameboard.game_matrix[active_blocks[3][0] - 2][
                active_blocks[3][1] - 1 + y_value] = True, 'purple', True
            self.rotation_count = 0

    def rotate_Z_block(self, active_blocks):
        if self.rotation_count == 0:
            x_value, _, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0] + 1 + x_value][active_blocks[0][1]] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[1][0] + x_value][active_blocks[1][1]] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[2][0] + x_value][active_blocks[2][1]] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[3][0] + 1 + x_value][active_blocks[3][1] - 2] = True, 'red', True
            self.rotation_count = 1

        elif self.rotation_count == 1:
            _, y_value, conditions = self.calculate_conditions(active_blocks)
            if any(conditions):
                return

            self.removing_active_block(active_blocks)

            # Generating new block
            self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + y_value] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[1][0] - 1][active_blocks[1][1] + y_value] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + y_value] = True, 'red', True
            self.gameboard.game_matrix[active_blocks[3][0] - 1][active_blocks[3][1] + 2 + y_value] = True, 'red', True
            self.rotation_count = 0

    # Removing active block to generate rotated
    def removing_active_block(self, active_blocks):
        # Removing old block
        for x, y in active_blocks:
            self.gameboard.game_matrix[x][y] = (False, '', False)

    # Calculating rotating conditions
    def calculate_conditions(self, active_blocks):
        y_coordinates = [y for _, y in active_blocks]
        x_coordinates = [x for x, _ in active_blocks]
        y_value = 0
        x_value = 0
        conditions = ()
        # I-type Block
        if self.block_type == 'I':
            if self.rotation_count == 0:
                if min(y_coordinates) == 0:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 2][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 3][0],)
                    y_value = 2
                elif min(y_coordinates) == 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 2][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                    y_value = 1
                elif max(y_coordinates) == self.gameboard.game_matrix_width - 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 2][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 3][0],)
                    y_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 2][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 1:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 2][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 3][active_blocks[0][1]][0],)
                    x_value = -3
                elif max(x_coordinates) == self.gameboard.game_matrix_height - 2:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 2][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1]][0],)
                    x_value = -2
                elif max(x_coordinates) == self.gameboard.game_matrix_height - 3:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] - 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 2][active_blocks[0][1]][0],)
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 1][active_blocks[2][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 2][active_blocks[2][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 3][active_blocks[2][1]][0],)
                return x_value, y_value, conditions
        # J-type Block
        elif self.block_type == 'J':
            if self.rotation_count == 0:
                if max(y_coordinates) == self.gameboard.game_matrix_width - 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 2][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] - 2][0],)
                    y_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] - 1][active_blocks[2][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] - 2][active_blocks[2][1]][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 1:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 2][active_blocks[2][1]][0],)
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 1][active_blocks[1][1]][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 2:
                if min(y_coordinates) == 0:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 2][0],)
                    y_value = 1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 1][active_blocks[1][1]][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 3:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 1][active_blocks[1][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 1][0],)
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 2][active_blocks[1][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[3][0] + 1][active_blocks[3][1]][0],)
                return x_value, y_value, conditions
        # L-type Block
        elif self.block_type == 'L':
            if self. rotation_count == 0:
                if min(y_coordinates) == 0:
                    y_value = 1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[1][1] - 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] - 1][0],)
                return x_value, y_value, conditions
            elif self. rotation_count == 1:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 1][active_blocks[1][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 2][active_blocks[1][1]][0],)
                return x_value, y_value, conditions
            elif self. rotation_count == 2:
                if max(y_coordinates) == self.gameboard.game_matrix_width - 1:
                    y_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] - 1][0],)
                return x_value, y_value, conditions
            elif self. rotation_count == 3:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 1][active_blocks[2][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] - 1][active_blocks[2][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[3][0] + 1][active_blocks[3][1]][0],)
                return x_value, y_value, conditions
        # S-type Block
        elif self.block_type == 'S':
            if self.rotation_count == 0:
                if min(y_coordinates) == 0:
                    y_value = 1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0]][active_blocks[1][1] - 1][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 1:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 1][active_blocks[1][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[1][0] + 2][active_blocks[1][1]][0],)
                return x_value, y_value, conditions
        # T-type Block
        elif self.block_type == 'T':
            if self.rotation_count == 0:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[3][0] + 1][active_blocks[3][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[3][0]][active_blocks[3][1] - 1][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 1:
                if max(y_coordinates) == self.gameboard.game_matrix_width - 1:
                    y_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 1][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 2:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0] + 1][active_blocks[2][1]][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 3:
                if min(y_coordinates) == 0:
                    y_value = 1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] + 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                return x_value, y_value, conditions
        # Z-type Block
        elif self.block_type == 'Z':
            if self.rotation_count == 0:
                if max(x_coordinates) == self.gameboard.game_matrix_height - 1:
                    x_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 1][active_blocks[0][1]][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0] + 2][active_blocks[0][1]][0],)
                return x_value, y_value, conditions
            elif self.rotation_count == 1:
                if max(y_coordinates) == self.gameboard.game_matrix_width - 1:
                    y_value = -1
                else:
                    conditions += (self.gameboard.game_matrix[active_blocks[0][0]][active_blocks[0][1] - 1][0],)
                    conditions += (self.gameboard.game_matrix[active_blocks[2][0]][active_blocks[2][1] + 1][0],)
                return x_value, y_value, conditions
