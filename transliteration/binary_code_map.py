# ancient_translator/transliteration_maps/binary_code_map.py

SCRIPT_NAME = "binary"
DESCRIPTION = "Binary Code (8-bit per char) Transliteration"
UNICODE_RANGE = None # Not a script block

# Separator between binary codes for individual characters
BINARY_CHAR_SEPARATOR = ' ' # A space is common

# We don't need explicit maps for binary as it's algorithmic.
# The core_utils.py will handle the conversion directly.
# Provide empty maps to satisfy the loader.
TO_LATIN_MAP = {}   # Binary to Latin (will be handled algorithmically)
FROM_LATIN_MAP = {} # Latin to Binary (will be handled algorithmically)