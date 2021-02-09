from wit import Wit

access_token = "WF7LRTYFMA6VOCP7ORHYDDE464DTUC2I"

client = Wit(access_token)

resp = client.message("rook to c5")
print("Wit's response: " + str(resp))

with open("Na5test.wav", "rb") as f:
    resp = client.speech(f, {'Content-Type':'audio/wav'})

print("Wit's response: " + str(resp))
