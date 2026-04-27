import pyttsx3
import random
import time

# Initialize voice engine
engine = pyttsx3.init()

# Optional: change voice (0 = male, 1 = female depending on system)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Adjust speed
engine.setProperty('rate', 170)

roasts = [
    "Sanhik, bro writes code like WiFi on one bar",
    "Sanhik's code has more bugs than a jungle",
    "Even Python is confused reading Sanhik's logic",
    "Sanhik doesn't debug... he just hopes",
    "Indentation left Sanhik's life long ago",
    "Sanhik copy pastes and still gets errors",
    "Bro named Sanhik but coding level still tutorial mode",
    "Sanhik's code runs only when luck is strong",
    "Compiler sees Sanhik's code and says I am tired",
    "Sanhik versus syntax error is a daily fight"
]

print("\n💻 Initializing Voice Roast Engine...\n")
time.sleep(1)

engine.say("Initializing roast for Sanhik")
engine.runAndWait()

time.sleep(1)

for i in range(5):
    roast = random.choice(roasts)
    print("👉", roast)
    
    engine.say(roast)
    engine.runAndWait()
    
    time.sleep(1)

engine.say("Roast complete. Sanhik needs serious coding upgrade.")
engine.runAndWait()

print("\n💀 Roast Complete.\n")
