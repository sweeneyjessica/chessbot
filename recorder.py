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


def record():
	blank = {'_text': '', 'entities': {}}
	resp = blank
	while resp == blank:
		sample_rate = 44100
		sd.default.samplerate = sample_rate

		duration = 4  # record for four seconds

		access_token = "WF7LRTYFMA6VOCP7ORHYDDE464DTUC2I"

		client = Wit(access_token)

		print("Go ahead I'm listening...")
		print('-------------------------')
		myrecording = sd.rec(duration * sample_rate, channels=1)
		sd.wait()

		wav.write("output_sound.wav", sample_rate, myrecording)  # create wav file

		with open("output_sound.wav", "rb") as f:
			resp = client.speech(f, {'Content-Type': 'audio/wav'})  # send to wit

		if resp == blank:
			print("Hm, I didn't hear anything. Could you repeat that?")
			continue

	return resp