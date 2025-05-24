# ancient_translator/transliteration_maps/katakana_map.py

SCRIPT_NAME = "katakana"
DESCRIPTION = "Japanese Katakana (Hepburn Romanization)"
UNICODE_RANGE = ('30A0', '30FF') # Main Katakana block U+30A0 to U+30FF
# Also considers Katakana Phonetic Extensions U+31F0–U+31FF

# Maps Katakana characters (keys) to their Hepburn Romanization (values).
TO_LATIN_MAP = {
    # === Basic Vowels ===
    '\u30A2': 'a',    # ア KATAKANA LETTER A
    '\u30A4': 'i',    # イ KATAKANA LETTER I
    '\u30A6': 'u',    # ウ KATAKANA LETTER U
    '\u30A8': 'e',    # エ KATAKANA LETTER E
    '\u30AA': 'o',    # オ KATAKANA LETTER O

    # === K-series ===
    '\u30AB': 'ka',   # カ KATAKANA LETTER KA
    '\u30AD': 'ki',   # キ KATAKANA LETTER KI
    '\u30AF': 'ku',   # ク KATAKANA LETTER KU
    '\u30B1': 'ke',   # ケ KATAKANA LETTER KE
    '\u30B3': 'ko',   # コ KATAKANA LETTER KO

    # === S-series ===
    '\u30B5': 'sa',   # サ KATAKANA LETTER SA
    '\u30B7': 'shi',  # シ KATAKANA LETTER SI (Hepburn: shi)
    '\u30B9': 'su',   # ス KATAKANA LETTER SU
    '\u30BB': 'se',   # セ KATAKANA LETTER SE
    '\u30BD': 'so',   # ソ KATAKANA LETTER SO

    # === T-series ===
    '\u30BF': 'ta',   # タ KATAKANA LETTER TA
    '\u30C1': 'chi',  # チ KATAKANA LETTER TI (Hepburn: chi)
    '\u30C4': 'tsu',  # ツ KATAKANA LETTER TU (Hepburn: tsu)
    '\u30C6': 'te',   # テ KATAKANA LETTER TE
    '\u30C8': 'to',   # ト KATAKANA LETTER TO

    # === N-series ===
    '\u30CA': 'na',   # ナ KATAKANA LETTER NA
    '\u30CB': 'ni',   # ニ KATAKANA LETTER NI
    '\u30CC': 'nu',   # ヌ KATAKANA LETTER NU
    '\u30CD': 'ne',   # ネ KATAKANA LETTER NE
    '\u30CE': 'no',   # ノ KATAKANA LETTER NO

    # === H-series ===
    '\u30CF': 'ha',   # ハ KATAKANA LETTER HA
    '\u30D2': 'hi',   # ヒ KATAKANA LETTER HI
    '\u30D5': 'fu',   # フ KATAKANA LETTER HU (Hepburn: fu)
    '\u30D8': 'he',   # ヘ KATAKANA LETTER HE
    '\u30DB': 'ho',   # ホ KATAKANA LETTER HO

    # === M-series ===
    '\u30DE': 'ma',   # マ KATAKANA LETTER MA
    '\u30DF': 'mi',   # ミ KATAKANA LETTER MI
    '\u30E0': 'mu',   # ム KATAKANA LETTER MU
    '\u30E1': 'me',   # メ KATAKANA LETTER ME
    '\u30E2': 'mo',   # モ KATAKANA LETTER MO

    # === Y-series ===
    '\u30E4': 'ya',   # ヤ KATAKANA LETTER YA
    '\u30E6': 'yu',   # ユ KATAKANA LETTER YU
    '\u30E8': 'yo',   # ヨ KATAKANA LETTER YO

    # === R-series ===
    '\u30E9': 'ra',   # ラ KATAKANA LETTER RA
    '\u30EA': 'ri',   # リ KATAKANA LETTER RI
    '\u30EB': 'ru',   # ル KATAKANA LETTER RU
    '\u30EC': 're',   # レ KATAKANA LETTER RE
    '\u30ED': 'ro',   # ロ KATAKANA LETTER RO

    # === W-series ===
    '\u30EF': 'wa',   # ワ KATAKANA LETTER WA
    '\u30F0': 'wi',   # ヰ KATAKANA LETTER WI (obsolete, transliterated 'wi')
    '\u30F1': 'we',   # ヱ KATAKANA LETTER WE (obsolete, transliterated 'we')
    '\u30F2': 'o',    # ヲ KATAKANA LETTER WO (obsolete for sound 'wo', now almost exclusively for particle in Hiragana)
                      # In Katakana, it's extremely rare. Usually transliterated 'wo' if encountered for historical reasons.
                      # For consistency with its Hiragana particle use (pronounced 'o'), mapping to 'o' is an option,
                      # but 'wo' is often seen for its Katakana form if it ever appears. Let's use 'wo'.
    '\u30F2': 'wo',   # ヲ KATAKANA LETTER WO (obsolete)

    # === N (syllabic) ===
    '\u30F3': 'n',    # ン KATAKANA LETTER N (syllabic N)

    # === Voiced Sounds (Dakuten ゙ ) - G, Z, D, B series ===
    '\u30AC': 'ga',   # ガ KATAKANA LETTER GA
    '\u30AE': 'gi',   # ギ KATAKANA LETTER GI
    '\u30B0': 'gu',   # グ KATAKANA LETTER GU
    '\u30B2': 'ge',   # ゲ KATAKANA LETTER GE
    '\u30B4': 'go',   # ゴ KATAKANA LETTER GO

    '\u30B6': 'za',   # ザ KATAKANA LETTER ZA
    '\u30B8': 'ji',   # ジ KATAKANA LETTER ZI (Hepburn: ji)
    '\u30BA': 'zu',   # ズ KATAKANA LETTER ZU
    '\u30BC': 'ze',   # ゼ KATAKANA LETTER ZE
    '\u30BE': 'zo',   # ゾ KATAKANA LETTER ZO

    '\u30C0': 'da',   # ダ KATAKANA LETTER DA
    '\u30C2': 'ji',   # ヂ KATAKANA LETTER DI (Hepburn: ji, often same as ジ)
    '\u30C5': 'zu',   # ヅ KATAKANA LETTER DU (Hepburn: zu, often same as ズ) - Small version ッ is sokuon.
    '\u30C7': 'de',   # デ KATAKANA LETTER DE
    '\u30C9': 'do',   # ド KATAKANA LETTER DO

    '\u30D0': 'ba',   # バ KATAKANA LETTER BA
    '\u30D3': 'bi',   # ビ KATAKANA LETTER BI
    '\u30D6': 'bu',   # ブ KATAKANA LETTER BU
    '\u30D9': 'be',   # ベ KATAKANA LETTER BE
    '\u30DC': 'bo',   # ボ KATAKANA LETTER BO

    # === Semi-voiced Sounds (Handakuten ゜) - P series ===
    '\u30D1': 'pa',   # パ KATAKANA LETTER PA
    '\u30D4': 'pi',   # ピ KATAKANA LETTER PI
    '\u30D7': 'pu',   # プ KATAKANA LETTER PU
    '\u30DA': 'pe',   # ペ KATAKANA LETTER PE
    '\u30DD': 'po',   # ポ KATAKANA LETTER PO

    # === Small Katakana (for yōon, sokuon, foreign sounds) ===
    '\u30A1': 'a',    # ァ KATAKANA LETTER SMALL A
    '\u30A3': 'i',    # ィ KATAKANA LETTER SMALL I
    '\u30A5': 'u',    # ゥ KATAKANA LETTER SMALL U
    '\u30A7': 'e',    # ェ KATAKANA LETTER SMALL E
    '\u30A9': 'o',    # ォ KATAKANA LETTER SMALL O

    '\u30C3': 'small_tsu', # ッ KATAKANA LETTER SMALL TU (Sokuon - gemination marker)
    '\u30E3': 'ya',   # ャ KATAKANA LETTER SMALL YA
    '\u30E5': 'yu',   # ュ KATAKANA LETTER SMALL YU
    '\u30E7': 'yo',   # ョ KATAKANA LETTER SMALL YO

    '\u30EE': 'wa',   # ヮ KATAKANA LETTER SMALL WA (rare)
    '\u30F5': 'ka',   # ヵ KATAKANA LETTER SMALL KA (archaic or specific uses)
    '\u30F6': 'ke',   # ヶ KATAKANA LETTER SMALL KE (archaic or specific uses, like in 一ヶ月 ikkagetsu)

    # === Special Katakana for foreign sounds / extended use (often with small vowels) ===
    # These often combine with small vowels. Example: ヴァ (va) = ヴ + ァ
    '\u30F4': 'vu',   # ヴ KATAKANA LETTER VU (for 'v' sound, e.g., ヴァ va, ヴィ vi, ヴェ ve, ヴォ vo)

    # === Iteration Marks ===
    '\u30FD': 'iteration_mark',       # ヽ KATAKANA ITERATION MARK
    '\u30FE': 'voiced_iteration_mark',# ヾ KATAKANA VOICED ITERATION MARK

    # === Punctuation and Symbols (shared with Hiragana or generic) ===
    # '\u3001': ',',    # 、 IDEOGRAPHIC COMMA (already in Hiragana map if sharing)
    # '\u3002': '.',    # 。 IDEOGRAPHIC FULL STOP (already in Hiragana map if sharing)
    '\u30FB': '/',    # ・ KATAKANA MIDDLE DOT (often used in Katakana names, like '/')
    '\u30FC': '-',    # ー KATAKANA-HIRAGANA PROLONGED SOUND MARK (long vowel)

    # === Katakana Phonetic Extensions (U+31F0–U+31FF) ===
    # Mostly for Ainu language and some archaic forms.
    '\u31F0': 'small_ku', # ㇰ KATAKANA LETTER SMALL KU
    '\u31F1': 'small_si', # ㇱ KATAKANA LETTER SMALL SI
    '\u31F2': 'small_su', # ㇲ KATAKANA LETTER SMALL SU
    '\u31F3': 'small_to', # ㇳ KATAKANA LETTER SMALL TO
    '\u31F4': 'small_nu', # ㇴ KATAKANA LETTER SMALL NU
    '\u31F5': 'small_ha', # ㇵ KATAKANA LETTER SMALL HA
    '\u31F6': 'small_hi', # ㇶ KATAKANA LETTER SMALL HI
    '\u31F7': 'small_fu', # ㇷ KATAKANA LETTER SMALL FU
    '\u31F8': 'small_he', # ㇸ KATAKANA LETTER SMALL HE
    '\u31F9': 'small_ho', # ㇹ KATAKANA LETTER SMALL HO
    '\u31FA': 'small_mu', # ㇺ KATAKANA LETTER SMALL MU
    '\u31FB': 'small_ra', # ㇻ KATAKANA LETTER SMALL RA
    '\u31FC': 'small_ri', # ㇼ KATAKANA LETTER SMALL RI
    '\u31FD': 'small_ru', # ㇽ KATAKANA LETTER SMALL RU
    '\u31FE': 'small_re', # ㇾ KATAKANA LETTER SMALL RE
    '\u31FF': 'small_ro', # ㇿ KATAKANA LETTER SMALL RO
}
