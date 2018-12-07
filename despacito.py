#I did a thing

import webbrowser


def despacito(alexa):
	if alexa == "sad":
		return webbrowser.open("https://soundcloud.com/luisfonsiofficial/despacito", new=2)
	elif alexa == "spicy":
		return webbrowser.open("https://www.youtube.com/watch?v=TrZk3igdICc", new=2)
	elif alexa == "beefy":
		return webbrowser.open("https://www.youtube.com/watch?v=LYhF9ZRjVek", new=2)
	elif alexa == "cancer":
		return webbrowser.open("https://www.youtube.com/watch?v=W3GrSMYbkBE", new=2)        
	elif alexa == "minecraft":
		return webbrowser.open("https://www.youtube.com/watch?v=Gl6ekgobG2k", new=2)  
	elif alexa == "english":
		return webbrowser.open("https://youtu.be/TVudARY3SD4?t=54", new=2)  		
	elif alexa == "trump":
		return webbrowser.open("https://www.youtube.com/watch?v=X3q9RdU3he0", new=2)
	elif alexa == "roblox":
		return webbrowser.open("https://www.youtube.com/watch?v=A6I3U4iLITQ", new=2)  					
	elif alexa == "america":
		return webbrowser.open("https://youtu.be/6cmg75bgkkg", new=2) 		
	elif alexa == "a chicken wing":
		return webbrowser.open("https://youtu.be/tLUaycJFjWA", new=2) 				
	else:
		return print("alexa doesn't know what this is")

despacito(input("Alexa, this is "))

