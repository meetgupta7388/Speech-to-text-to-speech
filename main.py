import speech_recognition
import pyttsx3
import sys

recognizer = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        try:
            # Use the recognize_google method for online speech recognition
            text = recognizer.recognize_google(audio)
           
            text = text.lower()
            if text == "on yourself jarvis":
                text_speech = pyttsx3.init()
                text_speech.setProperty('rate', 150)  # Speed of speech
                text_speech.say("i am on ,sir")
                text_speech.runAndWait()
                continue
            if text == "hello jarvis":
                text_speech = pyttsx3.init()
                text_speech.setProperty('rate', 150)  # Speed of speech
                text_speech.say("hello sir , what can I do for you?")
                text_speech.runAndWait()
                continue
            if text == "can you repeat after me":
                text_speech = pyttsx3.init()
                text_speech.setProperty('rate', 150)  # Speed of speech
                text_speech.say("sure sir, i will repeat after you")
                text_speech.runAndWait()
                continue
            if text == "thank u jarvis" or text == "thank you jarvis":
                text_speech = pyttsx3.init()
                text_speech.setProperty('rate', 150)  # Speed of speech
                text_speech.say("you are welcome,sir")
                text_speech.runAndWait()
                continue
            print(f"Recognized: {text}")

            if text == "turn off yourself":
                text_speech = pyttsx3.init()
                text_speech.setProperty('rate', 150)  # Speed of speech
                text_speech.say("Okay sir, Exiting the program")
                text_speech.runAndWait()
                sys.exit()

            # Initialize the text-to-speech engine
            text_speech = pyttsx3.init()

            # Set properties (optional)
            text_speech.setProperty('rate', 150)  # Speed of speech

            # Say the recognized text
            text_speech.say(text)

            # Wait for the speech to finish
            text_speech.runAndWait()
              
        except speech_recognition.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except speech_recognition.RequestError as e: 
            print(f"Speech Recognition request failed; {e}")
