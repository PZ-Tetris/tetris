from entities.gameboard_entity import Gameboard
from entities.block_entity import Block


# TO DO make this work with Game View
class PauseGameInteractor():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.game_paused = False
        self.paused_label_id = None
        self.additional_label_id = None

    def toggle_pause(self, block: Block):
        print("Toggle Pause method called")

        self.game_paused = not self.game_paused
        if self.game_paused:
            self.show_paused_message()
        else:
            self.hide_paused_message()

    def show_paused_message(self):
        if not self.paused_label_id:
            x = self.gameboard.winfo_width() // 2
            y = self.gameboard.winfo_height() // 2
            self.paused_label_id = self.gameboard.create_text(x, y, text="Game Paused", font=("Helvetica", 24),
                                                              fill="red")

            additional_text = "(Press 'P' to unpause)"
            self.additional_label_id = self.gameboard.create_text(x, y + 30, text=additional_text,
                                                                  font=("Helvetica", 14), fill="gray")

    def hide_paused_message(self):
        if self.paused_label_id:
            self.gameboard.delete(self.paused_label_id)
            self.paused_label_id = None
            self.gameboard.delete(self.additional_label_id)
            self.additional_label_id = None
