import enum
import pygame

class MusicType(enum.Enum):
    MENU = 1
    STANDARD = 2
    RANDOM = 3
    OVER = 4

class SoundManager:
    """Sound manager class
    """
    def __init__(self):
        pygame.mixer.init()
        self.hover_sound = pygame.mixer.Sound('./assets/button_hover.wav')
        self.click_sound = pygame.mixer.Sound('./assets/button_click.wav')
        self.button_channel = pygame.mixer.Channel(0)
        self.music_channel = pygame.mixer.Channel(1)

    def play_hover_sound(self):
        """Method for playing hover game sound
        """
        if not self.button_channel.get_busy():
            self.button_channel.play(self.hover_sound)

    def play_click_sound(self):
        """Method for playing click game sound
        """
        if not self.button_channel.get_busy():
            self.button_channel.play(self.click_sound)

    def play_music(self, music_type):
        """Method for playing in-game music

        Args:
            music_type (MusicType): type of the music to be played
        """
        if music_type == MusicType.MENU:
            pygame.mixer.music.load('./assets/punch_out.wav')
        elif music_type == MusicType.STANDARD:
            pygame.mixer.music.load('./assets/press_play.wav')
        elif music_type == MusicType.RANDOM:
            pygame.mixer.music.load('./assets/voyage.wav')
        elif music_type == MusicType.OVER:
            pygame.mixer.music.load('./assets/continue.wav')
        pygame.mixer.music.play(-1)

    def pause_music(self):
        """Pause the currently played track
        """
        pygame.mixer.music.pause()

    def unpause_music(self):
        """Start the currently paused track
        """
        pygame.mixer.music.unpause()
