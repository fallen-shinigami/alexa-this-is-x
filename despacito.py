import webbrowser

def despacito(alexa):
	if alexa == "sad":
		return webbrowser.open("https://soundcloud.com/luisfonsiofficial/despacito", new=2)
	elif alexa == "spicy":
        	return webbrowser.open("https://www.youtube.com/watch?v=TrZk3igdICc", new=2)
        elif alexa == "beefy":
                return webbrowser.open("https://www.youtube.com/watch?v=LYhF9ZRjVek", new=2)
        else:
		return print("alexa is not sad or spicy")

despacito(input("Alexa this is "))
