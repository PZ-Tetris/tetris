from controllers.game_mode_controller import GameModeController
from controllers.leaderboard_controller import LeaderBoardController
from controllers.about_controller import AboutController
from controllers.instruction_controller import InstructionController
from helpers.sound_manager import MusicType, SoundManager
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.view = MainView(self)
        self.model = None
        self.sound_manager = SoundManager()
        self.sound_manager.play_music(MusicType.MENU)

    def open_leaderboard(self):
        """On click handler for displaying leaderboard view
        """
        ctrl = LeaderBoardController(self.view)
        ctrl.view.present()
        self.view.clear()

    def open_game_mode_selection(self):
        """On click handler for displaying game mode selection view
        """
        ctrl = GameModeController(self.view)
        ctrl.view.present()
        self.view.clear()

    def open_about(self):
        """On click handler for displaying game view
        """
        ctrl = AboutController(self.view)
        ctrl.view.present()
        self.view.clear()

    def open_instruction(self):
        """On click handler for displaying instruction view
        """
        ctrl = InstructionController(self.view)
        ctrl.view.present()
        self.view.clear()
