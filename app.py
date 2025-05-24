# ancient_translator/app.py

from flask import Flask, render_template, request
import random # Import the random module
from core_utils import (
    transliterate_to_latin,
    transliterate_from_latin,
    get_character_info
)
from transliteration import ALL_SCRIPTS_DATA

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    input_text = ""
    output_text = ""
    # Default selected_script to the first one if available, otherwise an empty string
    default_first_script = list(ALL_SCRIPTS_DATA.keys())[0] if ALL_SCRIPTS_DATA else ""
    selected_script = default_first_script
    selected_script_name_display = "" # For the "BIG" display
    
    selected_direction = "to_latin"
    error_message = None

    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        selected_script = request.form.get('script', default_first_script) # Use default if not found
        selected_direction = request.form.get('direction', 'to_latin')
        # random_button_pressed = request.form.get('random_button_pressed_field') == 'true' # Check if random button was pressed

        # If a script is selected (either by user or random button), get its display name
        if selected_script and selected_script in ALL_SCRIPTS_DATA:
            selected_script_name_display = ALL_SCRIPTS_DATA[selected_script].get('description', selected_script).split('(')[0].strip()

        if not selected_script or selected_script not in ALL_SCRIPTS_DATA:
            error_message = "Invalid script selected."
            selected_script = default_first_script # Fallback
            if selected_script:
                 selected_script_name_display = ALL_SCRIPTS_DATA[selected_script].get('description', selected_script).split('(')[0].strip()

        elif not input_text.strip() and selected_direction != 'info':
             error_message = "Input text cannot be empty."
        elif not input_text.strip() and selected_direction == 'info' and len(input_text) > 0 :
            error_message = "Cannot get info for only whitespace characters."
        elif not input_text.strip() and selected_direction == 'info' and len(input_text) == 0:
            error_message = "Input text cannot be empty for character info."
        else:
            try:
                if selected_direction == 'to_latin':
                    output_text = transliterate_to_latin(input_text, selected_script)
                elif selected_direction == 'from_latin':
                    output_text = transliterate_from_latin(input_text, selected_script)
                elif selected_direction == 'info':
                    if input_text:
                        output_text = get_character_info(input_text)
                    else:
                        error_message = "Please enter a character to get information."
                else:
                    error_message = "Invalid action selected."
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
    else: # GET request - initial page load or if random button was pressed without form submission
        # If a script is specified in URL params (e.g., from a future enhancement or direct link)
        # For now, this handles initial load.
        # If you want the random button to cause a GET request to update the server's selected_script:
        # script_from_url = request.args.get('script')
        # if script_from_url and script_from_url in ALL_SCRIPTS_DATA:
        #    selected_script = script_from_url
        
        if selected_script and selected_script in ALL_SCRIPTS_DATA:
            selected_script_name_display = ALL_SCRIPTS_DATA[selected_script].get('description', selected_script).split('(')[0].strip()


    return render_template(
        'index.html',
        available_scripts=ALL_SCRIPTS_DATA,
        input_text=input_text,
        output_text=output_text,
        selected_script=selected_script,
        selected_script_name=selected_script_name_display, # Pass the name for BIG display
        selected_direction=selected_direction,
        error_message=error_message
    )

if __name__ == '__main__':
    print("Flask development server starting...")
    print(f"Available scripts: {', '.join(ALL_SCRIPTS_DATA.keys())}")
    app.run(debug=True)