import pyttsx3
# Create a TTS engine
engine = pyttsx3.init()

greetings = ("Hello, I am Robo Speaker, what do you want me to say?")
engine.say(greetings)
engine.runAndWait()
while True:
        text = (input("Type to speak: "))
        if text.lower() == "exit":
                engine.say("Bue Bye! See You Soon!")
                break
        else:
                engine.say(text)
                engine.runAndWait()

# Set the properties of the TTS voice (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.8)  # Volume of speech (0.0 to 1.0)

# Run the TTS engine to speak the text

