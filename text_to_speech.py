# Import google translate library
from gtts import gTTS
import os

# Define the text which wants to convert to speech
myText = "Text To Speech Conversion Using Python"

# Natural Language
language = 'en'

# Get conversion to output variable using the gtts package
output = gTTS(text=myText, lang=language, slow=False)

# Save output as output.mp3
output.save("output.mp3")

# Start playing mp3 file using default player in the os
os.system("start output.mp3")