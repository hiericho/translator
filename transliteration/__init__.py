# ancient_translator/transliteration_maps/__init__.py

import importlib
import os
import pkgutil

ALL_SCRIPTS_DATA = {}

# Dynamically import all modules in this package (the map files)
# This makes it easy to add new script maps by just adding a new .py file.
package_dir = os.path.dirname(__file__)
for (_, module_name, _) in pkgutil.iter_modules([package_dir]):
    # Ensure we only attempt to load modules that are likely script maps
    # and not __init__ itself or other utility files.
    if module_name.endswith("_map"):
        try:
            module = importlib.import_module(f".{module_name}", package=__name__)
            
            script_name_attr = getattr(module, "SCRIPT_NAME", None)
            to_latin_map_attr = getattr(module, "TO_LATIN_MAP", None)
            # from_latin_map_attr = getattr(module, "FROM_LATIN_MAP", None) # Can be derived

            if script_name_attr and to_latin_map_attr is not None:
                # Automatically generate FROM_LATIN_MAP if not explicitly defined,
                # assuming a one-to-one relationship or that the user wants simple inversion.
                # For complex cases, FROM_LATIN_MAP should be defined manually in the script_map file.
                from_latin_map_attr = getattr(module, "FROM_LATIN_MAP", None)
                if from_latin_map_attr is None:
                    from_latin_map_attr = {v: k for k, v in to_latin_map_attr.items()}

                ALL_SCRIPTS_DATA[script_name_attr] = {
                    "to_latin": to_latin_map_attr,
                    "from_latin": from_latin_map_attr, # Use derived or explicitly defined
                    "description": getattr(module, "DESCRIPTION", "No description provided."),
                    "range": getattr(module, "UNICODE_RANGE", None), # Tuple (start_hex, end_hex)
                }
            # else:
            #     print(f"Warning: Module {module_name} in transliteration_maps is missing SCRIPT_NAME or TO_LATIN_MAP.")

        except ImportError as e:
            print(f"Warning: Could not import module {module_name} from transliteration_maps: {e}")


# Helper function (optional, as main_translator can access ALL_SCRIPTS_DATA directly)
def get_all_script_names():
    """Returns a list of names of all configured scripts."""
    return list(ALL_SCRIPTS_DATA.keys())

def get_script_data(script_name):
    """Returns the data dictionary for a specific script, or None if not found."""
    return ALL_SCRIPTS_DATA.get(script_name)