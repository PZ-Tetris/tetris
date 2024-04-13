import tkinter as tk
from enum import Enum


class BlockColor(Enum):
    CYAN = 0
    BLUE = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    PINK = 5
    RED = 6


class GameCanvas(tk.Canvas):
    def __init__(self, parent,
                 background: str,
                 board_width: int = 10,
                 board_height: int = 20,
                 block_size: int = 50):

        self._board_width = board_width
        self._board_height = board_height
        self._block_size = block_size
        self._blocks_grid = [[[None for _ in range(4)] for _ in range(board_height)] for _ in range(board_width)]
        self._block_border = round(block_size * 0.15)
        self._template_color_string = '#%02x%02x%02x'

        width = board_width * block_size
        height = board_height * block_size
        super().__init__(parent, width=width, height=height, background=background)

    def _draw_block(self, x_position: int, y_position: int, color: BlockColor):
        if color == BlockColor.CYAN:
            color_main, color_top, color_side, color_bottom = '#00f0f0', '#99ffff', '#00d8d8', '#007878'
        elif color == BlockColor.BLUE:
            color_main, color_top, color_side, color_bottom = '#0000f0', '#9999ff', '#0000d8', '#000078'
        elif color == BlockColor.ORANGE:
            color_main, color_top, color_side, color_bottom = '#f0a000', '#ffdd99', '#d89000', '#785000'
        elif color == BlockColor.YELLOW:
            color_main, color_top, color_side, color_bottom = '#f0f000', '#ffff99', '#d8d800', '#787800'
        elif color == BlockColor.GREEN:
            color_main, color_top, color_side, color_bottom = '#00f000', '#99ff99', '#00d800', '#007800'
        elif color == BlockColor.PINK:
            color_main, color_top, color_side, color_bottom = '#f000f0', '#ff99ff', '#d800d8', '#780078'
        else:
            color_main, color_top, color_side, color_bottom = '#f00000', '#ff9999', '#d80000', '#780000'

        # somehow the pixels are drawn with 2 pixels offset (maybe border?)
        x1 = x_position * self._block_size + 2
        y1 = y_position * self._block_size + 2
        x2 = x1 + self._block_size
        y2 = y1 + self._block_size

        x_center = (x1 + x2) // 2
        y_center = (y1 + y2) // 2

        self._blocks_grid[x_position][y_position][0] = self.create_polygon(x1, y1, x1, y2, x2, y1, x2, y2,
                            fill=color_side,
                            width=0)

        self._blocks_grid[x_position][y_position][1] = self.create_polygon(x1, y1, x2, y1, x_center, y_center,
                            fill=color_top,
                            width=0)

        self._blocks_grid[x_position][y_position][2] = self.create_polygon(x1, y2, x2, y2, x_center, y_center,
                            fill=color_bottom,
                            width=0)

        self._blocks_grid[x_position][y_position][3] = self.create_rectangle(x1 + self._block_border,
                              y1 + self._block_border,
                              x2 - self._block_border,
                              y2 - self._block_border,
                              fill=color_main,
                              width=0)

    def _remove_block(self, x: int, y: int):
        for i in range(4):
            if self._blocks_grid[x][y][i] is not None:
                self.delete(self._blocks_grid[x][y][i])
                self._blocks_grid[x][y][i] = None

    def update_grid(self, data: list):
        for y, line in enumerate(data):
            for x in range(self._board_width):
                if line[x] is not None:
                    self._remove_block(x, y)
                    self._draw_block(x, y, line[x])
                else:
                    self._remove_block(x, y)
