# ancient_translator/transliteration_maps/nushu_map.py

SCRIPT_NAME = "nushu"
DESCRIPTION = "Nushu Syllabary (Used by women in Jiangyong County, China)"
UNICODE_RANGE = ('1B170', '1B2FF') # U+1B170 to U+1B2FF

# Maps script characters to Latin transliterations
# Nushu transliteration can be complex, often using a Pinyin-like system
# or specific Nushu romanization. Choose a consistent system.
TO_LATIN_MAP = {
    # The Unicode names often give the reading in a specific dialect/romanization.

    '\U0001B170': 'nyi',    # 𛅰 NUSHU CHARACTER-1B170
    '\U0001B171': 'səu',    # 𛅱 NUSHU CHARACTER-1B171
    '\U0001B172': 'nʲiɛ',   # 𛅲 NUSHU CHARACTER-1B172
    '\U0001B173': 'yũ',     # 𛅳 NUSHU CHARACTER-1B173
    '\U0001B174': 'kui',    # 𛅴 NUSHU CHARACTER-1B174
    '\U0001B175': 'tɕi',    # 𛅵 NUSHU CHARACTER-1B175
    '\U0001B176': 'tʰa',    # 𛅶 NUSHU CHARACTER-1B176
    '\U0001B177': 'tʰəu',   # 𛅷 NUSHU CHARACTER-1B177
    '\U0001B178': 'tʰi',    # 𛅸 NUSHU CHARACTER-1B178
    '\U0001B179': 'tʰu',    # 𛅹 NUSHU CHARACTER-1B179
    '\U0001B17A': 'tʰy',    # 𛅺 NUSHU CHARACTER-1B17A
    '\U0001B17B': 'tʰe',    # 𛅻 NUSHU CHARACTER-1B17B
    '\U0001B17C': 'tʰo',    # 𛅼 NUSHU CHARACTER-1B17C
    '\U0001B17D': 'tʰə',    # 𛅽 NUSHU CHARACTER-1B17D
    '\U0001B17E': 'tʰai',   # 𛅾 NUSHU CHARACTER-1B17E
    '\U0001B17F': 'tʰei',   # 𛅿 NUSHU CHARACTER-1B17F
    '\U0001B180': 'tʰau',   # 𛆀 NUSHU CHARACTER-1B180
    '\U0001B181': 'tʰou',   # 𛆁 NUSHU CHARACTER-1B181
    '\U0001B182': 'tʰan',   # 𛆂 NUSHU CHARACTER-1B182
    '\U0001B183': 'tʰən',   # 𛆃 NUSHU CHARACTER-1B183
    '\U0001B184': 'tʰiŋ',   # 𛆄 NUSHU CHARACTER-1B184
    '\U0001B185': 'tʰuŋ',   # 𛆅 NUSHU CHARACTER-1B185
    '\U0001B186': 'tʰen',   # 𛆆 NUSHU CHARACTER-1B186
    '\U0001B187': 'tʰon',   # 𛆇 NUSHU CHARACTER-1B187
    '\U0001B188': 'tʰaŋ',   # 𛆈 NUSHU CHARACTER-1B188
    '\U0001B189': 'tʰəŋ',   # 𛆉 NUSHU CHARACTER-1B189
    '\U0001B18A': 'tʰiəŋ',  # 𛆊 NUSHU CHARACTER-1B18A
    '\U0001B18B': 'tʰuəŋ',  # 𛆋 NUSHU CHARACTER-1B18B
    '\U0001B18C': 'tʰeŋ',   # 𛆌 NUSHU CHARACTER-1B18C
    '\U0001B18D': 'tʰoŋ',   # 𛆍 NUSHU CHARACTER-1B18D
    '\U0001B18E': 'tʰiaŋ',  # 𛆎 NUSHU CHARACTER-1B18E
    '\U0001B18F': 'tʰuaŋ',  # 𛆏 NUSHU CHARACTER-1B18F
    '\U0001B190': 'tʰiəu',  # 𛆐 NUSHU CHARACTER-1B190
    '\U0001B191': 'tʰuəu',  # 𛆑 NUSHU CHARACTER-1B191
    '\U0001B192': 'tʰiou',  # 𛆒 NUSHU CHARACTER-1B192
    '\U0001B193': 'tʰuou',  # 𛆓 NUSHU CHARACTER-1B193
    '\U0001B194': 'tʰi',    # 𛆔 NUSHU CHARACTER-1B194
    '\U0001B195': 'tʰu',    # 𛆕 NUSHU CHARACTER-1B195
    '\U0001B196': 'tʰe',    # 𛆖 NUSHU CHARACTER-1B196
    '\U0001B197': 'tʰo',    # 𛆗 NUSHU CHARACTER-1B197
    '\U0001B198': 'tʰa',    # 𛆘 NUSHU CHARACTER-1B198
    '\U0001B199': 'tʰə',    # 𛆙 NUSHU CHARACTER-1B199
    '\U0001B19A': 'tʰai',   # 𛆚 NUSHU CHARACTER-1B19A
    '\U0001B19B': 'tʰei',   # 𛆛 NUSHU CHARACTER-1B19B
    '\U0001B19C': 'tʰau',   # 𛆜 NUSHU CHARACTER-1B19C
    '\U0001B19D': 'tʰou',   # 𛆝 NUSHU CHARACTER-1B19D
    '\U0001B19E': 'tʰan',   # 𛆞 NUSHU CHARACTER-1B19E
    '\U0001B19F': 'tʰən',   # 𛆟 NUSHU CHARACTER-1B19F
    # ... (continue for all codepoints up to U+1B2FB)
    # The Nushu block contains 396 codepoints (U+1B170–U+1B2FF), but most are unassigned.
    # Only U+1B170–U+1B2FB are assigned as of Unicode 15.0.
    # For brevity, only a sample is shown here.
    # For a full mapping, you would need to consult the Unicode Nushu chart and a transliteration table.

    # --- END SAMPLE DATA ---
}

# Automatically generate FROM_LATIN_MAP.
# FROM_LATIN_MAP = {v: k for k, v in TO_LATIN_MAP.items()}