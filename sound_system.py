from playsound import playsound
from threading import Thread

class Sound:
    def __init__(self, enable=True):
        self.enable = enable

    def play_eat_apple(self):
        if self.enable:
            Thread(target=playsound, args=('coin.wav',)).start()

    def play_game_over(self):
        if self.enable:
            Thread(target=playsound, args=('bruh.mp3',)).start()