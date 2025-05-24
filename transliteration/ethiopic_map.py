# ancient_translator/transliteration_maps/ethiopic_map.py

SCRIPT_NAME = "ethiopic"
DESCRIPTION = "Ethiopic (Ge'ez Fidel - Amharic/Tigrinya focus)"
UNICODE_RANGE = ('1200', '137F') # Main Ethiopic block

# Maps Ethiopic (Ge'ez) characters (keys) to their common Latin transliterations (values).
# Based on the 7 orders/vowel forms for each consonant series.
TO_LATIN_MAP = {
    # === Həylet Həylet (Vowels) ===
    '\u12A0': 'hä',   # ሀ ETHIOPIC SYLLABLE HA (Sometimes transliterated 'he')
    '\u12A1': 'hu',   # ሁ ETHIOPIC SYLLABLE HU
    '\u12A2': 'hi',   # ሂ ETHIOPIC SYLLABLE HI
    '\u12A3': 'ha',   # ሃ ETHIOPIC SYLLABLE HAA (long 'a')
    '\u12A4': 'he',   # ሄ ETHIOPIC SYLLABLE HEE (long 'e')
    '\u12A5': 'hə',   # ህ ETHIOPIC SYLLABLE HE (schwa, or 'h' with no vowel)
    '\u12A6': 'ho',   # ሆ ETHIOPIC SYLLABLE HO

    # === Lamed ===
    '\u1208': 'lä',   # ለ ETHIOPIC SYLLABLE LA
    '\u1209': 'lu',   # ሉ ETHIOPIC SYLLABLE LU
    '\u120A': 'li',   # ሊ ETHIOPIC SYLLABLE LI
    '\u120B': 'la',   # ላ ETHIOPIC SYLLABLE LAA
    '\u120C': 'le',   # ሌ ETHIOPIC SYLLABLE LEE
    '\u120D': 'lə',   # ል ETHIOPIC SYLLABLE LE (schwa)
    '\u120E': 'lo',   # ሎ ETHIOPIC SYLLABLE LO
    # Labialized L
    '\u120F': 'lʷa',  # ሏ ETHIOPIC SYLLABLE LWA (or loa)

    # === Ḥawṭ === (ḥ - pharyngeal H)
    '\u1210': 'ḥä',   # ሐ ETHIOPIC SYLLABLE HHAUT
    '\u1211': 'ḥu',   # ሑ ETHIOPIC SYLLABLE HHU
    '\u1212': 'ḥi',   # ሒ ETHIOPIC SYLLABLE HHI
    '\u1213': 'ḥa',   # ሓ ETHIOPIC SYLLABLE HHAA
    '\u1214': 'ḥe',   #ሔ ETHIOPIC SYLLABLE HHEE
    '\u1215': 'ḥə',   # ሕ ETHIOPIC SYLLABLE HHE
    '\u1216': 'ḥo',   # ሖ ETHIOPIC SYLLABLE HHO
    # Labialized Ḥ
    '\u1217': 'ḥʷa',  # ሗ ETHIOPIC SYLLABLE HHWA

    # === May === (m)
    '\u1218': 'mä',   # መ ETHIOPIC SYLLABLE MA
    '\u1219': 'mu',   # ሙ ETHIOPIC SYLLABLE MU
    '\u121A': 'mi',   # ሚ ETHIOPIC SYLLABLE MI
    '\u121B': 'ma',   # ማ ETHIOPIC SYLLABLE MAA
    '\u121C': 'me',   # ሜ ETHIOPIC SYLLABLE MEE
    '\u121D': 'mə',   # ም ETHIOPIC SYLLABLE ME (schwa)
    '\u121E': 'mo',   # ሞ ETHIOPIC SYLLABLE MO
    # Labialized M
    '\u121F': 'mʷa',  # ሟ ETHIOPIC SYLLABLE MWA

    # === Śawṭ === (ś - like 'sh' but different from 'š')
    '\u1220': 'śä',   # ሠ ETHIOPIC SYLLABLE SSAUT
    '\u1221': 'śu',   # ሡ ETHIOPIC SYLLABLE SSU
    '\u1222': 'śi',   # ሢ ETHIOPIC SYLLABLE SSI
    '\u1223': 'śa',   # ሣ ETHIOPIC SYLLABLE SSAA
    '\u1224': 'śe',   # ሤ ETHIOPIC SYLLABLE SSEE
    '\u1225': 'śə',   # ሥ ETHIOPIC SYLLABLE SSE
    '\u1226': 'śo',   # ሦ ETHIOPIC SYLLABLE SSO
    # Labialized Ś
    '\u1227': 'śʷa',  # ሧ ETHIOPIC SYLLABLE SSWA

    # === Reʾs === (r)
    '\u1228': 'rä',   # ረ ETHIOPIC SYLLABLE RA
    '\u1229': 'ru',   # ሩ ETHIOPIC SYLLABLE RU
    '\u122A': 'ri',   # ሪ ETHIOPIC SYLLABLE RI
    '\u122B': 'ra',   # ራ ETHIOPIC SYLLABLE RAA
    '\u122C': 're',   # ሬ ETHIOPIC SYLLABLE REE
    '\u122D': 'rə',   # ር ETHIOPIC SYLLABLE RE (schwa)
    '\u122E': 'ro',   # ሮ ETHIOPIC SYLLABLE RO
    # Labialized R (rare in Amharic, more in other languages)
    '\u122F': 'rʷa',  # ሯ ETHIOPIC SYLLABLE RWA

    # === Sat === (s)
    '\u1230': 'sä',   # ሰ ETHIOPIC SYLLABLE SA
    '\u1231': 'su',   # ሱ ETHIOPIC SYLLABLE SU
    '\u1232': 'si',   # ሲ ETHIOPIC SYLLABLE SI
    '\u1233': 'sa',   # ሳ ETHIOPIC SYLLABLE SAA
    '\u1234': 'se',   # ሴ ETHIOPIC SYLLABLE SEE
    '\u1235': 'sə',   # ስ ETHIOPIC SYLLABLE SE (schwa)
    '\u1236': 'so',   # ሶ ETHIOPIC SYLLABLE SO
    # Labialized S
    '\u1237': 'sʷa',  # ሷ ETHIOPIC SYLLABLE SWA

    # === Šat === (š - "sh" as in "shoe")
    '\u1238': 'šä',   # ሸ ETHIOPIC SYLLABLE SHA
    '\u1239': 'šu',   # ሹ ETHIOPIC SYLLABLE SHU
    '\u123A': 'ši',   # ሺ ETHIOPIC SYLLABLE SHI
    '\u123B': 'ša',   # ሻ ETHIOPIC SYLLABLE SHAA
    '\u123C': 'še',   # ሼ ETHIOPIC SYLLABLE SHEE
    '\u123D': 'šə',   # ሽ ETHIOPIC SYLLABLE SHE (schwa)
    '\u123E': 'šo',   # ሾ ETHIOPIC SYLLABLE SHO
    # Labialized Š
    '\u123F': 'šʷa',  # ሿ ETHIOPIC SYLLABLE SHWA

    # === Qaf === (q or q̣ - uvular ejective k')
    '\u1240': 'qä',   # ቀ ETHIOPIC SYLLABLE QA
    '\u1241': 'qu',   # ቁ ETHIOPIC SYLLABLE QU
    '\u1242': 'qi',   # ቂ ETHIOPIC SYLLABLE QI
    '\u1243': 'qa',   # ቃ ETHIOPIC SYLLABLE QAA
    '\u1244': 'qe',   # ቄ ETHIOPIC SYLLABLE QEE
    '\u1245': 'qə',   # ቅ ETHIOPIC SYLLABLE QE (schwa)
    '\u1246': 'qo',   # ቆ ETHIOPIC SYLLABLE QO
    # Labialized Q series (Qʷ)
    '\u1248': 'qʷä',  # ቈ ETHIOPIC SYLLABLE QWA (or qwe)
    # U+1249, U+124F are unassigned
    '\u124A': 'qʷi',  # ቊ ETHIOPIC SYLLABLE QWI
    '\u124B': 'qʷa',  # ቋ ETHIOPIC SYLLABLE QWAA
    '\u124C': 'qʷe',  # ቌ ETHIOPIC SYLLABLE QWEE
    '\u124D': 'qʷə',  # ቍ ETHIOPIC SYLLABLE QWE (schwa)

    # === Bet === (b)
    '\u1260': 'bä',   # በ ETHIOPIC SYLLABLE BA
    '\u1261': 'bu',   # ቡ ETHIOPIC SYLLABLE BU
    '\u1262': 'bi',   # ቢ ETHIOPIC SYLLABLE BI
    '\u1263': 'ba',   # ባ ETHIOPIC SYLLABLE BAA
    '\u1264': 'be',   # ቤ ETHIOPIC SYLLABLE BEE
    '\u1265': 'bə',   # ብ ETHIOPIC SYLLABLE BE (schwa)
    '\u1266': 'bo',   # ቦ ETHIOPIC SYLLABLE BO
    # Labialized B
    '\u1267': 'bʷa',  # ቧ ETHIOPIC SYLLABLE BWA

    # === Täwe === (t)
    '\u1270': 'tä',   # ተ ETHIOPIC SYLLABLE TA
    '\u1271': 'tu',   # ቱ ETHIOPIC SYLLABLE TU
    '\u1272': 'ti',   # ቲ ETHIOPIC SYLLABLE TI
    '\u1273': 'ta',   # ታ ETHIOPIC SYLLABLE TAA
    '\u1274': 'te',   # ቴ ETHIOPIC SYLLABLE TEE
    '\u1275': 'tə',   # ት ETHIOPIC SYLLABLE TE (schwa)
    '\u1276': 'to',   # ቶ ETHIOPIC SYLLABLE TO
    # Labialized T
    '\u1277': 'tʷa',  # ቷ ETHIOPIC SYLLABLE TWA

    # === Č̣awi === (č or ch - affricate like "church")
    '\u1278': 'čä',   # ቸ ETHIOPIC SYLLABLE CA (Amharic CH sound)
    '\u1279': 'ču',   # ቹ ETHIOPIC SYLLABLE CU
    '\u127A': 'či',   # ቺ ETHIOPIC SYLLABLE CI
    '\u127B': 'ča',   # ቻ ETHIOPIC SYLLABLE CAA
    '\u127C': 'če',   # ቼ ETHIOPIC SYLLABLE CEE
    '\u127D': 'čə',   # ች ETHIOPIC SYLLABLE CE (schwa)
    '\u127E': 'čo',   # ቾ ETHIOPIC SYLLABLE CO
    # Labialized Č
    '\u127F': 'čʷa',  # ቿ ETHIOPIC SYLLABLE CWA

    # === Ḫarm === (ḫ - voiceless velar or uvular fricative, like German 'ch' in 'Bach')
    # This series is mostly for Ge'ez or other Semitic languages, less common in modern Amharic.
    '\u1280': 'ḫä',   # ኀ ETHIOPIC SYLLABLE XA (older transliteration)
    '\u1281': 'ḫu',   # ኁ ETHIOPIC SYLLABLE XU
    '\u1282': 'ḫi',   # ኂ ETHIOPIC SYLLABLE XI
    '\u1283': 'ḫa',   # ኃ ETHIOPIC SYLLABLE XAA
    '\u1284': 'ḫe',   # ኄ ETHIOPIC SYLLABLE XEE
    '\u1285': 'ḫə',   # ኅ ETHIOPIC SYLLABLE XE (schwa)
    '\u1286': 'ḫo',   # ኆ ETHIOPIC SYLLABLE XO
    # Labialized Ḫ series (Ḫʷ)
    '\u1288': 'ḫʷä',  # ኈ ETHIOPIC SYLLABLE XWA
    # U+1289, U+128F are unassigned
    '\u128A': 'ḫʷi',  # ኊ ETHIOPIC SYLLABLE XWI
    '\u128B': 'ḫʷa',  # ቋ ETHIOPIC SYLLABLE XWAA (Note: same glyph as QWAA U+124B in some fonts, but different char)
                      # This is actually a known issue. U+128B is ኋ.
    '\u128B': 'ḫʷa',  # ኋ ETHIOPIC SYLLABLE XWAA
    '\u128C': 'ḫʷe',  # ኌ ETHIOPIC SYLLABLE XWEE
    '\u128D': 'ḫʷə',  # ኍ ETHIOPIC SYLLABLE XWE (schwa)

    # === Nähas === (n)
    '\u1290': 'nä',   # ነ ETHIOPIC SYLLABLE NA
    '\u1291': 'nu',   # ኑ ETHIOPIC SYLLABLE NU
    '\u1292': 'ni',   # ኒ ETHIOPIC SYLLABLE NI
    '\u1293': 'na',   # ና ETHIOPIC SYLLABLE NAA
    '\u1294': 'ne',   # ኔ ETHIOPIC SYLLABLE NEE
    '\u1295': 'nə',   # ን ETHIOPIC SYLLABLE NE (schwa)
    '\u1296': 'no',   # ኖ ETHIOPIC SYLLABLE NO
    # Labialized N
    '\u1297': 'nʷa',  # ኗ ETHIOPIC SYLLABLE NWA

    # === Ña === (ñ - palatal nasal, like Spanish 'ñ' or 'ny' in "canyon") (Amharic)
    '\u1298': 'ñä',   # ኘ ETHIOPIC SYLLABLE NYA (Amharic)
    '\u1299': 'ñu',   # ኙ ETHIOPIC SYLLABLE NYU
    '\u129A': 'ñi',   # ኚ ETHIOPIC SYLLABLE NYI
    '\u129B': 'ña',   # ኛ ETHIOPIC SYLLABLE NYAA
    '\u129C': 'ñe',   # ኜ ETHIOPIC SYLLABLE NYEE
    '\u129D': 'ñə',   # ኝ ETHIOPIC SYLLABLE NYE (schwa)
    '\u129E': 'ño',   # ኞ ETHIOPIC SYLLABLE NYO
    # Labialized Ñ
    '\u129F': 'ñʷa',  # ኟ ETHIOPIC SYLLABLE NYWA

    # === ʼAlef === (ʼ - glottal stop, like the pause in "uh-oh")
    '\u12A8': 'ʼä',   # አ ETHIOPIC SYLLABLE GLOTTAL A
    '\u12A9': 'ʼu',   # ኡ ETHIOPIC SYLLABLE GLOTTAL U
    '\u12AA': 'ʼi',   # ኢ ETHIOPIC SYLLABLE GLOTTAL I
    '\u12AB': 'ʼa',   # ኣ ETHIOPIC SYLLABLE GLOTTAL AA
    '\u12AC': 'ʼe',   # ኤ ETHIOPIC SYLLABLE GLOTTAL EE
    '\u12AD': 'ʼə',   # እ ETHIOPIC SYLLABLE GLOTTAL E (schwa)
    '\u12AE': 'ʼo',   # ኦ ETHIOPIC SYLLABLE GLOTTAL O
    # Labialized ʼ (rare)
    # '\u12AF': 'ʼʷa', # ኧ ETHIOPIC SYLLABLE GLOTTAL WA - U+12AF is actually "ETHIOPIC SYLLABLE WA" (see Wawē below)

    # === Kaf === (k)
    '\u12B0': 'kä',   # ከ ETHIOPIC SYLLABLE KA
    '\u12B1': 'ku',   # ኩ ETHIOPIC SYLLABLE KU
    '\u12B2': 'ki',   # ኪ ETHIOPIC SYLLABLE KI
    '\u12B3': 'ka',   # ካ ETHIOPIC SYLLABLE KAA
    '\u12B4': 'ke',   # ኬ ETHIOPIC SYLLABLE KEE
    '\u12B5': 'kə',   # ክ ETHIOPIC SYLLABLE KE (schwa)
    '\u12B6': 'ko',   # ኮ ETHIOPIC SYLLABLE KO
    # Labialized K series (Kʷ)
    '\u12B8': 'kʷä',  # ኰ ETHIOPIC SYLLABLE KWA
    # U+12B9, U+12BF are unassigned
    '\u12BA': 'kʷi',  # ኲ ETHIOPIC SYLLABLE KWI
    '\u12BB': 'kʷa',  # ኳ ETHIOPIC SYLLABLE KWAA
    '\u12BC': 'kʷe',  # ኴ ETHIOPIC SYLLABLE KWEE
    '\u12BD': 'kʷə',  # ኵ ETHIOPIC SYLLABLE KWE (schwa)

    # === Wäwē === (w)
    '\u12C8': 'wä',   # ወ ETHIOPIC SYLLABLE WA (modern Amharic 'wä')
    '\u12C9': 'wu',   # ዉ ETHIOPIC SYLLABLE WU
    '\u12CA': 'wi',   # ዊ ETHIOPIC SYLLABLE WI
    '\u12CB': 'wa',   # ዋ ETHIOPIC SYLLABLE WAA
    '\u12CC': 'we',   # ዌ ETHIOPIC SYLLABLE WEE
    '\u12CD': 'wə',   # ው ETHIOPIC SYLLABLE WE (schwa)
    '\u12CE': 'wo',   # ዎ ETHIOPIC SYLLABLE WO

    # === ʿAyn === (ʿ - voiced pharyngeal fricative)
    '\u12D0': 'ʿä',   # ዐ ETHIOPIC SYLLABLE AIN
    '\u12D1': 'ʿu',   # ዑ ETHIOPIC SYLLABLE AU
    '\u12D2': 'ʿi',   # ዒ ETHIOPIC SYLLABLE AI
    '\u12D3': 'ʿa',   # ዓ ETHIOPIC SYLLABLE AAA
    '\u12D4': 'ʿe',   # ዔ ETHIOPIC SYLLABLE AEE
    '\u12D5': 'ʿə',   # ዕ ETHIOPIC SYLLABLE AE
    '\u12D6': 'ʿo',   # ዖ ETHIOPIC SYLLABLE AO
    # No standard labialized forms for ʿAyn in Unicode main block

    # === Zäy === (z)
    '\u12D8': 'zä',   # ዘ ETHIOPIC SYLLABLE ZA
    '\u12D9': 'zu',   # ዙ ETHIOPIC SYLLABLE ZU
    '\u12DA': 'zi',   # ዚ ETHIOPIC SYLLABLE ZI
    '\u12DB': 'za',   # ዛ ETHIOPIC SYLLABLE ZAA
    '\u12DC': 'ze',   # ዜ ETHIOPIC SYLLABLE ZEE
    '\u12DD': 'zə',   # ዝ ETHIOPIC SYLLABLE ZE (schwa)
    '\u12DE': 'zo',   # ዞ ETHIOPIC SYLLABLE ZO
    # Labialized Z
    '\u12DF': 'zʷa',  # ዟ ETHIOPIC SYLLABLE ZWA

    # === Žäy === (ž - like 's' in "measure" or French 'j') (Amharic)
    '\u12E0': 'žä',   # ዠ ETHIOPIC SYLLABLE ZHA (Amharic ZH sound)
    '\u12E1': 'žu',   # ዡ ETHIOPIC SYLLABLE ZHU
    '\u12E2': 'ži',   # ዢ ETHIOPIC SYLLABLE ZHI
    '\u12E3': 'ža',   # ዣ ETHIOPIC SYLLABLE ZHAA
    '\u12E4': 'že',   # ዤ ETHIOPIC SYLLABLE ZHEE
    '\u12E5': 'žə',   # ዥ ETHIOPIC SYLLABLE ZHE (schwa)
    '\u12E6': 'žo',   # ዦ ETHIOPIC SYLLABLE ZHO
    # Labialized Ž
    '\u12E7': 'žʷa',  # ዧ ETHIOPIC SYLLABLE ZHWA

    # === Yämän === (y)
    '\u12E8': 'yä',   # የ ETHIOPIC SYLLABLE YA
    '\u12E9': 'yu',   # ዩ ETHIOPIC SYLLABLE YU
    '\u12EA': 'yi',   #ዪ ETHIOPIC SYLLABLE YI
    '\u12EB': 'ya',   # ያ ETHIOPIC SYLLABLE YAA
    '\u12EC': 'ye',   #ዬ ETHIOPIC SYLLABLE YEE
    '\u12ED': 'yə',   # ይ ETHIOPIC SYLLABLE YE (schwa)
    '\u12EE': 'yo',   # ዮ ETHIOPIC SYLLABLE YO
    # No standard labialized forms for Yämän in Unicode main block

    # === Dänt === (d)
    '\u12F0': 'dä',   # ደ ETHIOPIC SYLLABLE DA
    '\u12F1': 'du',   # ዱ ETHIOPIC SYLLABLE DU
    '\u12F2': 'di',   # ዲ ETHIOPIC SYLLABLE DI
    '\u12F3': 'da',   # ዳ ETHIOPIC SYLLABLE DAA
    '\u12F4': 'de',   # ዴ ETHIOPIC SYLLABLE DEE
    '\u12F5': 'də',   # ድ ETHIOPIC SYLLABLE DE (schwa)
    '\u12F6': 'do',   # ዶ ETHIOPIC SYLLABLE DO
    # Labialized D
    '\u12F7': 'dʷa',  # ዷ ETHIOPIC SYLLABLE DWA

    # === J̌änt === (ǰ or j - affricate like "judge") (Amharic)
    '\u1300': 'ǧä',   # ጀ ETHIOPIC SYLLABLE JA (Amharic J sound, often written 'j')
    '\u1301': 'ǧu',   # ጁ ETHIOPIC SYLLABLE JU
    '\u1302': 'ǧi',   # ጂ ETHIOPIC SYLLABLE JI
    '\u1303': 'ǧa',   # ጃ ETHIOPIC SYLLABLE JAA
    '\u1304': 'ǧe',   # ጄ ETHIOPIC SYLLABLE JEE
    '\u1305': 'ǧə',   # ጅ ETHIOPIC SYLLABLE JE (schwa)
    '\u1306': 'ǧo',   # ጆ ETHIOPIC SYLLABLE JO
    # Labialized J̌
    '\u1307': 'ǧʷa',  # ጇ ETHIOPIC SYLLABLE JWA

    # === Gäml === (g)
    '\u1308': 'gä',   # ገ ETHIOPIC SYLLABLE GA
    '\u1309': 'gu',   # ጉ ETHIOPIC SYLLABLE GU
    '\u130A': 'gi',   # ጊ ETHIOPIC SYLLABLE GI
    '\u130B': 'ga',   # ጋ ETHIOPIC SYLLABLE GAA
    '\u130C': 'ge',   # ጌ ETHIOPIC SYLLABLE GEE
    '\u130D': 'gə',   # ግ ETHIOPIC SYLLABLE GE (schwa)
    '\u130E': 'go',   # ጎ ETHIOPIC SYLLABLE GO
    # Labialized G series (Gʷ)
    '\u1310': 'gʷä',  # ጐ ETHIOPIC SYLLABLE GWA
    # U+1311 is unassigned
    '\u1312': 'gʷi',  # ጒ ETHIOPIC SYLLABLE GWI
    '\u1313': 'gʷa',  # ጓ ETHIOPIC SYLLABLE GWAA
    '\u1314': 'gʷe',  # ጔ ETHIOPIC SYLLABLE GWEE
    '\u1315': 'gʷə',  #  Guilherme ETHIOPIC SYLLABLE GWE (schwa)

    # ===Ṭäyt === (ṭ or t' - ejective t)
    '\u1320': 'ṭä',   # ጠ ETHIOPIC SYLLABLE TTA
    '\u1321': 'ṭu',   # ጡ ETHIOPIC SYLLABLE TTU
    '\u1322': 'ṭi',   # ጢ ETHIOPIC SYLLABLE TTI
    '\u1323': 'ṭa',   # ጣ ETHIOPIC SYLLABLE TTAA
    '\u1324': 'ṭe',   # ጤ ETHIOPIC SYLLABLE TTEE
    '\u1325': 'ṭə',   # ጥ ETHIOPIC SYLLABLE TTE (schwa)
    '\u1326': 'ṭo',   # ጦ ETHIOPIC SYLLABLE TTO
    # Labialized Ṭ
    '\u1327': 'ṭʷa',  # ጧ ETHIOPIC SYLLABLE TTWA

    # === Č̣äyt === (č̣ or ch' - ejective ch) (Amharic)
    '\u1328': 'č̣ä',   # ጨ ETHIOPIC SYLLABLE CCHA (Amharic CH' sound)
    '\u1329': 'č̣u',   #ጩ ETHIOPIC SYLLABLE CCHU
    '\u132A': 'č̣i',   #ጪ ETHIOPIC SYLLABLE CCHI
    '\u132B': 'č̣a',   #ጫ ETHIOPIC SYLLABLE CCHAA
    '\u132C': 'č̣e',   #ጬ ETHIOPIC SYLLABLE CCHEE
    '\u132D': 'č̣ə',   #ጭ ETHIOPIC SYLLABLE CCHE (schwa)
    '\u132E': 'č̣o',   #ጮ ETHIOPIC SYLLABLE CCHO
    # Labialized Č̣
    '\u132F': 'č̣ʷa',  # ጯ ETHIOPIC SYLLABLE CCHWA

    # === P̣äyt === (p̣ or p' - ejective p)
    '\u1330': 'p̣ä',   # ጰ ETHIOPIC SYLLABLE PPA
    '\u1331': 'p̣u',   # ጱ ETHIOPIC SYLLABLE PPU
    '\u1332': 'p̣i',   # ጲ ETHIOPIC SYLLABLE PPI
    '\u1333': 'p̣a',   # ጳ ETHIOPIC SYLLABLE PPAA
    '\u1334': 'p̣e',   # ጴ ETHIOPIC SYLLABLE PPEE
    '\u1335': 'p̣ə',   # ጵ ETHIOPIC SYLLABLE PPE (schwa)
    '\u1336': 'p̣o',   # ጶ ETHIOPIC SYLLABLE PPO
    # Labialized P̣
    '\u1337': 'p̣ʷa',  # ጷ ETHIOPIC SYLLABLE PPWA

    # === Ṣädäy === (ṣ or ts' - ejective s)
    '\u1338': 'ṣä',   # ጸ ETHIOPIC SYLLABLE TZA
    '\u1339': 'ṣu',   # ጹ ETHIOPIC SYLLABLE TZU
    '\u133A': 'ṣi',   # ጺ ETHIOPIC SYLLABLE TZI
    '\u133B': 'ṣa',   # ጻ ETHIOPIC SYLLABLE TZAA
    '\u133C': 'ṣe',   # ጼ ETHIOPIC SYLLABLE TZEE
    '\u133D': 'ṣə',   # ጽ ETHIOPIC SYLLABLE TZE (schwa)
    '\u133E': 'ṣo',   # ጾ ETHIOPIC SYLLABLE TZO
    # Labialized Ṣ
    '\u133F': 'ṣʷa',  # ጿ ETHIOPIC SYLLABLE TZWA

    # === Ẓädäy === (ẓ - sometimes like 'ts', related to Ṣädäy, Ge'ez only)
    '\u1340': 'ẓä',   # ፀ ETHIOPIC SYLLABLE ZZA (rare, often merged with ጸ in Amharic)
    '\u1341': 'ẓu',   # ፁ ETHIOPIC SYLLABLE ZZU
    '\u1342': 'ẓi',   # ፂ ETHIOPIC SYLLABLE ZZI
    '\u1343': 'ẓa',   # ፃ ETHIOPIC SYLLABLE ZZAA
    '\u1344': 'ẓe',   # ፄ ETHIOPIC SYLLABLE ZZEE
    '\u1345': 'ẓə',   # ፅ ETHIOPIC SYLLABLE ZZE (schwa)
    '\u1346': 'ẓo',   # ፆ ETHIOPIC SYLLABLE ZZO
    # Labialized Ẓ (very rare)
    # '\u1347': 'ẓʷa', # ፇ ETHIOPIC SYLLABLE ZZWA (U+1347 is unassigned)

    # === Fä === (f) (For foreign words, more common in Amharic)
    '\u1348': 'fä',   # ፈ ETHIOPIC SYLLABLE FA
    '\u1349': 'fu',   # ፉ ETHIOPIC SYLLABLE FU
    '\u134A': 'fi',   # ፊ ETHIOPIC SYLLABLE FI
    '\u134B': 'fa',   # ፋ ETHIOPIC SYLLABLE FAA
    '\u134C': 'fe',   # ፌ ETHIOPIC SYLLABLE FEE
    '\u134D': 'fə',   # ፍ ETHIOPIC SYLLABLE FE (schwa)
    '\u134E': 'fo',   # ፎ ETHIOPIC SYLLABLE FO
    # Labialized F
    '\u134F': 'fʷa',  # ፏ ETHIOPIC SYLLABLE FWA

    # === Pä === (p) (For foreign words, more common in Amharic)
    '\u1350': 'pä',   # ፐ ETHIOPIC SYLLABLE PA
    '\u1351': 'pu',   # ፑ ETHIOPIC SYLLABLE PU
    '\u1352': 'pi',   # ፒ ETHIOPIC SYLLABLE PI
    '\u1353': 'pa',   # ፓ ETHIOPIC SYLLABLE PAA
    '\u1354': 'pe',   # ፔ ETHIOPIC SYLLABLE PEE
    '\u1355': 'pə',   # ፕ ETHIOPIC SYLLABLE PE (schwa)
    '\u1356': 'po',   # ፖ ETHIOPIC SYLLABLE PO
    # Labialized P
    '\u1357': 'pʷa',  # ፗ ETHIOPIC SYLLABLE PWA

    # === Vä === (v) (For foreign words, more common in Amharic)
    # This series is in the Ethiopic Supplement block U+1380–U+139F
    '\u1380': 'vä',   # ᎀ ETHIOPIC SYLLABLE VA
    '\u1381': 'vu',   # ᎁ ETHIOPIC SYLLABLE VU
    '\u1382': 'vi',   # ᎂ ETHIOPIC SYLLABLE VI
    '\u1383': 'va',   # ᎃ ETHIOPIC SYLLABLE VAA
    '\u1384': 've',   # ᎄ ETHIOPIC SYLLABLE VEE
    '\u1385': 'və',   # ᎅ ETHIOPIC SYLLABLE VE (schwa)
    '\u1386': 'vo',   # ᎆ ETHIOPIC SYLLABLE VO
    # Labialized V
    '\u1387': 'vʷa',  # ᎇ ETHIOPIC SYLLABLE VWA


    # === Ethiopic Punctuation and Digits ===
    '\u1360': '።',   # ። ETHIOPIC SECTION MARK (often like a full stop with extra flair)
    '\u1361': '፡',   # ፡ ETHIOPIC WORDSPACE (word separator)
    '\u1362': '።',   # ። ETHIOPIC FULL STOP (similar to section mark, usage varies)
    '\u1363': '፣',   # ፣ ETHIOPIC COMMA
    '\u1364': '፤',   # ፤ ETHIOPIC SEMICOLON
    '\u1365': '፥',   # ፥ ETHIOPIC COLON
    '\u1366': '፦',   # ፦ ETHIOPIC PREFACE COLON
    '\u1367': '፧',   # ፧ ETHIOPIC QUESTION MARK
    '\u1368': '፨',   # ፨ ETHIOPIC PARAGRAPH SEPARATOR

    # Digits
    '\u1369': '1',    # ፩ ETHIOPIC DIGIT ONE
    '\u136A': '2',    # ፪ ETHIOPIC DIGIT TWO
    '\u136B': '3',    # ፫ ETHIOPIC DIGIT THREE
    '\u136C': '4',    # ፬ ETHIOPIC DIGIT FOUR
    '\u136D': '5',    # ፭ ETHIOPIC DIGIT FIVE
    '\u136E': '6',    # ፮ ETHIOPIC DIGIT SIX
    '\u136F': '7',    # ፯ ETHIOPIC DIGIT SEVEN
    '\u1370': '8',    # ፰ ETHIOPIC DIGIT EIGHT
    '\u1371': '9',    # ፱ ETHIOPIC DIGIT NINE
    '\u1372': '10',   # ፲ ETHIOPIC NUMBER TEN
    '\u1373': '20',   # ፳ ETHIOPIC NUMBER TWENTY
    '\u1374': '30',   # ፴ ETHIOPIC NUMBER THIRTY
    '\u1375': '40',   # ፵ ETHIOPIC NUMBER FORTY
    '\u1376': '50',   # ፶ ETHIOPIC NUMBER FIFTY
    '\u1377': '60',   # ፷ ETHIOPIC NUMBER SIXTY
    '\u1378': '70',   # ፸ ETHIOPIC NUMBER SEVENTY
    '\u1379': '80',   # ፹ ETHIOPIC NUMBER EIGHTY
    '\u137A': '90',   # ፺ ETHIOPIC NUMBER NINETY
    '\u137B': '100',  # ፻ ETHIOPIC NUMBER HUNDRED
    '\u137C': '10000',# ፼ ETHIOPIC NUMBER TEN THOUSAND

    # Other symbols sometimes used
    '\u135A': '+GEM', # ፚ ETHIOPIC GEMINATION MARK (indicates consonant doubling)
    '\u135F': '+VM',  # ፟ ETHIOPIC COMBINING GEMINATION AND VOWEL LENGTH MARK
}