import pyttsx3 as pyt
import requests
import json

engine = pyt.init()

greetings = "Hi There, I am an program designed to tell you about todays weather"
engine.say(greetings)
engine.runAndWait()


b = 0
while b == 0:
    try:
        greetings_1= "Type in which city's weather you'd like to know?"
        engine.say(greetings_1)
        engine.runAndWait()

        city = input("Type in city name: ")
        url = f"https://api.weatherapi.com/v1/current.json?key=a4816660485b468b9e7112427241209&q={city}"
        r = requests.get(url)

        dic = json.loads(r.text)
        location = dic["location"]["name"]
        temp = dic["current"]["temp_c"]

        final = (f"The current weather in {location} is {temp}")
        engine.say(final)
        engine.runAndWait()

        print(f"The current weather in {location} is {temp}")
        a = "Type Yes if you Would like to know weather for more cities? or Type no to exit the program"
        engine.say(a)
        engine.runAndWait()
        c = input("""Type "yes" if you'd like to know weather for more cities :""" )

        if c.lower() != "yes":
            b += 1
            k = "Bye! See you soon"
            engine.say(k)   
            engine.runAndWait()


    except EOFError:
        error = "Hmm, seems like you typed in something which is not in the database"

    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.8)  # Volume of speech (0.0 to 1.0)