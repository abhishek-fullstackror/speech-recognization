import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def openWebsite(command):
    if "google" in command:
        webbrowser.open("https://www.google.com/")
    if "youtube" in command:
        webbrowser.open('https://www.youtube.com/')
    if "linkedin" in command:
        webbrowser.open("https://www.linkedin.com/feed/")
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise and listen for audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        print('recognizing..')
        try:
            # Use Google Web Speech API for recognition
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            # Check for a specific command (e.g., "open website")
            openWebsite(command.lower())
            # if "google" in command:
            #     # Example action
            #     speak("Opening website...")
            #     webbrowser.open("https://www.example.com")  # Change to your desired URL
            
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
