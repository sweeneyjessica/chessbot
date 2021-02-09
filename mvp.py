import pprint
import pyttsx3
import scipy.io.wavfile as wav
import sounddevice as sd
from wit import Wit

access_token = "WF7LRTYFMA6VOCP7ORHYDDE464DTUC2I"

client = Wit(access_token)

# resp = client.message("rook to c5")
# print("Wit's response: " + str(resp))
#
# with open("Na52.wav", "rb") as f:
#     resp = client.speech(f, {'Content-Type':'audio/wav'})
#
# print("Wit's response: " + str(resp))

sample_rate = 44100
sd.default.samplerate = sample_rate

duration = 6 # record for six seconds

engine = pyttsx3.init()

print("Hit enter to continue, type `stop` to stop.")

while input() != "stop":
    print("recording, say your move...")
    myrecording = sd.rec(duration * sample_rate, channels=1)
    sd.wait()

    wav.write("output_sound.wav", sample_rate, myrecording) # create wav file

    with open("output_sound.wav", "rb") as f:
        resp = client.speech(f, {'Content-Type':'audio/wav'}) # send to wit

    print(resp['text'])
    engine.say(resp['text'])
    engine.runAndWait()

    print("Hit enter to continue, type `stop` to stop.")

