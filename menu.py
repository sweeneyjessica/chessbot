from recorder import record
from NLU import NLUDefault


def menu(debug=False):

	#initialize NLU for menu
	NLU = NLUDefault()
	opp_level = ''

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
		game_type, opp_type, slots = NLU.parse(game_type)


		if not debug:
			#confirm opponent type
			try:
				print('I heard: "{}". Is that correct?'.format(opp_type))
			except:
				print("I didn't recognize that, can you repeat that?")
				hide_menu = True
				continue

			#listen for input
			resp = record()
			intent,text,slots = NLU.parse(resp)


			if intent == 'confirm':
				if opp_type == 'friend':
					print("Great, Let's get started!")
					print('-------------------------------')
					return opp_type,opp_level
				elif opp_type == 'computer':
					print('What level computer? (easy, medium, or hard)')
					resp = record()
					intent,opp_level,slots = NLU.parse(resp)
					return opp_type,opp_level

			else:
				print("I heard no, so let's start over")
				print('-------------------------------')


