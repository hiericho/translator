# Angelic Transliteration Scribe

An interactive web-based tool for transliterating various ancient, historical, and coded scripts to/from Latin characters, and for viewing Unicode character information. The interface features an "angelic scribe" theme with sepia-khaki colors and a dynamic dark mode.

This tool is designed for enthusiasts, students, and anyone curious about different writing systems.

## Features

*   **Multiple Script Support:** Transliterate between Latin and the following scripts:
    *   **Binary Code:** 8-bit per character representation.
    *   **Cypro-Minoan:** Conventional numerical labels (CM001-CM064) for the undeciphered script.
    *   **Cypriot Syllabary:** Phonetic transliteration for the ancient Greek dialect script.
    *   **Cyrillic:** Primarily based on Russian, including common characters from other Slavic languages (Ukrainian, Serbian, etc.), using a common romanization.
    *   **Ethiopic (Ge'ez Script):** Syllabic transliteration focusing on Amharic/Tigrinya usage (e.g., `hä, hu, hi, ha, he, hə, ho`).
    *   **Hiragana (Japanese):** Hepburn romanization for the Japanese syllabary.
    *   **Katakana (Japanese):** Hepburn romanization for the Japanese syllabary, including phonetic extensions.
    *   **Mende Kikakui:** Syllabic transliteration.
    *   **Morse Code:** International Morse Code.
    *   **Nushu:** Phonetic approximations for the unique syllabic script used by women in Jiangyong County, China.
    *   **Ogham:** Transliteration of the early medieval Irish alphabet.
    *   **Runic (Comprehensive):** Covers major runes from Elder Futhark, Anglo-Saxon Futhorc, and Younger Futhark (long-branch) with common romanizations.
    *   **Vai:** Syllabic transliteration.
    *   **Yi Syllables:** Nuosu Yi Pinyin.
*   **User-Friendly Web Interface:** Built with Python (Flask framework).
    *   Intuitive dropdowns for script selection and transliteration direction (to Latin, from Latin) or character info.
    *   Clear input and output text areas.
    *   "Swap Directions" button to easily reverse the input and output context.
    *   "Reveal a Random Script" button for exploration and discovery.
    *   Dynamic dark/light mode theme toggle with persistence via `localStorage`.
*   **Character Information:** Display detailed Unicode properties for any input character, including its codepoint, name, category, and script range (if defined).
*   **Thematic Design:** An "Angelic Scribe" aesthetic with sepia and khaki color palettes, and thematic icons.
*   **Favicon:** Custom icon for the browser tab/bookmarks.

## Project Structure
ancient_translator/
├── app.py # Main Flask web application
├── core_utils.py # Core transliteration logic and utility functions
├── main_translator.py # Original Command Line Interface (CLI) version (optional)
├── static/
│ └── favicon.png # Website favicon (replace with your actual icon)
│ └── (other static assets like custom CSS/JS if separated)
├── templates/
│ └── index.html # HTML template for the web interface
└── transliteration_maps/
├── init.py # Initializes and loads all script mapping modules
├── binary_code_map.py
├── cypro_minoan_map.py
├── cypriot_map.py
├── cyrillic_map.py
├── ethiopic_map.py
├── hiragana_map.py
├── katakana_map.py
├── mende_kikakui_map.py
├── morse_code_map.py
├── nushu_map.py
├── ogham_map.py
├── runic_comprehensive_map.py # Or individual Futhark maps if preferred
├── vai_map.py
└── yi_map.py


## Setup and Installation

Follow these steps to set up and run the Angelic Transliteration Scribe on your local machine:

1.  **Prerequisites:**
    *   Python 3.7+ installed.
    *   `pip` (Python package installer).

2.  **Clone the Repository (or Download Files):**
    If using Git:
    ```bash
    git clone <your-repository-url>
    cd ancient_translator
    ```
    If you downloaded the project as a ZIP file, extract it and navigate into the `ancient_translator` directory using your terminal.

3.  **Create and Activate a Virtual Environment (Highly Recommended):**
    This keeps project dependencies isolated.
    ```bash
    python -m venv venv
    ```
    Activate it:
    *   On Windows: `venv\Scripts\activate`
    *   On macOS/Linux: `source venv/bin/activate`

4.  **Install Dependencies:**
    The primary Python dependency is Flask.
    ```bash
    pip install Flask
    ```

5.  **Font Installation (Crucial for Correct Script Display):**
    To properly view the non-Latin scripts in your browser, you **must** have appropriate Unicode fonts installed on your operating system. The application's CSS suggests these fonts, but they need to be present on your system.

    The **Google Noto Fonts** family is an excellent resource for comprehensive script coverage. It is highly recommended to download and install Noto fonts for the scripts you intend to use, such as:
    *   `Noto Sans Nushu`
    *   `Noto Sans Mende Kikakui`
    *   `Noto Sans Vai`
    *   `Noto Sans Yi`
    *   `Noto Sans Ogham`
    *   `Noto Sans Runic`
    *   `Noto Sans Cypriot`
    *   `Noto Sans` (for general Latin, includes good Cyrillic coverage)
    *   `Noto Sans JP` (for Hiragana & Katakana)
    *   `Noto Sans Ethiopic`
    *   *Search "Google Noto Fonts" to find the download page for these individual font families.*

6.  **Prepare Favicon:**
    *   Create your desired icon as a `.png` or `.ico` file (e.g., `favicon.png`). Recommended sizes are 32x32 or 48x48 pixels.
    *   Place this icon file into the `ancient_translator/static/` directory. If the `static` directory does not exist, create it.

## Running the Web Application

1.  Ensure you are in the root `ancient_translator` directory in your terminal.
2.  Make sure your Python virtual environment is activated (see Step 3 in Setup).
3.  Execute the Flask application:
    ```bash
    python app.py
    ```
4.  The terminal will show output indicating the server is running, typically on `http://127.0.0.1:5000/`.
5.  Open this URL in your web browser to access the transliteration tool.

## Using the Transliteration Tool

The web interface is designed to be intuitive:

1.  **Toggle Theme:** Use the button (🌙/☀️) at the top right to switch between dark and light modes. Your preference is saved locally.
2.  **Reveal a Random Script:** Click the "🔮 Reveal a Random Script" button. A script will be randomly selected, its name displayed prominently, and the script dropdown updated. Input/output fields will be cleared for a fresh start.
3.  **Select a Script:** Choose the script you wish to work with from the "Sacred Script" dropdown menu.
4.  **Select an Action:**
    *   **Transcribe to Latin Script:** Converts characters from the selected script into their Latin transliteration.
    *   **Transcribe from Latin Script:** Converts Latin transliterations (according to the chosen script's mapping rules) into the selected script's characters.
    *   **Reveal Character's Essence:** Displays detailed Unicode information about the *first* character entered in the input field.
5.  **Input Text:** Type or paste the text you want to process into the "Inscribe Text Here" field.
6.  **Process:** Click the "📜 Transcribe" button. The transliterated result (or character info) will appear in the "Transcribed Revelation" field below.
7.  **Swap Directions:** Click the "⇆ Swap Directions" button to quickly toggle the "Divine Action" between "to Latin" and "from Latin." If there is text in the output field, it will be moved to the input field.

## Transliteration Maps & Logic

The transliteration capabilities are powered by Python dictionaries defined in `.py` files within the `transliteration_maps/` directory. Each script has its own map file.

*   **`TO_LATIN_MAP`:** Defines mappings from the script's characters to Latin.
*   **`FROM_LATIN_MAP`:** Defines mappings from Latin to the script's characters (often auto-generated by reversing `TO_LATIN_MAP`).
*   **Algorithmic Scripts:** Morse Code and Binary Code conversions are handled algorithmically within `core_utils.py` rather than through explicit large mapping dictionaries.

The `core_utils.py` file contains the main transliteration functions, which include logic for handling multi-character sequences (longest match first) when converting from Latin.

## Adding New Scripts (Contributing / Extending)

You can extend this tool by adding support for more scripts:

1.  **Research:**
    *   Identify the script's Unicode block(s).
    *   Find a common, reliable transliteration system (e.g., a standard romanization).
    *   Compile a list of the script's characters and their corresponding Latin transliterations.
2.  **Create Map File:**
    *   In the `transliteration_maps/` directory, create a new Python file named `your_script_name_map.py`.
    *   Define `SCRIPT_NAME`, `DESCRIPTION`, `UNICODE_RANGE` (optional but helpful), and the `TO_LATIN_MAP` dictionary within this file.
3.  **Font Considerations:**
    *   Ensure good, freely available fonts exist for the script (e.g., from the Google Noto family).
    *   You may need to update the `font-family` CSS in `templates/index.html` if the default browser fonts don't cover the new script well.
4.  **Test:**
    *   The system is designed to automatically detect and load new map files from the `transliteration_maps/` directory.
    *   Restart the Flask application and thoroughly test the new script for both "to Latin" and "from Latin" transliterations. Check for any ambiguities or errors.
5.  **Update README.md:** Add the newly supported script to the list in the "Features" section and to the `transliteration_maps/` listing in "Project Structure".

## Known Limitations & Potential Future Enhancements

*   **Contextual Transliteration:** The current system uses direct character/sequence mapping. True linguistic transliteration for some scripts (e.g., Japanese particles like は/わ, Cyrillic `Е` becoming `Ye`, Ethiopic gemination, handling of Arabic/Hebrew vowel points) requires complex contextual rules which are not implemented.
*   **Complex `FROM_LATIN` Scenarios:** For scripts where multiple native characters might correspond to a single simple Latin sequence, or where complex phonetic combinations in Latin need to map to specific ligatures or character sequences (e.g., advanced Japanese yōon or sokuon from Latin input), the auto-generated `FROM_LATIN_MAP` might be insufficient. Manual curation or more sophisticated parsing logic would be needed.
*   **Binary Encoding:** The current binary transliteration uses a simple 8-bit-per-character scheme based on `ord()`, suitable for ASCII and Latin-1. A full UTF-8 to multi-byte binary stream representation is more complex.
*   **Font Dependencies:** The visual rendering of many scripts is entirely dependent on the user having appropriate fonts installed on their system.
*   **Error Handling:** Basic error messages are provided, but more granular feedback for invalid input sequences could be added.
*   **Performance:** For extremely large inputs or very complex mapping rules (not currently an issue), performance could be a consideration.

## License

This project is provided as an educational and experimental tool. Please feel free to use, modify, and distribute it. If you plan to use it for more formal purposes, consider adding a specific open-source license.