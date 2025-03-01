# This easy thing made by pingvortex
# https://github.com/pingvortex/Text-To-Wav/
# this thing makes a output.wav file of "ai" saying what you set in text_to_speak

import pyttsx3

def generate_singing_voice(text, output_filename="output.wav"):
    # replace underscores with spaces cuz of dum dum bliptext users
    text = text.replace('_', ' ')

    engine = pyttsx3.init()

    engine.setProperty('rate', 200)  # Speed, 200 recommended

    engine.save_to_file(text, output_filename)

    engine.runAndWait()

    print(f"Audio saved as {output_filename}")

# provide text u want the "ai" to say
text_to_speak = """
Hi I'm very dum dum
"""

generate_singing_voice(text_to_speak)
