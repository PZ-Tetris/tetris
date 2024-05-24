from entities.gameboard_entity import Gameboard
from entities.block_entity import Block


class RotateBlockInteractor:
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.rotation_count = 0
        self.block_type = ''

        self.I_matrix = [[False, False, False, False, False],
                         [False, False, False, False, False],
                         [False, True, True, True, True],
                         [False, False, False, False, False],
                         [False, False, False, False, False], 'cyan']

        self.J_matrix = [[True, False, False],
                         [True, True, True],
                         [False, False, False], 'blue']

        self.L_matrix = [[False, False, True],
                         [True, True, True],
                         [False, False, False], 'orange']

        self.O_matrix = [[True, True],
                         [True, True], 'yellow']

        self.S_matrix = [[False, True, True],
                         [True, True, False],
                         [False, False, False], 'green']

        self.T_matrix = [[False, True, False],
                         [True, True, True],
                         [False, False, False], 'purple']

        self.Z_matrix = [[True, True, False],
                         [False, True, True],
                         [False, False, False], 'red']

        self.matrix_dict = {'I': self.I_matrix,
                            'J': self.J_matrix,
                            'L': self.L_matrix,
                            'O': self.O_matrix,
                            'S': self.S_matrix,
                            'T': self.T_matrix,
                            'Z': self.Z_matrix}

        # data taken from website: https://tetris.wiki/Super_Rotation_System#Wall_Kicks
        # (x, y) - +x: right, +y: up
        self.JLSTZ_wall_kick_data = [[(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],
                                     [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],
                                     [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],
                                     [(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],
                                     [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)],
                                     [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)],
                                     [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)],
                                     [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)]]

        self.I_wall_kick_data = [[(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)],
                                 [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
                                 [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)],
                                 [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)],
                                 [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
                                 [(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)],
                                 [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)],
                                 [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)]]

    def generate_tetromino(self, center: tuple):
        matrix = self.matrix_dict.get(self.block_type)

        size = len(matrix[0])
        offset = size // 2 if self.block_type != 'O' else 0

        if self.rotation_count == 0:
            for y in range(size):
                for x in range(size):
                    if matrix[y][x]:
                        self.gameboard.game_matrix[center[0] + y - offset][center[1] + x - offset] = True, matrix[
                            -1], True
        elif self.rotation_count == 1:
            for y in range(size):
                for x in range(size):
                    if matrix[size - x - 1][y]:
                        self.gameboard.game_matrix[center[0] + y - offset][center[1] + x - offset] = True, matrix[
                            -1], True
        elif self.rotation_count == 2:
            for y in range(size):
                for x in range(size):
                    if matrix[size - y - 1][size - x - 1]:
                        self.gameboard.game_matrix[center[0] + y - offset][center[1] + x - offset] = True, matrix[
                            -1], True
        else:
            for y in range(size):
                for x in range(size):
                    if matrix[x][size - y - 1]:
                        self.gameboard.game_matrix[center[0] + y - offset][center[1] + x - offset] = True, matrix[
                            -1], True

    def tetromino_center(self, active_blocks: list):
        left_corner_y = min(coord[0] for coord in active_blocks)
        left_corner_x = min(coord[1] for coord in active_blocks)

        if self.block_type == 'I':
            if self.rotation_count == 0:
                return left_corner_y, left_corner_x + 1
            elif self.rotation_count == 1:
                return left_corner_y + 1, left_corner_x
            elif self.rotation_count == 2:
                return left_corner_y, left_corner_x + 2
            elif self.rotation_count == 3:
                return left_corner_y + 2, left_corner_x
        elif self.block_type != 'O':
            if self.rotation_count == 0 or self.rotation_count == 3:
                return left_corner_y + 1, left_corner_x + 1
            elif self.rotation_count == 1:
                return left_corner_y + 1, left_corner_x
            elif self.rotation_count == 2:
                return left_corner_y, left_corner_x + 1
        return left_corner_y, left_corner_x

    def can_rotate(self, center: tuple, clockwise_rotation: bool = True):
        matrix = self.matrix_dict.get(self.block_type)

        size = len(matrix[0])
        offset = size // 2 if self.block_type != 'O' else 0

        anticlockwise_offset = 0 if clockwise_rotation else 1
        if clockwise_rotation:
            next_rotation = (self.rotation_count + 1) % 4
        else:
            next_rotation = (self.rotation_count - 1) % 4

        for wall_kick_no in range(5):
            if self.block_type == 'I':
                wall_kick = self.I_wall_kick_data[next_rotation * 2 + anticlockwise_offset][wall_kick_no]
            else:
                wall_kick = self.JLSTZ_wall_kick_data[next_rotation * 2 + anticlockwise_offset][wall_kick_no]
            break_loop = False
            if next_rotation == 0:
                for y in range(size):
                    if break_loop:
                        break
                    for x in range(size):
                        if matrix[y][x]:
                            coord_y = center[0] + y - offset - wall_kick[1]
                            coord_x = center[1] + x - offset + wall_kick[0]
                            if ((not 0 <= coord_x <= 13 or not 0 <= coord_y <= 19) or
                                    (self.gameboard.game_matrix[coord_y][coord_x][0] and not
                                     self.gameboard.game_matrix[coord_y][coord_x][2])):
                                break_loop = True
                                break
            elif next_rotation == 1:
                for y in range(size):
                    if break_loop:
                        break
                    for x in range(size):
                        if matrix[size - x - 1][y]:
                            coord_y = center[0] + y - offset - wall_kick[1]
                            coord_x = center[1] + x - offset + wall_kick[0]
                            if ((not 0 <= coord_x <= 13 or not 0 <= coord_y <= 19) or
                                    (self.gameboard.game_matrix[coord_y][coord_x][0] and not
                                     self.gameboard.game_matrix[coord_y][coord_x][2])):
                                break_loop = True
                                break
            elif next_rotation == 2:
                for y in range(size):
                    if break_loop:
                        break
                    for x in range(size):
                        if matrix[size - y - 1][size - x - 1]:
                            coord_y = center[0] + y - offset - wall_kick[1]
                            coord_x = center[1] + x - offset + wall_kick[0]
                            if ((not 0 <= coord_x <= 13 or not 0 <= coord_y <= 19) or
                                    (self.gameboard.game_matrix[coord_y][coord_x][0] and not
                                     self.gameboard.game_matrix[coord_y][coord_x][2])):
                                break_loop = True
                                break
            else:
                for y in range(size):
                    if break_loop:
                        break
                    for x in range(size):
                        if matrix[x][size - y - 1]:
                            coord_y = center[0] + y - offset - wall_kick[1]
                            coord_x = center[1] + x - offset + wall_kick[0]
                            if ((not 0 <= coord_x <= 13 or not 0 <= coord_y <= 19) or
                                    (self.gameboard.game_matrix[coord_y][coord_x][0] and not
                                     self.gameboard.game_matrix[coord_y][coord_x][2])):
                                break_loop = True
                                break
            if not break_loop:
                return True, (-wall_kick[1], wall_kick[0])
        return False, (-1, -1)

    def rotate_block(self, block: Block):
        # Find the active blocks using the gameboard's attributes
        active_blocks = [(i, j) for i in range(self.gameboard.game_matrix_height)
                         for j in range(self.gameboard.game_matrix_width)
                         if self.gameboard.game_matrix[i][j][2]]

        center = self.tetromino_center(active_blocks)

        new_block_type = self.check_type_of_block(active_blocks[0])
        if self.block_type != new_block_type:
            self.block_type = new_block_type
            self.rotation_count = 0

        rotation_data = self.can_rotate(center)
        if rotation_data[0]:
            self.rotation_count = (self.rotation_count + 1) % 4
            self.removing_active_block(active_blocks)
            self.generate_tetromino((center[0] + rotation_data[1][0], center[1] + rotation_data[1][1]))

        return

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

    # Removing active block to generate rotated
    def removing_active_block(self, active_blocks):
        # Removing old block
        for x, y in active_blocks:
            self.gameboard.game_matrix[x][y] = (False, '', False)
