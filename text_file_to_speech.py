# Import google translate library
from gtts import gTTS
import os

# Instead of using text paragraph use text file

# Create fh (file handler) variable
# open the file
# r means read mode, w means write mode
fh = open("test.txt", "r")
# Replace line endings with whitespace
myText = fh.read().replace("\n", " ")

# Natural Language
language = 'en'

# Get conversion to output1 variable using the gtts package
output = gTTS(text=myText, lang=language, slow=False)

# Save output as output.mp3
output.save("output1.mp3")

#close file
fh.close()

# Start playing mp3 file using default player in the os
os.system("start output1.mp3")