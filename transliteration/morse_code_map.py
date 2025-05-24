# ancient_translator/transliteration_maps/morse_code_map.py

SCRIPT_NAME = "morse"
DESCRIPTION = "Morse Code Transliteration"
UNICODE_RANGE = None # Not a script block in the Unicode sense

# Standard separators for Morse code
LETTER_SEPARATOR = ' '    # Character(s) to place between Morse codes for individual letters
WORD_SEPARATOR = ' / '     # Character(s) to place between Morse codes for words

# International Morse Code
# Maps Latin characters (and numbers/punctuation) to Morse Code strings
# This map is used when converting FROM Latin TO Morse.
LATIN_TO_MORSE = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.',
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..',
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.',
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-',
    'Y': '-.--', 
    'Z': '--..',
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-',
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.',
    '.': '.-.-.-', 
    ',': '--..--', 
    '?': '..--..', 
    "'": '.----.', 
    '!': '-.-.--',
    '/': '-..-.', 
    '(': '-.--.', 
    ')': '-.--.-', 
    '&': '.-...', 
    ':': '---...',
    ';': '-.-.-.', 
    '=': '-...-', 
    '+': '.-.-.', 
    '-': '-....-', 
    '_': '..--.-',
    '"': '.-..-.', 
    '$': '...-..-', 
    '@': '.--.-.',
    # Special handling for space in the input Latin text: it becomes a WORD_SEPARATOR in Morse.
    ' ': WORD_SEPARATOR
}

# Maps Morse Code strings to Latin characters
# This map is used when converting FROM Morse TO Latin.
# We derive this from LATIN_TO_MORSE, excluding the space-to-WORD_SEPARATOR mapping
# as word separation in Morse input is handled by splitting.
MORSE_TO_LATIN = {value: key for key, value in LATIN_TO_MORSE.items() if key != ' '}


# These are the maps expected by the __init__.py loader and core_utils.py
# TO_LATIN_MAP: Converts "script" (Morse) to Latin. So, it uses MORSE_TO_LATIN.
TO_LATIN_MAP = MORSE_TO_LATIN

# FROM_LATIN_MAP: Converts Latin to "script" (Morse). So, it uses LATIN_TO_MORSE.
FROM_LATIN_MAP = LATIN_TO_MORSE