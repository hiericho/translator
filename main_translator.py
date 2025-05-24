# ancient_translator/main_translator.py

import argparse
from core_utils import (
    transliterate_to_latin,
    transliterate_from_latin,
    get_character_info
)
# Import ALL_SCRIPTS_DATA to list available scripts and their names
from transliteration import ALL_SCRIPTS_DATA

def main():
    available_script_names = list(ALL_SCRIPTS_DATA.keys())
    
    parser = argparse.ArgumentParser(
        description="Transliterate text or get character info for various ancient/historical scripts.",
        formatter_class=argparse.RawTextHelpFormatter # Allows for better formatting of help text
    )
    
    script_help_text = "The script to use for transliteration."
    if available_script_names:
        script_help_text += f"\nAvailable: {', '.join(sorted(available_script_names))}"
    else:
        script_help_text += "\nNo scripts configured in transliteration_maps."
    script_help_text += "\nNot needed for 'info' action."

    parser.add_argument(
        "script", 
        nargs="?", 
        help=script_help_text
    )
    parser.add_argument(
        "text", 
        help="The text to transliterate or the character for info."
    )
    parser.add_argument(
        "-d", "--direction", 
        choices=["to_latin", "from_latin", "info"], 
        default="to_latin",
        help="Direction of transliteration or 'info' to get character details.\n"
             "  to_latin: Convert script characters to Latin representation.\n"
             "  from_latin: Convert Latin representation to script characters.\n"
             "  info: Display Unicode information about the first character in the text.\n"
             "(default: to_latin)"
    )
    parser.add_argument(
        "-l", "--list-scripts",
        action="store_true",
        help="List all available scripts and their descriptions, then exit."
    )


    args = parser.parse_args()

    if args.list_scripts:
        print("Available scripts:")
        if ALL_SCRIPTS_DATA:
            for name, data in sorted(ALL_SCRIPTS_DATA.items()):
                print(f"  - {name}: {data.get('description', 'No description')}")
        else:
            print("  No scripts have been configured in the transliteration_maps directory.")
        return

    if args.direction == "info":
        print(get_character_info(args.text))
    elif args.script:
        if args.script not in available_script_names:
            print(f"Error: Script '{args.script}' not supported.")
            if available_script_names:
                print(f"Available scripts: {', '.join(sorted(available_script_names))}")
            else:
                print("No scripts have been configured in the transliteration_maps directory.")
            parser.print_help()
            return

        if args.direction == "to_latin":
            result = transliterate_to_latin(args.text, args.script)
            print(f"To Latin ({args.script}): {result}")
        elif args.direction == "from_latin":
            result = transliterate_from_latin(args.text, args.script)
            print(f"From Latin ({args.script}): {result}")
    else:
        # This case should be caught by argparse if script is required for the chosen direction
        # but added for robustness if nargs='?' for script is ever problematic.
        if args.direction in ["to_latin", "from_latin"]:
            print("Error: Script name required for transliteration.")
            parser.print_help()
        else: # Should not happen with current logic
            print("Invalid state. Please check arguments.")
            parser.print_help()


if __name__ == "__main__":
    # --- IMPORTANT REMINDER ---
    # The `*_map.py` files in the `transliteration_maps` directory MUST be
    # populated with comprehensive character mappings for this tool to be useful.
    # The provided map files contain only small samples.
    #
    # TO RUN (assuming you are in the directory CONTAINING `ancient_translator`):
    #   python -m ancient_translator.main_translator --list-scripts
    #   python -m ancient_translator.main_translator cypriot "𐠀𐠈𐠊" -d to_latin
    #   python -m ancient_translator.main_translator cypriot "aka" -d from_latin
    #   python -m ancient_translator.main_translator -- -d info "𐠀" (use -- if char starts with -)
    #
    # Or, if you are INSIDE the `ancient_translator` directory:
    #   python main_translator.py --list-scripts
    #   python main_translator.py cypriot "𐠀𐠈𐠊" -d to_latin
    #   python main_translator.py cypriot "aka" -d from_latin
    #   python main_translator.py -- -d info "𐠀"
    main()