from wit import Wit
import scipy.io.wavfile as wav
import os

access_token = "WF7LRTYFMA6VOCP7ORHYDDE464DTUC2I"

client = Wit(access_token)

#for file in os.listdir("../chessbot_audio_piece_square"):
 #   file = "./chessbot_audio_piece_square/{}".format(file)

for file in os.listdir():
    if file == "batch_submit.py" or file == "submitted" or file == ".DS_Store":
        continue

    with open(file, "rb") as f:
        print(file)
        resp = client.speech(f, {'Content-Type':'audio/wav'}) # send to wit

    os.rename(file, "submitted/{}".format(file))
    print(resp['text'])
