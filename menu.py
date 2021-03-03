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


#blank recording
blank = {'_text': '', 'entities': {}}

startover = True

while startover:
	print('Welcome! My name is ChessBuddy! How should we play chess today?')
	print('Play a game against a...')
	print('1-friend')
	print('2-computer')


	#listen for input
	resp = record()

	try:
		opp_type = resp['entities']['opponent:opponent'][0]['body']
	except:
		print("I didn't recognize that, can you repeat that?")

	print('I heard: "{}". Is that correct?'.format(opp_type))

	#listen for input
	resp = record()

	if resp['intents'][0]['name'] == 'confirm':
		print("Great, Let's get started!")
		print('-------------------------------')
		startover = False
	else:
		print("I heard no, so let's start over")
		print('-------------------------------')
