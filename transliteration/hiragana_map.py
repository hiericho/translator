# ancient_translator/transliteration_maps/hiragana_map.py

SCRIPT_NAME = "hiragana"
DESCRIPTION = "Japanese Hiragana (Hepburn Romanization)"
UNICODE_RANGE = ('3040', '309F') # U+3040 to U+309F

# Maps Hiragana characters (keys) to their Hepburn Romanization (values).
TO_LATIN_MAP = {
    # === Basic Vowels ===
    '\u3042': 'a',    # あ HIRAGANA LETTER A
    '\u3044': 'i',    # い HIRAGANA LETTER I
    '\u3046': 'u',    # う HIRAGANA LETTER U
    '\u3048': 'e',    # え HIRAGANA LETTER E
    '\u304A': 'o',    # お HIRAGANA LETTER O

    # === K-series ===
    '\u304B': 'ka',   # か HIRAGANA LETTER KA
    '\u304D': 'ki',   # き HIRAGANA LETTER KI
    '\u304F': 'ku',   # く HIRAGANA LETTER KU
    '\u3051': 'ke',   # け HIRAGANA LETTER KE
    '\u3053': 'ko',   # こ HIRAGANA LETTER KO

    # === S-series ===
    '\u3055': 'sa',   # さ HIRAGANA LETTER SA
    '\u3057': 'shi',  # し HIRAGANA LETTER SI (Hepburn: shi)
    '\u3059': 'su',   # す HIRAGANA LETTER SU
    '\u305B': 'se',   # せ HIRAGANA LETTER SE
    '\u305D': 'so',   # そ HIRAGANA LETTER SO

    # === T-series ===
    '\u305F': 'ta',   # た HIRAGANA LETTER TA
    '\u3061': 'chi',  # ち HIRAGANA LETTER TI (Hepburn: chi)
    '\u3064': 'tsu',  # つ HIRAGANA LETTER TU (Hepburn: tsu)
    '\u3066': 'te',   # て HIRAGANA LETTER TE
    '\u3068': 'to',   # と HIRAGANA LETTER TO

    # === N-series ===
    '\u306A': 'na',   # な HIRAGANA LETTER NA
    '\u306B': 'ni',   # に HIRAGANA LETTER NI
    '\u306C': 'nu',   # ぬ HIRAGANA LETTER NU
    '\u306D': 'ne',   # ね HIRAGANA LETTER NE
    '\u306E': 'no',   # の HIRAGANA LETTER NO

    # === H-series ===
    '\u306F': 'ha',   # は HIRAGANA LETTER HA (also particle 'wa')
    '\u3072': 'hi',   # ひ HIRAGANA LETTER HI
    '\u3075': 'fu',   # ふ HIRAGANA LETTER HU (Hepburn: fu)
    '\u3078': 'he',   # へ HIRAGANA LETTER HE (also particle 'e')
    '\u307B': 'ho',   # ほ HIRAGANA LETTER HO

    # === M-series ===
    '\u307E': 'ma',   # ま HIRAGANA LETTER MA
    '\u307F': 'mi',   # み HIRAGANA LETTER MI
    '\u3080': 'mu',   # む HIRAGANA LETTER MU
    '\u3081': 'me',   # め HIRAGANA LETTER ME
    '\u3082': 'mo',   # も HIRAGANA LETTER MO

    # === Y-series ===
    '\u3084': 'ya',   # や HIRAGANA LETTER YA
    '\u3086': 'yu',   # ゆ HIRAGANA LETTER YU
    '\u3088': 'yo',   # よ HIRAGANA LETTER YO

    # === R-series ===
    '\u3089': 'ra',   # ら HIRAGANA LETTER RA
    '\u308A': 'ri',   # り HIRAGANA LETTER RI
    '\u308B': 'ru',   # る HIRAGANA LETTER RU
    '\u308C': 're',   # れ HIRAGANA LETTER RE
    '\u308D': 'ro',   # ろ HIRAGANA LETTER RO

    # === W-series ===
    '\u308F': 'wa',   # わ HIRAGANA LETTER WA
    '\u3090': 'wi',   # ゐ HIRAGANA LETTER WI (obsolete, transliterated 'wi')
    '\u3091': 'we',   # ゑ HIRAGANA LETTER WE (obsolete, transliterated 'we')
    '\u3092': 'o',    # を HIRAGANA LETTER WO (particle 'o', pronounced 'o')

    # === N (syllabic) ===
    '\u3093': 'n',    # ん HIRAGANA LETTER N (syllabic N, can be n, m, ng depending on context)
                      # Simple transliteration is 'n'. More advanced would need rules.

    # === Voiced Sounds (Dakuten ゙ ) - G, Z, D, B series ===
    # These are base kana + dakuten. The map includes the precomposed characters.
    '\u304C': 'ga',   # が HIRAGANA LETTER GA
    '\u304E': 'gi',   # ぎ HIRAGANA LETTER GI
    '\u3050': 'gu',   # ぐ HIRAGANA LETTER GU
    '\u3052': 'ge',   # げ HIRAGANA LETTER GE
    '\u3054': 'go',   # ご HIRAGANA LETTER GO

    '\u3056': 'za',   # ざ HIRAGANA LETTER ZA
    '\u3058': 'ji',   # じ HIRAGANA LETTER ZI (Hepburn: ji)
    '\u305A': 'zu',   # ず HIRAGANA LETTER ZU
    '\u305C': 'ze',   # ぜ HIRAGANA LETTER ZE
    '\u305E': 'zo',   # ぞ HIRAGANA LETTER ZO

    '\u3060': 'da',   # だ HIRAGANA LETTER DA
    '\u3062': 'ji',   # ぢ HIRAGANA LETTER DI (Hepburn: ji, often same as じ)
    '\u3065': 'zu',   # づ HIRAGANA LETTER DU (Hepburn: zu, often same as ず)
    '\u3067': 'de',   # で HIRAGANA LETTER DE
    '\u3069': 'do',   # ど HIRAGANA LETTER DO

    '\u3070': 'ba',   # ば HIRAGANA LETTER BA
    '\u3073': 'bi',   # び HIRAGANA LETTER BI
    '\u3076': 'bu',   # ぶ HIRAGANA LETTER BU
    '\u3079': 'be',   # べ HIRAGANA LETTER BE
    '\u307C': 'bo',   # ぼ HIRAGANA LETTER BO

    # === Semi-voiced Sounds (Handakuten ゜) - P series ===
    '\u3071': 'pa',   # ぱ HIRAGANA LETTER PA
    '\u3074': 'pi',   # ぴ HIRAGANA LETTER PI
    '\u3077': 'pu',   # ぷ HIRAGANA LETTER PU
    '\u307A': 'pe',   # ぺ HIRAGANA LETTER PE
    '\u307D': 'po',   # ぽ HIRAGANA LETTER PO

    # === Small Hiragana (often for yōon - contracted sounds, or sokuon) ===
    '\u3041': 'a',    # ぁ HIRAGANA LETTER SMALL A (used in some contexts, or for emphasis)
    '\u3043': 'i',    # ぃ HIRAGANA LETTER SMALL I
    '\u3045': 'u',    # ぅ HIRAGANA LETTER SMALL U
    '\u3047': 'e',    # ぇ HIRAGANA LETTER SMALL E
    '\u3049': 'o',    # ぉ HIRAGANA LETTER SMALL O

    '\u3063': 'small_tsu', # っ HIRAGANA LETTER SMALL TU (Sokuon - gemination marker, doubles following consonant)
                          # Representing it as "small_tsu" to distinguish. Actual transliteration logic is complex.
                          # E.g., きって (ki-small_tsu-te) -> kitte

    '\u3083': 'ya',   # ゃ HIRAGANA LETTER SMALL YA (for yōon, e.g., きゃ kya)
    '\u3085': 'yu',   # ゅ HIRAGANA LETTER SMALL YU (for yōon, e.g., きゅ kyu)
    '\u3087': 'yo',   # ょ HIRAGANA LETTER SMALL YO (for yōon, e.g., きょ kyo)

    '\u308E': 'wa',   # ゎ HIRAGANA LETTER SMALL WA (rare, for くゎ kwa etc.)

    # === Iteration Marks ===
    '\u309D': 'iteration_mark', # ゝ HIRAGANA VOICED ITERATION MARK (repeats previous kana voiced)
                                # Actual transliteration is context-dependent.
    '\u309E': 'voiced_iteration_mark', # ゞ HIRAGANA VOICED ITERATION MARK (repeats previous kana voiced)
                                     # Actual transliteration is context-dependent.

    # === Punctuation and Symbols sometimes used with Hiragana (though mostly generic punctuation) ===
    '\u3001': ',',    # 、 IDEOGRAPHIC COMMA
    '\u3002': '.',    # 。 IDEOGRAPHIC FULL STOP
    '\u30FB': '/',    # ・ KATAKANA MIDDLE DOT (used as separator, sometimes like '/')
    '\u30FC': '-',    # ー KATAKANA-HIRAGANA PROLONGED SOUND MARK (long vowel, e.g., あー ā)
                      # Simple transliteration is '-', more advanced would be doubling vowel or macron.

    # Obsolete characters (rarely used in modern Japanese)
    '\u3095': 'k',    # ゕ HIRAGANA LETTER SMALL KA (archaic)
    '\u3096': 'ke',   # ゖ HIRAGANA LETTER SMALL KE (archaic)
}