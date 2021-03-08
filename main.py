from engine import Computer
import chess
import chess.svg
import time
import sys
import webbrowser
import sounddevice as sd
import scipy.io.wavfile as wav
from wit import Wit
import time
from recorder import record
from menu import menu
from interface import play_game


if __name__ == '__main__':
	game_type = menu()

	#launch game
	play_game(game_type)
