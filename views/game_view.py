import tkinter as tk
import os

from controls.page_button import PageButton
from views.base_view import BaseView
from entities.gameboard_entity import Gameboard
from interactors.generate_next_block import BlockGenerator
from interactors.move_block_interactor import MoveBlockInteractor
from interactors.rotate_block_interactor import RotateBlockInteractor
from interactors.drop_block_interactor import DropBlockInteractor
from interactors.pause_game_interactor import PauseGameInteractor
from entities.block_entity import Block


class GameView(BaseView):
    def __init__(self, controller):
        self.controls_active = True
        self.paused = False
        self.move_block_down_counter = -1
        self.score = 0
        self.frames_delay = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 4, 3, 2, 1]
        self.frame_delay_multiplier = 16.66
        self.level = 0
        self.lines = 0
        self.game_ended = False
        super().__init__(controller)

    def __add_widgets(self):
        self.columnconfigure([0, 1, 2], minsize=165)

        save_button = PageButton(
            self, text="Save result", command=self.controller.save_result)
        restart_button = PageButton(
            self, text="Restart", command=self.controller.restart)
        back_button = PageButton(
            self, text="Home", command=self.controller.back_to_main)

        self.score_label = tk.Label(self, text="Score: 0")

        self.canvas = Gameboard(self, width=350, height=500)
        self.block_generator = BlockGenerator(self.canvas)
        self.move_block_interactor = MoveBlockInteractor(self.canvas)
        self.rotate_block_interactor = RotateBlockInteractor(self.canvas)
        self.drop_block_interactor = DropBlockInteractor(self.canvas)
        self.pause_game_interactor = PauseGameInteractor(self.canvas)
        self.paused = False
        self.controls_active = True

        self.bind_all('<Down>', self.handle_keypress)
        self.bind_all('<Right>', self.handle_keypress)
        self.bind_all('<Left>', self.handle_keypress)
        self.bind_all('<Up>', self.handle_keypress)
        self.bind_all('<space>', self.handle_keypress)
        self.bind_all('<p>', self.pause_game)
        self.bind_all('<P>', self.pause_game)

        save_button.grid(column=0, row=0, sticky='w', pady=10)
        restart_button.grid(column=1, row=0, pady=10)
        back_button.grid(column=2, row=0, sticky='e', pady=10)
        self.score_label.grid(column=1, row=1)
        self.canvas.grid(column=0, columnspan=3, row=2, pady=10)

    def pause_game(self, event=None):
        self.paused = not self.paused
        if self.paused:
            self.controls_active = False
            self.pause_game_interactor.show_paused_message()
            self.move_block_down_counter = -1
        else:
            self.pause_game_interactor.hide_paused_message()
            self.controls_active = True
            self.update()
            self.move_block_down(0)

    def handle_keypress(self, event):
        if self.controls_active:
            if event.keysym == 'Down':
                self.move_block_interactor.move_block_down(event)
                self.score += 1 * (self.level + 1)
            elif event.keysym == 'Right':
                self.move_block_interactor.move_block_right(event)
            elif event.keysym == 'Left':
                self.move_block_interactor.move_block_left(event)
            elif event.keysym == 'Up':
                self.rotate_block_interactor.rotate_block(event)
            elif event.keysym == 'space':
                y1, x1 = self.y_drop_block()
                self.drop_block_interactor.drop_block(event)
                y2, x2 = self.y_drop_block(False, (y1, x1))
                self.score += (y2 - y1) * (self.level + 1)

    def any_key(self, event):
        if self.game_ended:
            self.controller.open_save_score(self.score)

    def update(self):
        if self.game_ended:
            game_over_text = "GAME OVER"
            x = self.canvas.winfo_width() // 2
            y = self.canvas.winfo_height() // 2 - 20
            for offset in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                self.canvas.create_text(x + offset[0], y + offset[1], text=game_over_text, font=("Helvetica", 36), fill="black")
            self.canvas.create_text(x, y, text=game_over_text, font=("Helvetica", 36), fill="red")

            press_any_key_text = "Press any key to continue"
            y = self.canvas.winfo_height() // 2 + 20
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.canvas.create_text(x + offset[0], y + offset[1], text=press_any_key_text, font=("Helvetica", 18), fill="black")
            self.canvas.create_text(x, y, text=press_any_key_text, font=("Helvetica", 18), fill="red")
            return
        if not self.paused:
            # Check if all blocks are inactive
            all_inactive = all(self.canvas.game_matrix[i][j][2] == False
                               for i in range(self.canvas.game_matrix_height)
                               for j in range(self.canvas.game_matrix_width))

            # If all blocks are inactive, generate the next block
            if all_inactive:
                line_detected = True
                start = 19
                line_combo = -1
                while line_detected:
                    line_detected, start = self.line_checker(start)
                    self.drop_blocks_from(start)
                    line_combo += 1
                if line_combo != 0:
                    self.lines += line_combo
                    self.score += (100 + (line_combo - 1) * 200) * (self.level + 1)

                coords = self.get_spawn_blocks_space()
                self.block_generator.generate_next_block()
                if self.do_new_block_overlap(coords):
                    self.end_game()
                self.rotate_block_interactor.rotation_count = 0

            first_criteria = self.level * 10 + 10
            second_criteria = max(100, self.level * 10 - 50)
            if self.lines >= first_criteria:
                self.lines -= first_criteria
                self.level += 1
            elif self.lines >= second_criteria:
                self.lines -= second_criteria
                self.level += 1

            # DEBUG: Print the game matrix to the console
            # os.system('cls' if os.name == 'nt' else 'clear')
            # for i in range(20):
            # print(self.canvas.game_matrix[i])

            self.canvas.delete("all")  # Remove everything from canvas
            self.draw_trace()
            for i in range(self.canvas.game_matrix_height):
                for j in range(self.canvas.game_matrix_width):
                    value, block_type, status = self.canvas.game_matrix[i][j]
                    if value != 0:  # If the block exists
                        x1 = j * self.canvas.block_width
                        y1 = i * self.canvas.block_width
                        x2 = x1 + self.canvas.block_width
                        y2 = y1 + self.canvas.block_width
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=block_type)  # Draw the block

            self.score_label.config(text=f"Score: {self.score}, level: {self.level}, lines: {self.lines}")

            # Schedule the next call of this function in 1/30 second
            self.after(10, self.update)

    def move_block_down(self, counter):
        if self.move_block_down_counter + 1 == counter:
            if 0 <= self.level <= 9:
                delay = int(self.frames_delay[self.level] * self.frame_delay_multiplier)
            elif 10 <= self.level <= 18:
                delay = int(self.frames_delay[10 + (self.level - 10) // 2] * self.frame_delay_multiplier)
            elif 19 <= self.level <= 28:
                delay = int(self.frames_delay[-2] * self.frame_delay_multiplier)
            else:
                delay = int(self.frames_delay[-1] * self.frame_delay_multiplier)

            self.after(delay, lambda: self.move_block_down(counter + 1))
            self.move_block_interactor.move_block_down(None)
            self.move_block_down_counter += 1

    def line_checker(self, start: int = 19):
        for y in range(start, -1, -1):
            line_detected = True
            for x in range(14):
                if not self.canvas.game_matrix[y][x][0]:
                    line_detected = False
                    break
            if line_detected:
                return True, y
        return False, -1

    def y_drop_block(self, active: bool = True, coords: tuple = (0, 0)):
        if active:
            for y in range(20):
                for x in range(14):
                    if self.canvas.game_matrix[y][x][2]:
                        return y, x
        else:
            for y in range(coords[0], 20):
                if self.canvas.game_matrix[y][coords[1]][0]:
                    return y, coords[1]
        return -1, -1

    def draw_trace(self):
        xs = []
        for x in range(14):
            for y in range(20):
                if self.canvas.game_matrix[y][x][2]:
                    xs.append(x)
                    break
        for x in xs:
            x1 = x * self.canvas.block_width
            x2 = x1 + self.canvas.block_width
            y1 = 0
            y2 = self.canvas.height

            self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray', width=0)

    def drop_blocks_from(self, start):
        for y in range(start, 0, -1):
            for x in range(14):
                self.canvas.game_matrix[y][x] = (self.canvas.game_matrix[y - 1][x][0],
                                                 self.canvas.game_matrix[y - 1][x][1],
                                                 self.canvas.game_matrix[y - 1][x][2])

    def get_spawn_blocks_space(self):
        coordinates = []
        for y in range(2):
            for x in range(5, 9):
                if self.canvas.game_matrix[y][x][0] and not self.canvas.game_matrix[y][x][2]:
                    coordinates.append((y, x))
        return coordinates

    def do_new_block_overlap(self, coordinates: list):
        for y, x in coordinates:
            if self.canvas.game_matrix[y][x][2]:
                return True
        return False

    def end_game(self):
        self.game_ended = True
        self.controls_active = False
        self.unbind_all('<Down>')
        self.unbind_all('<Right>')
        self.unbind_all('<Left>')
        self.unbind_all('<Up>')
        self.unbind_all('<space>')
        self.unbind_all('<p>')
        self.unbind_all('<P>')
        self.bind_all('<KeyPress>', self.any_key)

    def present(self):
        self.__add_widgets()
        self.update()
        self.move_block_down(0)
        self.pack()
