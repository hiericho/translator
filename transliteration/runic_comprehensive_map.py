# ancient_translator/transliteration_maps/runic_comprehensive_map.py

SCRIPT_NAME = "runic_all" # Or just "runic" if it's the main one
DESCRIPTION = "Runic (Comprehensive - Elder, Anglo-Saxon, Younger)"
UNICODE_RANGE = ('16A0', '16FF') # General Runic block

# Maps Runic characters (keys) to their common Latin transliterations (values).
# This map attempts to cover major runes from Elder Futhark, Anglo-Saxon Futhorc,
# and Younger Futhark (long-branch).
# Transliterations like 'th', 'ng', 'ae', 'oe', 'ea' are used for better from-Latin input.
TO_LATIN_MAP = {
    # === Elder Futhark (EF) / Shared Runes ===
    '\u16A0': 'f',    # ᚠ FEHU (EF, AS, YF)
    '\u16A2': 'u',    # ᚢ URUZ (EF, AS, YF - also 'o' in YF sometimes)
    '\u16A6': 'th',   # ᚦ THURISAZ (EF, AS, YF - thorn)
    '\u16A8': 'a',    # ᚨ ANSUZ (EF, AS - 'a' or 'o') -> AS usually 'o' (see Os ᚩ)
                      # For YF, this shape is Áss/Óss (see ᚬ)
    '\u16B1': 'r',    # ᚱ RAIDHO (EF, AS, YF - Reid)
    '\u16B2': 'k',    # ᚲ KENAZ (EF, AS - Cen) / YF - Kaun (often 'k', sometimes 'g')
    '\u16B7': 'g',    # ᚷ GEBO (EF - Gyfu in AS, but AS uses a different 'g' sometimes)
    '\u16B9': 'w',    # ᚹ WUNJO (EF, AS - Wynn)

    '\u16BA': 'h',    # ᚺ HAGLAZ (EF, AS - Hægl) / YF - Hagall (long-branch)
    '\u16BC': 'n',    # ᚼ NAUDHIZ (EF, AS - Nyd) / YF - Nauð (long-branch)
    '\u16BE': 'i',    # ᛁ ISAZ (EF, AS - Is) / YF - Íss (long-branch)
    '\u16C1': 'j',    # ᛅ JERAN (EF - Jera, Ger in AS) / YF Ar (long-branch 'a', sometimes 'e')
                      # Note: YF Ar (ᛅ) is phonetically 'a' or 'æ'. EF Jera is 'j' or 'y'.
                      # This overlap is tricky. For YF 'a', ᛅ is common.
                      # Let's keep EF Jera as 'j'. See YF section for its 'a'.

    '\u16C7': 'eo',   # ᛇ EIHWAZ (EF - Eoh in AS) - also ï, æ, ihw. Using 'eo' for distinctness.
    '\u16C8': 'p',    # ᛈ PERTHO (EF, AS - Peorð)
    '\u16C9': 'z',    # ᛉ ALGIZ (EF - Eolh in AS) - also ʀ. (Not in YF)
    '\u16CB': 's',    # ᛋ SOWILO (EF, AS - Sigel) / YF - Sól (long-branch)

    '\u16CF': 't',    # ᛏ TIWAZ (EF, AS - Tir) / YF - Týr (long-branch)
    '\u16D2': 'b',    # ᛒ BERKANAN (EF, AS - Beorc) / YF - Bjarkan (long-branch)
    '\u16D6': 'e',    # ᛖ EHWAZ (EF, AS - Eh)
    '\u16D7': 'm',    # ᛗ MANNAZ (EF, AS - Mann) / YF - Maðr (long-branch)
    '\u16DA': 'l',    # ᛚ LAGUZ (EF, AS - Lagu) / YF - Lögr (long-branch)
    '\u16DD': 'ng',   # ᛝ INGWAZ (EF, AS - Ing)
    '\u16DE': 'd',    # ᛞ DAGAZ (EF, AS - Dæg)
    '\u16DF': 'o',    # ᛟ OTHALAN (EF, AS - Éðel/Œðel)

    # === Additional Anglo-Saxon Futhorc Runes ===
    '\u16A9': 'o_as', # ᚩ OS (AS 'o', distinct from EF Ansuz used as 'a') - using 'o_as' to disambiguate from EF Othalan
                      # Could also be just 'o' if EF Ansuz is strictly 'a' and EF Othalan is 'oe' or 'œ'
    '\u16AB': 'ae',   # ᚫ ÆSC (AS 'æ')
    '\u16AC': 'y',    # ᚬ YR (AS 'y') - Note: This shape is Óss/Áss in YF. This is a point of major confusion.
                      # Unicode U+16AC is RUNE YR. The Anglo-Saxon 'yr' rune.
    '\u16AD': 'io',   # ᚭ IOR (AS 'io', a diphthong)
    '\u16AE': 'ea',   # ᚮ EAR (AS 'ea', a diphthong)

    '\u16B0': 'c_as', # ᚰ CALC (AS 'c', often for 'k' sound, different from Cen)
    '\u16B3': 'q',    # ᚳ CWEN (AS 'cw' or 'q') - This is Cweorð. Cen is ᚲ for 'c/k'.
                      # For AS Cen (ᚳ): This is U+16B3, often transliterated 'c'.
                      # Your previous ᚲ was Cen for EF. Let's use ᚳ for AS Cen/'c'.
    # '\u16B2': 'k', # ᚲ KENAZ (EF, AS - Cen) - already listed
    '\u16B3': 'c',    # ᚳ RUNE CEN (AS 'c') - Distinct from EF Kenaz if 'k' is strictly used for ᚲ.
    '\u16B8': 'g_as', # ᚸ GAR (AS 'g', a specific 'g' sound, often a spear)
    '\u16BB': 'h_double', # ᚻ RUNE HAEGL H (double bar variant sometimes in AS) - maps to 'h'
    '\u16E1': 'st',   # ᛡ STAN (AS 'st' ligature)
    
    # Some Northumbrian runes (extensions to AS)
    '\u16B4': 'g_n',  # ᚴ RUNE GYFU G (Northumbrian G, different shape for 'g') -> This is Younger Futhark Kaun.
                      # Let's use a more distinct Northumbrian G if available or map existing Gar.
                      # Gar ᚸ is probably better for a special G.
    # '\u16E0': 'kk', # ᛠ RUNE EAR (Northumbrian variant for 'ea' or double 'k'?) - this is RUNE CALC.
    # Let's stick to the more common AS extensions for now.

    # === Younger Futhark (Long-Branch specific forms & transliterations) ===
    # Many YF runes share shapes with EF/AS but have different sounds or names.
    # The 16 YF runes are: f, u/o/y/w, th, o/a, r, k/g, h, n, i/e, a/æ, s, t/d, b/p, m, l.
    # Some Unicode points are reused or have specific YF names.

    # '\u16A0': 'f',    # ᚠ FÉ (YF) - already listed
    # '\u16A2': 'u',    # ᚢ ÚR (YF - u, o, y, w) - already listed
    # '\u16A6': 'th',   # ᚦ THURS (YF) - already listed
    '\u16AC': 'o_yf', # ᚬ ÓSS / ÁSS (YF - o, ø, nasal a) - This is RUNE YR in Unicode, used for AS YR.
                      # This is a major point of font/Unicode mapping issues.
                      # The typical YF Oss/Ass rune shape is ᚬ. We'll use 'o_yf' to distinguish.
    # '\u16B1': 'r',    # ᚱ REID (YF) - already listed
    '\u16B4': 'k_yf', # ᚴ KAUN (YF - k, g) - RUNE KAUN K. Can also be short-twig. (U+16B3 is AS Cen)
                      # Using 'k_yf' to distinguish if needed, but 'k' is often fine.
    # '\u16BA': 'h',    # ᚺ HAGALL (YF long-branch) - already listed
    # '\u16BC': 'n',    # ᚼ NAUÐ (YF long-branch) - already listed
    # '\u16BE': 'i',    # ᛁ ÍSS (YF long-branch - i, e) - already listed
    '\u16C1': 'a_yf', # ᛅ ÁR (YF long-branch - a, æ) - This is RUNE GER J in Unicode.
                      # EF Jera ᛅ is 'j'. YF Ar ᛅ is 'a'. This requires careful from-Latin handling.
                      # To disambiguate, we might need `j_ef` and `a_yf`.
                      # For simplicity, if user types 'j' it might map to ᛅ. If 'a_yf', also to ᛅ.
    # '\u16CB': 's',    # ᛋ SÓL (YF long-branch) - already listed
    # '\u16CF': 't',    # ᛏ TÝR (YF long-branch - t, d) - already listed
    # '\u16D2': 'b',    # ᛒ BJARKAN (YF long-branch - b, p) - already listed
    # '\u16D7': 'm',    # ᛗ MAÐR (YF long-branch) - already listed
    # '\u16DA': 'l',    # ᛚ LÖGR (YF long-branch) - already listed
    '\u16E6': 'R_yf', # ᛦ YR (YF - palatal R, often transcribed 'R' or 'ʀ') - This is RUNE LONG-BRANCH-YR R
                      # This is the specific YF 'yr' or 'R' sound, distinct from AS Yr ᚬ.

    # Short-twig Younger Futhark variants (some share codepoints, some are distinct)
    # Generally, transliteration is similar to long-branch. Adding a few distinct ones if commonly needed.
    # '\u16BD': 'n_st', # ᚽ NAUD N (short-twig variant for N) - if needed for specific rendering
    # '\u16BF': 'i_st', # ᚿ ISAZ IS ISS I (short-twig variant for I)
    # '\u16C2': 'a_st', # ᛂ JERAN JARA GĒR J (short-twig variant for A/Æ)
    # '\u16CC': 's_st', # ᛌ SOWILO SIGEL S (short-twig variant for S)

    # Punctuation (often used with runes)
    '\u16EB': ':',    # ᛫ RUNIC SINGLE PUNCTUATION (dot, often a separator)
    '\u16EC': '*',    # ᛬ RUNIC MULTIPLE PUNCTUATION (colon-like, complex separator)
    '\u16ED': '+',    # ᛭ RUNIC CROSS PUNCTUATION
}
# Note: The above map is a simplified version. The actual transliteration may depend on context.