# ancient_translator/transliteration_maps/vai_map.py

SCRIPT_NAME = "vai"
DESCRIPTION = "Vai Syllabary (Liberia and Sierra Leone)"
UNICODE_RANGE = ('A500', 'A63F') # U+A500 to U+A63F

# Maps script characters to Latin transliterations
TO_LATIN_MAP = {
    # Vowels
    '\uA500': 'ee',     # ꔀ VAI SYLLABLE EE
    '\uA501': 'e',      # ꔁ VAI SYLLABLE E
    '\uA502': 'i',      # ꔂ VAI SYLLABLE I
    '\uA503': 'oo',     # ꔃ VAI SYLLABLE OO
    '\uA504': 'u',      # ꔄ VAI SYLLABLE U
    '\uA505': 'a',      # ꔅ VAI SYLLABLE A

    # Syllables (partial, full list is extensive; see Unicode chart for all)
    '\uA506': 'ba',     # ꔆ VAI SYLLABLE BA
    '\uA507': 'bɛ',     # ꔇ VAI SYLLABLE BHE
    '\uA508': 'be',     # ꔈ VAI SYLLABLE BE
    '\uA509': 'bi',     # ꔉ VAI SYLLABLE BI
    '\uA50A': 'bo',     # ꔊ VAI SYLLABLE BO
    '\uA50B': 'bu',     # ꔋ VAI SYLLABLE BU
    '\uA50C': 'bɔ',     # ꔌ VAI SYLLABLE BHO
    '\uA50D': 'bũ',     # ꔍ VAI SYLLABLE BHU
    '\uA50E': 'bã',     # ꔎ VAI SYLLABLE BHA

    '\uA50F': 'ca',     # ꔏ VAI SYLLABLE CA
    '\uA510': 'ce',     # ꔐ VAI SYLLABLE CE
    '\uA511': 'ci',     # ꔑ VAI SYLLABLE CI
    '\uA512': 'co',     # ꔒ VAI SYLLABLE CO
    '\uA513': 'cu',     # ꔓ VAI SYLLABLE CU
    '\uA514': 'cɔ',     # ꔔ VAI SYLLABLE CHO

    '\uA515': 'da',     # ꔕ VAI SYLLABLE DA
    '\uA516': 'de',     # ꔖ VAI SYLLABLE DE
    '\uA517': 'di',     # ꔗ VAI SYLLABLE DI
    '\uA518': 'do',     # ꔘ VAI SYLLABLE DO
    '\uA519': 'du',     # ꔙ VAI SYLLABLE DU
    '\uA51A': 'dɔ',     # ꔚ VAI SYLLABLE DHO

    '\uA51B': 'fa',     # ꔛ VAI SYLLABLE FA
    '\uA51C': 'fe',     # ꔜ VAI SYLLABLE FE
    '\uA51D': 'fi',     # ꔝ VAI SYLLABLE FI
    '\uA51E': 'fo',     # ꔞ VAI SYLLABLE FO
    '\uA51F': 'fu',     # ꔟ VAI SYLLABLE FU
    '\uA520': 'fɔ',     # ꔠ VAI SYLLABLE FHO

    '\uA521': 'ga',     # ꔡ VAI SYLLABLE GA
    '\uA522': 'ge',     # ꔢ VAI SYLLABLE GE
    '\uA523': 'gi',     # ꔣ VAI SYLLABLE GI
    '\uA524': 'go',     # ꔤ VAI SYLLABLE GO
    '\uA525': 'gu',     # ꔥ VAI SYLLABLE GU
    '\uA526': 'gɔ',     # ꔦ VAI SYLLABLE GHO

    '\uA527': 'ha',     # ꔧ VAI SYLLABLE HA
    '\uA528': 'he',     # ꔨ VAI SYLLABLE HE
    '\uA529': 'hi',     # ꔩ VAI SYLLABLE HI
    '\uA52A': 'ho',     # ꔪ VAI SYLLABLE HO
    '\uA52B': 'hu',     # ꔫ VAI SYLLABLE HU
    '\uA52C': 'hɔ',     # ꔬ VAI SYLLABLE HHO

    '\uA52D': 'ja',     # ꔭ VAI SYLLABLE JA
    '\uA52E': 'je',     # ꔮ VAI SYLLABLE JE
    '\uA52F': 'ji',     # ꔯ VAI SYLLABLE JI
    '\uA530': 'jo',     # ꔰ VAI SYLLABLE JO
    '\uA531': 'ju',     # ꔱ VAI SYLLABLE JU
    '\uA532': 'jɔ',     # ꔲ VAI SYLLABLE JHO

    '\uA533': 'ka',     # ꔳ VAI SYLLABLE KA
    '\uA534': 'ke',     # ꔴ VAI SYLLABLE KE
    '\uA535': 'ki',     # ꔵ VAI SYLLABLE KI
    '\uA536': 'ko',     # ꔶ VAI SYLLABLE KO
    '\uA537': 'ku',     # ꔷ VAI SYLLABLE KU
    '\uA538': 'kɔ',     # ꔸ VAI SYLLABLE KHO

    '\uA539': 'la',     # ꔹ VAI SYLLABLE LA
    '\uA53A': 'le',     # ꔺ VAI SYLLABLE LE
    '\uA53B': 'li',     # ꔻ VAI SYLLABLE LI
    '\uA53C': 'lo',     # ꔼ VAI SYLLABLE LO
    '\uA53D': 'lu',     # ꔽ VAI SYLLABLE LU
    '\uA53E': 'lɔ',     # ꔾ VAI SYLLABLE LHO

    '\uA53F': 'ma',     # ꔿ VAI SYLLABLE MA
    '\uA540': 'me',     # ꕀ VAI SYLLABLE ME
    '\uA541': 'mi',     # ꕁ VAI SYLLABLE MI
    '\uA542': 'mo',     # ꕂ VAI SYLLABLE MO
    '\uA543': 'mu',     # ꕃ VAI SYLLABLE MU
    '\uA544': 'mɔ',     # ꕄ VAI SYLLABLE MHO

    '\uA545': 'na',     # ꕅ VAI SYLLABLE NA
    '\uA546': 'ne',     # ꕆ VAI SYLLABLE NE
    '\uA547': 'ni',     # ꕇ VAI SYLLABLE NI
    '\uA548': 'no',     # ꕈ VAI SYLLABLE NO
    '\uA549': 'nu',     # ꕉ VAI SYLLABLE NU
    '\uA54A': 'nɔ',     # ꕊ VAI SYLLABLE NHO

    '\uA54B': 'ŋa',     # ꕋ VAI SYLLABLE NGA
    '\uA54C': 'ŋe',     # ꕌ VAI SYLLABLE NGE
    '\uA54D': 'ŋi',     # ꕍ VAI SYLLABLE NGI
    '\uA54E': 'ŋo',     # ꕎ VAI SYLLABLE NGO
    '\uA54F': 'ŋu',     # ꕏ VAI SYLLABLE NGU
    '\uA550': 'ŋɔ',     # ꕐ VAI SYLLABLE NGHO

    '\uA551': 'pa',     # ꕑ VAI SYLLABLE PA
    '\uA552': 'pe',     # ꕒ VAI SYLLABLE PE
    '\uA553': 'pi',     # ꕓ VAI SYLLABLE PI
    '\uA554': 'po',     # ꕔ VAI SYLLABLE PO
    '\uA555': 'pu',     # ꕕ VAI SYLLABLE PU
    '\uA556': 'pɔ',     # ꕖ VAI SYLLABLE PHO

    '\uA557': 'sa',     # ꕗ VAI SYLLABLE SA
    '\uA558': 'se',     # ꕘ VAI SYLLABLE SE
    '\uA559': 'si',     # ꕙ VAI SYLLABLE SI
    '\uA55A': 'so',     # ꕚ VAI SYLLABLE SO
    '\uA55B': 'su',     # ꕛ VAI SYLLABLE SU
    '\uA55C': 'sɔ',     # ꕜ VAI SYLLABLE SHO

    '\uA55D': 'ta',     # ꕝ VAI SYLLABLE TA
    '\uA55E': 'te',     # ꕞ VAI SYLLABLE TE
    '\uA55F': 'ti',     # ꕟ VAI SYLLABLE TI
    '\uA560': 'to',     # ꕠ VAI SYLLABLE TO
    '\uA561': 'tu',     # ꕡ VAI SYLLABLE TU
    '\uA562': 'tɔ',     # ꕢ VAI SYLLABLE THO

    '\uA563': 'va',     # ꕣ VAI SYLLABLE VA
    '\uA564': 've',     # ꕤ VAI SYLLABLE VE
    '\uA565': 'vi',     # ꕥ VAI SYLLABLE VI
    '\uA566': 'vo',     # ꕦ VAI SYLLABLE VO
    '\uA567': 'vu',     # ꕧ VAI SYLLABLE VU
    '\uA568': 'vɔ',     # ꕨ VAI SYLLABLE VHO

    '\uA569': 'wa',     # ꕩ VAI SYLLABLE WA
    '\uA56A': 'we',     # ꕪ VAI SYLLABLE WE
    '\uA56B': 'wi',     # ꕫ VAI SYLLABLE WI
    '\uA56C': 'wo',     # ꕬ VAI SYLLABLE WO
    '\uA56D': 'wu',     # ꕭ VAI SYLLABLE WU
    '\uA56E': 'wɔ',     # ꕮ VAI SYLLABLE WHO

    '\uA56F': 'ya',     # ꕯ VAI SYLLABLE YA
    '\uA570': 'ye',     # ꕰ VAI SYLLABLE YE
    '\uA571': 'yi',     # ꕱ VAI SYLLABLE YI
    '\uA572': 'yo',     # ꕲ VAI SYLLABLE YO
    '\uA573': 'yu',     # ꕳ VAI SYLLABLE YU
    '\uA574': 'yɛ',     # ꕴ VAI SYLLABLE YHE
    '\uA575': 'yɛ',     # ꕵ VAI SYLLABLE YHE
    
    '\uA576': 'za',     # ꕶ VAI SYLLABLE ZA
    '\uA577': 'ze',     # ꕷ VAI SYLLABLE ZE
    '\uA578': 'zi',     # ꕸ VAI SYLLABLE ZI
    '\uA579': 'zo',     # ꕹ VAI SYLLABLE ZO
    '\uA57A': 'zu',     # ꕺ VAI SYLLABLE ZU
    '\uA57B': 'zɔ',     # ꕻ VAI SYLLABLE ZHO

    # Digits
    '\uA620': '0',      # ꘠ VAI DIGIT ZERO
    '\uA621': '1',      # ꘡ VAI DIGIT ONE
    '\uA622': '2',      # ꘢ VAI DIGIT TWO
    '\uA623': '3',      # ꘣ VAI DIGIT THREE
    '\uA624': '4',      # ꘤ VAI DIGIT FOUR
    '\uA625': '5',      # ꘥ VAI DIGIT FIVE
    '\uA626': '6',      # ꘦ VAI DIGIT SIX
    '\uA627': '7',      # ꘧ VAI DIGIT SEVEN
    '\uA628': '8',      # ꘨ VAI DIGIT EIGHT
    '\uA629': '9',      # ꘩ VAI DIGIT NINE

    # Punctuation
    '\uA60C': ',',      # ꘌ VAI COMMA
    '\uA60D': '.',      # ꘍ VAI FULL STOP
    '\uA60E': '?',      # ꘎ VAI QUESTION MARK
    '\uA60F': ';',      # ꘏ VAI SYLLABLE LENGTHENER
    '\uA610': '!',      # ꘐ VAI EXCLAMATION MARK
    '\uA611': ':',      # ꘑ VAI COLON
    '\uA612': '(',      # ꘒ VAI LEFT PARENTHESIS
    '\uA613': ')',      # ꘓ VAI RIGHT PARENTHESIS
    '\uA614': '“',      # ꘔ VAI LEFT DOUBLE QUOTE
    '\uA615': '”',      # ꘕ VAI RIGHT DOUBLE QUOTE
    '\uA616': '‘',      # ꘖ VAI LEFT SINGLE QUOTE
    '\uA617': '’',      # ꘗ VAI RIGHT SINGLE QUOTE
    '\uA618': '…',      # ꘘ VAI ELDER SYMBOL
    '\uA619': '—',      # ꘙ VAI HYPHEN
    '\uA61A': '—',      # ꘚ VAI DASH
    '\uA61B': '—',      # ꘛ VAI LOW DASH
    '\uA61C': '—',      # ꘜ VAI HIGH DASH

    # consult the Unicode chart:
    # https://www.unicode.org/charts/PDF/UA500.pdf
}
# The above mapping is a partial representation.
# Automatically generate FROM_LATIN_MAP.
# FROM_LATIN_MAP = {v: k for k, v in TO_LATIN_MAP.items()}