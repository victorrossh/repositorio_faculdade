import time
from pyglow import PyGlow

def flash(char):
  if char == '-': # Dashes... in yellow
    print ('-')
    pyglow.color(4,255)
    time.sleep(1)
    pyglow.color(4,0)
    time.sleep(.2)
  else: # If it's not a dash then it's a dot - let's use blue
    print('.' )
    pyglow.color(2,255)
    time.sleep(.5)
    pyglow.color(2,0)
    time.sleep(.2)

# The morse alphabet
morse = {
  'A': '.-',  'B': '-...',  'C': '-.-.',  'D': '-..',
  'E': '.',   'F': '..-.',  'G': '--.', 'H': '....',
  'I': '..',  'J': '.---',  'K': '-.-', 'L': '.-..',
  'M': '--',  'N': '-.',  'O': '---', 'P': '.--.',
  'Q': '--.-',  'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-',  'W': '.--', 'X': '-..-',
  'Y': '-.--',  'Z': '--..'}

# Import PyGlow for my PiGlow (of course) and reset to all off
pyglow = PyGlow()
pyglow.all(0)

# Start with a nice moustache ~~
text = 'MOUSTACHE'

# split text into letters
for letter in text:
  # Work out the morse code for this letter
  coded = morse[letter] 
  # For each dot or dash do the flash
  for char in coded:
    flash(char)
  time.sleep(.5) # Gap between letters