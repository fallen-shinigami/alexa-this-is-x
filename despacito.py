#I did a thing

import webbrowser

dict1 = {
'speedos' : 'https://www.youtube.com/watch?v=ZPm3FSTbrQ4',
'sad' : 'https://soundcloud.com/luisfonsiofficial/despacito',
'spicy' : 'https://www.youtube.com/watch?v=TrZk3igdICc',
'beefy' : 'https://www.youtube.com/watch?v=LYhF9ZRjVek',
'cancer' : 'https://www.youtube.com/watch?v=W3GrSMYbkBE',
'minecraft' : 'https://www.youtube.com/watch?v=Gl6ekgobG2k',
'pokemon' : 'https://www.youtube.com/watch?v=MFCD2cahGoA',
'english' : 'https://youtu.be/TVudARY3SD4?t=54',
'trump' : 'https://www.youtube.com/watch?v=X3q9RdU3he0',
'roblox' : 'https://www.youtube.com/watch?v=A6I3U4iLITQ',
'america' : 'https://youtu.be/6cmg75bgkkg',
'a chicken wing' : 'https://youtu.be/tLUaycJFjWA',
'dragonball' : 'https://www.youtube.com/watch?v=lRavzcSnS9U',
'google translate' : 'https://www.youtube.com/watch?v=A57Awp0Lz48',
'windows update' : 'https://www.youtube.com/watch?v=QHdZjxrG35U'
}

def despacito_2(alexa):
		if alexa in dict1:
			return webbrowser.open(dict1[alexa], new=2)
		else:
			return print('dank MeMe does not exist')

alexa = input("Alexa, this is ")
despacito_2(alexa)