# ancient_translator/core_utils.py

import unicodedata
from transliteration import ALL_SCRIPTS_DATA

# --- Morse Code Constants (if morse_code_map exists) ---
try:
    from transliteration import morse_code_map
    MORSE_LETTER_SEPARATOR = morse_code_map.LETTER_SEPARATOR
    MORSE_WORD_SEPARATOR = morse_code_map.WORD_SEPARATOR
except ImportError:
    MORSE_LETTER_SEPARATOR = ' '
    MORSE_WORD_SEPARATOR = ' / '

# --- Binary Code Constants (if binary_code_map exists) ---
try:
    from transliteration import binary_code_map
    BINARY_CHAR_SEPARATOR = binary_code_map.BINARY_CHAR_SEPARATOR
except ImportError:
    BINARY_CHAR_SEPARATOR = ' '


# --- Helper function for Latin to Binary ---
def _transliterate_latin_to_binary(text):
    """Converts Latin text to an 8-bit binary string representation for each character."""
    binary_chars = []
    for char_code in text:
        # Get ASCII or Unicode ordinal value
        ord_val = ord(char_code)
        # Convert to 8-bit binary string (0-padded)
        # We'll cap at 255 for simplicity to ensure 8-bits,
        # otherwise UTF-8 characters beyond ASCII would need more bits or a different scheme.
        # For characters > 255, one might use multiple 8-bit sequences (like UTF-8 encoding)
        # or indicate an issue. For this example, let's represent them if they fit 8 bits,
        # or mark as unknown if larger.
        if 0 <= ord_val <= 255:
            binary_string = format(ord_val, '08b') # '08b' means 8-digit binary, zero-padded
            binary_chars.append(binary_string)
        else:
            # Character out of 8-bit representable range for this simple scheme
            binary_chars.append(f"[?ASC_{ord_val}]") 
    return BINARY_CHAR_SEPARATOR.join(binary_chars)

# --- Helper function for Binary to Latin ---
def _transliterate_binary_to_latin(text):
    """Converts an 8-bit binary string representation back to Latin text."""
    latin_chars = []
    # Split the input text by the binary character separator
    binary_segments = text.split(BINARY_CHAR_SEPARATOR)

    for bin_segment in binary_segments:
        bin_segment = bin_segment.strip() # Clean up any extra spaces
        if not bin_segment:
            continue
        
        if len(bin_segment) == 8 and all(c in '01' for c in bin_segment):
            try:
                ord_val = int(bin_segment, 2) # Convert binary string to integer
                if 0 <= ord_val <= 255: # Assuming we are decoding characters in this range
                    latin_chars.append(chr(ord_val))
                else:
                    # This case shouldn't be hit if we only encoded 0-255,
                    # but good for robustness if input binary is unexpected.
                    latin_chars.append(f"[?VAL_{ord_val}]")
            except ValueError:
                # Not a valid binary number (should be caught by all(c in '01'))
                latin_chars.append(f"[?BIN_{bin_segment}]")
        elif bin_segment: # If it's not empty and not valid 8-bit binary
            latin_chars.append(f"[?FMT_{bin_segment}]") # Format error

    return "".join(latin_chars)


# --- Morse Code specific functions (from previous step) ---
def _transliterate_latin_to_morse(text, latin_to_morse_map):
    # ... (keep existing Morse function)
    output_morse_parts = []
    text = text.upper()
    for char_index, char_code in enumerate(text):
        if char_code == ' ':
            morse_segment = latin_to_morse_map.get(' ')
            if morse_segment:
                if not (output_morse_parts and output_morse_parts[-1] == morse_segment):
                    output_morse_parts.append(morse_segment)
        elif char_code in latin_to_morse_map:
            output_morse_parts.append(latin_to_morse_map[char_code])
        else:
            output_morse_parts.append(f"[?{char_code}]")
    final_output_string = []
    for i, part in enumerate(output_morse_parts):
        final_output_string.append(part)
        if part != MORSE_WORD_SEPARATOR and i < len(output_morse_parts) - 1 and \
           output_morse_parts[i+1] != MORSE_WORD_SEPARATOR:
            final_output_string.append(MORSE_LETTER_SEPARATOR)
    return "".join(final_output_string).strip()

def _transliterate_morse_to_latin(text, morse_to_latin_map):
    # ... (keep existing Morse function)
    latin_output_words = []
    morse_words = text.split(MORSE_WORD_SEPARATOR)
    for morse_word_segment in morse_words:
        morse_letters = morse_word_segment.strip(MORSE_LETTER_SEPARATOR).split(MORSE_LETTER_SEPARATOR)
        current_latin_word_chars = []
        for morse_char_code in morse_letters:
            if not morse_char_code:
                continue
            latin_char = morse_to_latin_map.get(morse_char_code)
            if latin_char is not None:
                current_latin_word_chars.append(latin_char)
            else:
                current_latin_word_chars.append(f"[?{morse_char_code}]")
        if current_latin_word_chars:
            latin_output_words.append("".join(current_latin_word_chars))
    return " ".join(latin_output_words)


# --- Main Transliteration Functions ---
def transliterate_to_latin(text, script_name):
    """
    Transliterates text from a given script to its Latin representation.
    Handles Morse and Binary code as special cases.
    """
    if script_name == "morse":
        script_data = ALL_SCRIPTS_DATA.get(script_name)
        if not script_data: return f"Error: Script data for 'morse' not found."
        morse_to_latin_map = script_data.get("to_latin")
        if morse_to_latin_map is None: return f"Error: 'to_latin' (MORSE_TO_LATIN) mapping not found for Morse."
        return _transliterate_morse_to_latin(text, morse_to_latin_map)
    
    if script_name == "binary":
        # No specific map needed from script_data for binary to latin, it's algorithmic
        return _transliterate_binary_to_latin(text)

    # Existing generic logic for other scripts
    script_data = ALL_SCRIPTS_DATA.get(script_name)
    if not script_data:
        return f"Error: Script data for '{script_name}' not found."
    
    mapping = script_data.get("to_latin")
    if mapping is None: 
        return f"Error: 'to_latin' mapping not found for script '{script_name}'."
    
    result = []
    i = 0
    text_len = len(text)
    sorted_script_keys = sorted(mapping.keys(), key=len, reverse=True)

    while i < text_len:
        matched = False
        for key in sorted_script_keys:
            if text.startswith(key, i):
                result.append(mapping[key])
                i += len(key)
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return "".join(result)


def transliterate_from_latin(text, script_name):
    """
    Transliterates text from a Latin representation back to the script's characters.
    Handles Morse and Binary code as special cases.
    """
    if script_name == "morse":
        script_data = ALL_SCRIPTS_DATA.get(script_name)
        if not script_data: return f"Error: Script data for 'morse' not found."
        latin_to_morse_map = script_data.get("from_latin")
        if latin_to_morse_map is None: return f"Error: 'from_latin' (LATIN_TO_MORSE) mapping not found for Morse."
        return _transliterate_latin_to_morse(text, latin_to_morse_map)

    if script_name == "binary":
        # No specific map needed from script_data for latin to binary, it's algorithmic
        return _transliterate_latin_to_binary(text)

    # Existing generic logic for other scripts
    script_data = ALL_SCRIPTS_DATA.get(script_name)
    if not script_data:
        return f"Error: Script data for '{script_name}' not found."

    mapping = script_data.get("from_latin")
    if mapping is None:
        return f"Error: 'from_latin' mapping not found for script '{script_name}'."
    
    sorted_latin_keys = sorted(mapping.keys(), key=len, reverse=True)
    
    result = []
    i = 0
    text_len = len(text)
    while i < text_len:
        matched = False
        for key in sorted_latin_keys: 
            if text.startswith(key, i): 
                result.append(mapping[key]) 
                i += len(key)               
                matched = True
                break 
        if not matched:
            result.append(text[i]) 
            i += 1
            
    return "".join(result)


# ... (get_character_info function remains the same) ...
def get_character_info(char_text):
    if not char_text:
        return "No character provided."
    
    char = char_text[0]
    
    try:
        name = unicodedata.name(char)
    except ValueError:
        name = "No official Unicode name (or not a single character)"
    
    info_lines = [
        f"Character: '{char}'",
        f"Unicode Codepoint: U+{ord(char):04X}",
        f"Decimal Value: {ord(char)}",
        f"8-bit Binary: {format(ord(char), '08b') if 0 <= ord(char) <= 255 else 'N/A (out of 8-bit range)'}",
        f"Unicode Name: {name}",
        f"Category: {unicodedata.category(char)} ({unicodedata.category(char).__doc__})",
        f"Bidirectional Class: {unicodedata.bidirectional(char)}",
    ]

    char_cp = ord(char)
    matched_scripts = []
    for script_id, data in ALL_SCRIPTS_DATA.items():
        if data.get("range"): # Check if 'range' key exists
            try:
                start_cp_hex, end_cp_hex = data["range"]
                start_cp = int(start_cp_hex, 16)
                end_cp = int(end_cp_hex, 16)
                if start_cp <= char_cp <= end_cp:
                    script_info = f"Belongs to script range: {script_id} ({data.get('description', 'N/A')})"
                    translit_map = data.get("to_latin", {}) # Ensure to_latin map exists
                    translit = translit_map.get(char)
                    if translit:
                        script_info += f" -> Transliteration ({script_id}): {translit}"
                    matched_scripts.append(script_info)
            except (ValueError, TypeError, IndexError) as e:
                pass # Silently ignore malformed range data or if range is None
    
    if matched_scripts:
        info_lines.append("\nScript Membership (based on defined ranges):")
        info_lines.extend([f"  - {s_info}" for s_info in matched_scripts])
    else:
        info_lines.append("\nNot found in any defined script Unicode ranges.")
                
    return "\n".join(info_lines)