from entities.gameboard_entity import Gameboard
from entities.block_entity import Block

class PauseGameInteractor():
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard

    def toggle_pause(self):
        self.game_paused = not self.game_paused
        if self.game_paused:
            self.show_paused_message()
        else:
            self.hide_paused_message()

    def show_paused_message(self):
        if not self.paused_label_id:
            # Utwórz etykietę z informacją o pauzie
            x = self.view.canvas.winfo_width() // 2
            y = self.view.canvas.winfo_height() // 2
            self.paused_label_id = self.view.canvas.create_text(x, y, text="Game Paused", font=("Helvetica", 24),
                                                                fill="red")

            # Dodaj dodatkowy tekst pod głównym napisem
            additional_text = "(Press 'P' to unpause)"
            self.additional_label_id = self.view.canvas.create_text(x, y + 30, text=additional_text,
                                                                    font=("Helvetica", 14), fill="gray")

    def hide_paused_message(self):
        if self.paused_label_id:
            # Usuń etykiety z informacją o pauzie
            self.view.canvas.delete(self.paused_label_id)
            self.paused_label_id = None
            self.view.canvas.delete(self.additional_label_id)
            self.additional_label_id = None