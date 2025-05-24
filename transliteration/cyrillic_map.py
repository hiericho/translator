# ancient_translator/transliteration_maps/cyrillic_map.py

SCRIPT_NAME = "cyrillic"
DESCRIPTION = "Cyrillic (primarily Russian, common Slavic)"
UNICODE_RANGE = ('0400', '04FF') # Basic Cyrillic block U+0400 to U+04FF

# Maps Cyrillic characters (keys) to their common Latin transliterations (values).
# This map focuses on Russian and includes other common Slavic Cyrillic letters.
# Both uppercase and lowercase forms are included.
TO_LATIN_MAP = {
    # Russian Alphabet (+ common Slavic) - Uppercase
    '\u0410': 'A',    # А CYRILLIC CAPITAL LETTER A
    '\u0411': 'B',    # Б CYRILLIC CAPITAL LETTER BE
    '\u0412': 'V',    # В CYRILLIC CAPITAL LETTER VE
    '\u0413': 'G',    # Г CYRILLIC CAPITAL LETTER GHE
    '\u0414': 'D',    # Д CYRILLIC CAPITAL LETTER DE
    '\u0415': 'E',    # Е CYRILLIC CAPITAL LETTER IE (can be Ye initially or after vowel/soft/hard sign)
    '\u0401': 'Yo',   # Ё CYRILLIC CAPITAL LETTER IO (often transliterated Yo or Ë)
    '\u0416': 'Zh',   # Ж CYRILLIC CAPITAL LETTER ZHE
    '\u0417': 'Z',    # З CYRILLIC CAPITAL LETTER ZE
    '\u0418': 'I',    # И CYRILLIC CAPITAL LETTER I
    '\u0419': 'Y',    # Й CYRILLIC CAPITAL LETTER SHORT I (or J, I kratkoye)
    '\u041A': 'K',    # К CYRILLIC CAPITAL LETTER KA
    '\u041B': 'L',    # Л CYRILLIC CAPITAL LETTER EL
    '\u041C': 'M',    # М CYRILLIC CAPITAL LETTER EM
    '\u041D': 'N',    # Н CYRILLIC CAPITAL LETTER EN
    '\u041E': 'O',    # О CYRILLIC CAPITAL LETTER O
    '\u041F': 'P',    # П CYRILLIC CAPITAL LETTER PE
    '\u0420': 'R',    # Р CYRILLIC CAPITAL LETTER ER
    '\u0421': 'S',    # С CYRILLIC CAPITAL LETTER ES
    '\u0422': 'T',    # Т CYRILLIC CAPITAL LETTER TE
    '\u0423': 'U',    # У CYRILLIC CAPITAL LETTER U
    '\u0424': 'F',    # Ф CYRILLIC CAPITAL LETTER EF
    '\u0425': 'Kh',   # Х CYRILLIC CAPITAL LETTER HA
    '\u0426': 'Ts',   # Ц CYRILLIC CAPITAL LETTER TSE
    '\u0427': 'Ch',   # Ч CYRILLIC CAPITAL LETTER CHE
    '\u0428': 'Sh',   # Ш CYRILLIC CAPITAL LETTER SHA
    '\u0429': 'Shch', # Щ CYRILLIC CAPITAL LETTER SHCHA
    '\u042A': '"',    # Ъ CYRILLIC CAPITAL LETTER HARD SIGN (often ' or " or omitted, or `) - using " as a common simple representation
    '\u042B': 'Y',    # Ы CYRILLIC CAPITAL LETTER YERU (can be y, i, ui) - often 'y'
    '\u042C': "'",    # Ь CYRILLIC CAPITAL LETTER SOFT SIGN (often ' or omitted, or j) - using ' as a common simple representation
    '\u042D': 'E',    # Э CYRILLIC CAPITAL LETTER E
    '\u042E': 'Yu',   # Ю CYRILLIC CAPITAL LETTER YU
    '\u042F': 'Ya',   # Я CYRILLIC CAPITAL LETTER YA

    # Russian Alphabet (+ common Slavic) - Lowercase
    '\u0430': 'a',    # а CYRILLIC SMALL LETTER A
    '\u0431': 'b',    # б CYRILLIC SMALL LETTER BE
    '\u0432': 'v',    # в CYRILLIC SMALL LETTER VE
    '\u0433': 'g',    # г CYRILLIC SMALL LETTER GHE
    '\u0434': 'd',    # д CYRILLIC SMALL LETTER DE
    '\u0435': 'e',    # е CYRILLIC SMALL LETTER IE (ye)
    '\u0451': 'yo',   # ё CYRILLIC SMALL LETTER IO (ë)
    '\u0436': 'zh',   # ж CYRILLIC SMALL LETTER ZHE
    '\u0437': 'z',    # з CYRILLIC SMALL LETTER ZE
    '\u0438': 'i',    # и CYRILLIC SMALL LETTER I
    '\u0439': 'y',    # й CYRILLIC SMALL LETTER SHORT I (j)
    '\u043A': 'k',    # к CYRILLIC SMALL LETTER KA
    '\u043B': 'l',    # л CYRILLIC SMALL LETTER EL
    '\u043C': 'm',    # м CYRILLIC SMALL LETTER EM
    '\u043D': 'n',    # н CYRILLIC SMALL LETTER EN
    '\u043E': 'o',    # о CYRILLIC SMALL LETTER O
    '\u043F': 'p',    # п CYRILLIC SMALL LETTER PE
    '\u0440': 'r',    # р CYRILLIC SMALL LETTER ER
    '\u0441': 's',    # с CYRILLIC SMALL LETTER ES
    '\u0442': 't',    # т CYRILLIC SMALL LETTER TE
    '\u0443': 'u',    # у CYRILLIC SMALL LETTER U
    '\u0444': 'f',    # ф CYRILLIC SMALL LETTER EF
    '\u0445': 'kh',   # х CYRILLIC SMALL LETTER HA
    '\u0446': 'ts',   # ц CYRILLIC SMALL LETTER TSE
    '\u0447': 'ch',   # ч CYRILLIC SMALL LETTER CHE
    '\u0448': 'sh',   # ш CYRILLIC SMALL LETTER SHA
    '\u0449': 'shch', # щ CYRILLIC SMALL LETTER SHCHA
    '\u044A': '"',    # ъ CYRILLIC SMALL LETTER HARD SIGN (")
    '\u044B': 'y',    # ы CYRILLIC SMALL LETTER YERU (y)
    '\u044C': "'",    # ь CYRILLIC SMALL LETTER SOFT SIGN (')
    '\u044D': 'e',    # э CYRILLIC SMALL LETTER E
    '\u044E': 'yu',   # ю CYRILLIC SMALL LETTER YU
    '\u044F': 'ya',   # я CYRILLIC SMALL LETTER YA

    # Additional common Slavic letters (Ukrainian, Belarusian, Serbian, Macedonian etc.)
    # Uppercase
    '\u0402': 'Dj',   # Ђ CYRILLIC CAPITAL LETTER DJE (Serbian)
    '\u0403': 'Gj',   # Ѓ CYRILLIC CAPITAL LETTER GJE (Macedonian)
    '\u0404': 'Ye',   # Є CYRILLIC CAPITAL LETTER UKRAINIAN IE (Ukrainian Ye)
    '\u0405': 'Dz',   # Ѕ CYRILLIC CAPITAL LETTER DZE (Macedonian, Old Church Slavonic)
    '\u0406': 'I',    # І CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I (Ukrainian/Belarusian I)
    '\u0407': 'Yi',   # Ї CYRILLIC CAPITAL LETTER YI (Ukrainian Yi)
    '\u0408': 'J',    # Ј CYRILLIC CAPITAL LETTER JE (Serbian, Macedonian J)
    '\u0409': 'Lj',   # Љ CYRILLIC CAPITAL LETTER LJE (Serbian, Macedonian)
    '\u040A': 'Nj',   # Њ CYRILLIC CAPITAL LETTER NJE (Serbian, Macedonian)
    '\u040B': 'Tsh',  # Ћ CYRILLIC CAPITAL LETTER TSHE (Serbian Ch) - often Ć
    '\u040C': 'Kj',   # Ќ CYRILLIC CAPITAL LETTER KJE (Macedonian)
    # '\u040E': 'Dz', # Ў CYRILLIC CAPITAL LETTER SHORT U (Belarusian Waw/U) - often 'W' or 'Ŭ' -> This is U+040E, maps to 'Ŭ' or 'W'
    '\u040E': 'W',    # Ў CYRILLIC CAPITAL LETTER SHORT U (Belarusian W) - or Ŭ
    '\u040F': 'Dzh',  # Џ CYRILLIC CAPITAL LETTER DZHE (Serbian, Macedonian J as in Judge)
    '\u0490': 'Gg',   # Ґ CYRILLIC CAPITAL LETTER GHE WITH UPTURN (Ukrainian G)

    # Lowercase
    '\u0452': 'dj',   # ђ CYRILLIC SMALL LETTER DJE
    '\u0453': 'gj',   # ѓ CYRILLIC SMALL LETTER GJE
    '\u0454': 'ye',   # є CYRILLIC SMALL LETTER UKRAINIAN IE
    '\u0455': 'dz',   # ѕ CYRILLIC SMALL LETTER DZE
    '\u0456': 'i',    # і CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    '\u0457': 'yi',   # ї CYRILLIC SMALL LETTER YI
    '\u0458': 'j',    # ј CYRILLIC SMALL LETTER JE
    '\u0459': 'lj',   # љ CYRILLIC SMALL LETTER LJE
    '\u045A': 'nj',   # њ CYRILLIC SMALL LETTER NJE
    '\u045B': 'tsh',  # ћ CYRILLIC SMALL LETTER TSHE (ć)
    '\u045C': 'kj',   # ќ CYRILLIC SMALL LETTER KJE
    '\u045E': 'w',    # ў CYRILLIC SMALL LETTER SHORT U (Belarusian w) - or ŭ
    '\u045F': 'dzh',  # џ CYRILLIC SMALL LETTER DZHE
    '\u0491': 'gg',   # ґ CYRILLIC SMALL LETTER GHE WITH UPTURN

    # Note: Some transliterations (like for hard/soft signs) are conventional simplifications.
    # More precise linguistic transliteration would use different symbols (e.g., `’` for soft sign, `”` for hard sign, or `j`/nothing).
    # `Е е` is 'e' but often 'ye' if initial or after vowel/soft/hard sign. This map simplifies to 'e'.
    # A more complex transliterator would need rules for context.
}

# The FROM_LATIN_MAP will be automatically generated by your __init__.py
# Multi-letter Latin sequences like 'Zh', 'Kh', 'Ts', 'Ch', 'Sh', 'Shch', 'Yo', 'Yu', 'Ya'
# and 'Dj', 'Gj', 'Ye', 'Dz', 'Yi', 'Lj', 'Nj', 'Tsh', 'Kj', 'Dzh', 'Gg'
# will be handled correctly by the "longest match first" logic in `transliterate_from_latin`.
# FROM_LATIN_MAP = {v: k for k, v in TO_LATIN_MAP.items()}