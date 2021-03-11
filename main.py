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
from interface import FrameDM
from NLU import NLUDefault
from NLG import NLGDefault


if __name__ == '__main__':

	#initialize objects
	NLU = NLUDefault()
	NLG = NLGDefault()

	game_type,opp_level = menu(debug=False)
	#game_type = 'computer'

	
	DialogManager = FrameDM(NLU, NLG)


	#launch game
	DialogManager.play_game(game_type,opp_level)
