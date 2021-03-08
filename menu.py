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


def menu():
	#blank recording
	blank = {'_text': '', 'entities': {}}

	startover = True
	hide_menu = False
	while startover:

		if not hide_menu:
			print('Welcome! My name is ChessBuddy! How should we play chess today?')
			print('Play a game against a...')
			print('1-friend')
			print('2-computer')


		#listen for input
		game_type = record()
		try:
			opp_type = game_type['entities']['opponent:opponent'][0]['body']
			print('I heard: "{}". Is that correct?'.format(opp_type))
		except:
			print("I didn't recognize that, can you repeat that?")
			hide_menu = True
			continue

		#listen for input
		resp = record()

		if resp['intents'][0]['name'] == 'confirm':
			print("Great, Let's get started!")
			print('-------------------------------')
			return opp_type
		else:
			print("I heard no, so let's start over")
			print('-------------------------------')


