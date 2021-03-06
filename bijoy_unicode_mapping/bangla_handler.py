"# -*- coding: utf-8 -*-"

import re

def translate(txt):
    
    # txt = txt.replace("৷","|")
    # txt = txt.replace("।","|")
    # txt = txt.replace("‘", "Ô")
    # txt = txt.replace("a", 61952)
    # txt = txt.replace("A", 61952)
    # txt = txt.replace("b", 61953)
    # txt = txt.replace("B", 61953)
    # txt = txt.replace("c", 61954)
    # txt = txt.replace("C", 61954)
    # txt = txt.replace("d", 61955)
    # txt = txt.replace("D", 61955)
    # txt = txt.replace("e", 61956)
    # txt = txt.replace("E", 61956)
    # txt = txt.replace("f", 61957)
    # txt = txt.replace("F", 61957)
    # txt = txt.replace("g", 61958)
    # txt = txt.replace("G", 61958)
    # txt = txt.replace("h", 61959)
    # txt = txt.replace("H", 61959)
    # txt = txt.replace("i", 61960)
    # txt = txt.replace("I", 61960)
    # txt = txt.replace("j", 61961)
    # txt = txt.replace("J", 61961)
    # txt = txt.replace("k", 61962)
    # txt = txt.replace("K", 61962)
    # txt = txt.replace("l", 61963)
    # txt = txt.replace("L", 61963)
    # txt = txt.replace("m", 61964)
    # txt = txt.replace("M", 61964)
    # txt = txt.replace("n", 61965)
    # txt = txt.replace("N", 61965)
    # txt = txt.replace("o", 61966)
    # txt = txt.replace("O", 61966)
    # txt = txt.replace("p", 61967)
    # txt = txt.replace("P", 61967)
    # txt = txt.replace("q", 61968)
    # txt = txt.replace("Q", 61968)
    # txt = txt.replace("r", 61969)
    # txt = txt.replace("R", 61969)
    # txt = txt.replace("s", 61970)
    # txt = txt.replace("S", 61970)
    # txt = txt.replace("t", 61971)
    # txt = txt.replace("T", 61971)
    # txt = txt.replace("u", 61972)
    # txt = txt.replace("U", 61972)
    # txt = txt.replace("v", 61973)
    # txt = txt.replace("V", 61973)
    # txt = txt.replace("w", 61974)
    # txt = txt.replace("W", 61974)
    # txt = txt.replace("x", 61975)
    # txt = txt.replace("X", 61975)
    # txt = txt.replace("y", 61976)
    # txt = txt.replace("Y", 61976)
    # txt = txt.replace("z", 61977)
    txt = txt.replace("৷", "|")
    txt = txt.replace("।", "|")
    txt = txt.replace("‘", "Ô")
    txt = txt.replace("’", "Õ")
    txt = txt.replace("“", "Ò")
    txt = txt.replace("”", "Ó")
    txt = txt.replace("্র্য", "ª¨")
    txt = txt.replace("ম্প্র", "¤cÖ")
    txt = txt.replace("র‌্য", "i¨")
    txt = txt.replace("ক্ষ্ম", "²")
    txt = txt.replace("ক্ক", "°")
    txt = txt.replace("ক্ট", "±")
    txt = txt.replace("ক্ত", "³")
    txt = txt.replace("ক্ব", "K¡")
    txt = txt.replace("স্ক্র", "¯Œ")
    txt = txt.replace("ক্র", "µ")
    txt = txt.replace("ক্ল", "K¬")
    txt = txt.replace("ক্ষ", "¶")
    txt = txt.replace("ক্স", "·")
    txt = txt.replace("গু", "¸")
    txt = txt.replace("গ্ধ", "»")
    txt = txt.replace("গ্ন", "Mœ")
    txt = txt.replace("গ্ম", "M¥")
    txt = txt.replace("গ্ল", "M­")
    txt = txt.replace("গ্রু", "Mªy")
    txt = txt.replace("ঙ্ক", "¼")
    txt = txt.replace("ঙ্ক্ষ", "•¶")
    txt = txt.replace("ঙ্খ", "•L")
    txt = txt.replace("ঙ্গ", "½")
    txt = txt.replace("ঙ্ঘ", "•N")
    txt = txt.replace("চ্ছ্ব", "”Q¡")
    txt = txt.replace("চ্চ", "”P")
    txt = txt.replace("চ্ছ", "”Q")
    txt = txt.replace("চ্ঞ", "”T")
    txt = txt.replace("জ্জ্ব", "¾¡")
    txt = txt.replace("জ্জ", "¾")
    txt = txt.replace("জ্ঝ", "À")
    txt = txt.replace("জ্ঞ", "Á")
    txt = txt.replace("জ্ব", "R¡")
    txt = txt.replace("ঞ্চ", "Â")
    txt = txt.replace("ঞ্ছ", "Ã")
    txt = txt.replace("ঞ্জ", "Ä")
    txt = txt.replace("ঞ্ঝ", "Å")
    txt = txt.replace("ট্ট", "Æ")
    txt = txt.replace("ট্ব", "U¡")
    txt = txt.replace("ট্ম", "U¥")
    txt = txt.replace("ড্ড", "Ç")
    txt = txt.replace("ণ্ট", "È")
    txt = txt.replace("ণ্ঠ", "É")
    txt = txt.replace("ন্স", "Ý")
    txt = txt.replace("ণ্ড", "Ê")
    txt = txt.replace("ন্তু", "š‘")
    txt = txt.replace("ণ্ব", "Y^")
    txt = txt.replace("ত্ত্ব", "Ë¡")
    txt = txt.replace("ত্ত", "Ë")
    txt = txt.replace("ত্থ", "Ì")
    txt = txt.replace("ত্ন", "Zœ")
    txt = txt.replace("ত্ম", "Z¥")
    txt = txt.replace("ন্ত্ব", "š—¡")
    txt = txt.replace("ত্ব", "Z¡")
    txt = txt.replace("থ্ব", "_¡")
    txt = txt.replace("দ্গ", "˜M")
    txt = txt.replace("দ্ঘ", "˜N")
    txt = txt.replace("দ্দ", "Ï")
    txt = txt.replace("দ্ধ", "×")
    txt = txt.replace("দ্ব", "˜¡")
    txt = txt.replace("দ্ব", "Ø")
    txt = txt.replace("দ্ভ", "™¢")
    txt = txt.replace("দ্ম", "Ù")
    txt = txt.replace("দ্রু", "`ª“")
    txt = txt.replace("ধ্ব", "aŸ")
    txt = txt.replace("ধ্ম", "a¥")
    txt = txt.replace("ন্ট", "›U")
    txt = txt.replace("ন্ঠ", "Ú")
    txt = txt.replace("ন্ড", "Û")
    txt = txt.replace("ন্ত্র", "š¿")
    txt = txt.replace("ন্ত", "š—")
    txt = txt.replace("স্ত্র", "¯¿")
    txt = txt.replace("ত্র", "Î")
    txt = txt.replace("ন্থ", "š’")
    txt = txt.replace("ন্দ", "›`")
    txt = txt.replace("ন্দ্ব", "›Ø")
    txt = txt.replace("ন্ধ", "Ü")
    txt = txt.replace("ন্ন", "bœ")
    txt = txt.replace("ন্ব", "š^")
    txt = txt.replace("ন্ম", "b¥")
    txt = txt.replace("প্ট", "Þ")
    txt = txt.replace("প্ত", "ß")
    txt = txt.replace("প্ন", "cœ")
    txt = txt.replace("প্প", "à")
    txt = txt.replace("প্ল", "c­")
    txt = txt.replace("প্স", "á")
    txt = txt.replace("ফ্ল", "d¬")
    txt = txt.replace("ব্জ", "â")
    txt = txt.replace("ব্দ", "ã")
    txt = txt.replace("ব্ধ", "ä")
    txt = txt.replace("ব্ব", "eŸ")
    txt = txt.replace("ব্ল", "e¬")
    txt = txt.replace("ভ্র", "å")
    txt = txt.replace("ম্ন", "gœ")
    txt = txt.replace("ম্প", "¤ú")
    txt = txt.replace("ম্ফ", "ç")
    txt = txt.replace("ম্ব", "¤^")
    txt = txt.replace("ম্ভ", "¤¢")
    txt = txt.replace("ম্ভ্র", "¤£")
    txt = txt.replace("ম্ম", "¤§")
    txt = txt.replace("ম্ল", "¤­")
    txt = txt.replace("্র", "ª")
    txt = txt.replace("রু", "i“")
    txt = txt.replace("রূ", "iƒ")
    txt = txt.replace("ল্ক", "é")
    txt = txt.replace("ল্গ", "ê")
    txt = txt.replace("ল্ট", "ë")
    txt = txt.replace("ল্ড", "ì")
    txt = txt.replace("ল্প", "í")
    txt = txt.replace("ল্ফ", "î")
    txt = txt.replace("ল্ব", "j¦")
    txt = txt.replace("ল্ম", "j¥")
    txt = txt.replace("ল্ল", "j­")
    txt = txt.replace("শু", "ï")
    txt = txt.replace("শ্চ", "ð")
    txt = txt.replace("শ্ন", "kœ")
    txt = txt.replace("শ্ব", "k¦")
    txt = txt.replace("শ্ম", "k¥")
    txt = txt.replace("শ্ল", "k­")
    txt = txt.replace("ষ্ক", "®‹")
    txt = txt.replace("ষ্ক্র", "®Œ")
    txt = txt.replace("ষ্ট", "ó")
    txt = txt.replace("ষ্ঠ", "ô")
    txt = txt.replace("ষ্ণ", "ò")
    txt = txt.replace("ষ্প", "®ú")
    txt = txt.replace("ষ্ফ", "õ")
    txt = txt.replace("ষ্ম", "®§")
    txt = txt.replace("স্ক", "¯‹")
    txt = txt.replace("স্ট", "÷")
    txt = txt.replace("স্খ", "ö")
    txt = txt.replace("স্ত", "¯—")
    txt = txt.replace("স্তু", "¯‘")
    txt = txt.replace("স্থ", "¯’")
    txt = txt.replace("স্ন", "mœ")
    txt = txt.replace("স্প", "¯ú")
    txt = txt.replace("স্ফ", "ù")
    txt = txt.replace("স্ব", "¯^")
    txt = txt.replace("স্ম", "¯§")
    txt = txt.replace("স্ল", "¯­")
    txt = txt.replace("হু", "û")
    txt = txt.replace("হ্ণ", "nè")
    txt = txt.replace("হ্ব", "nŸ")
    txt = txt.replace("হ্ন", "ý")
    txt = txt.replace("হ্ম", "þ")
    txt = txt.replace("হ্ল", "n¬")
    txt = txt.replace("হৃ", "ü")
    txt = txt.replace("র্", "©")
    txt = txt.replace("্র", "«")
    txt = txt.replace("্য", "¨")
    txt = txt.replace("্", "&")
    txt = txt.replace("আ", "Av")
    txt = txt.replace("অ", "A")
    txt = txt.replace("ই", "B")
    txt = txt.replace("ঈ", "C")
    txt = txt.replace("উ", "D")
    txt = txt.replace("ঊ", "E")
    txt = txt.replace("ঋ", "F")
    txt = txt.replace("এ", "G")
    txt = txt.replace("ঐ", "H")
    txt = txt.replace("ও", "I")
    txt = txt.replace("ঔ", "J")
    txt = txt.replace("ক", "K")
    txt = txt.replace("খ", "L")
    txt = txt.replace("গ", "M")
    txt = txt.replace("ঘ", "N")
    txt = txt.replace("ঙ", "O")
    txt = txt.replace("চ", "P")
    txt = txt.replace("ছ", "Q")
    txt = txt.replace("জ", "R")
    txt = txt.replace("ঝ", "S")
    txt = txt.replace("ঞ", "T")
    txt = txt.replace("ট", "U")
    txt = txt.replace("ঠ", "V")
    txt = txt.replace("ড", "W")
    txt = txt.replace("ঢ", "X")
    txt = txt.replace("ণ", "Y")
    txt = txt.replace("ত", "Z")
    txt = txt.replace("থ", "_")
    txt = txt.replace("দ", "`")
    txt = txt.replace("ধ", "a")
    txt = txt.replace("ন", "b")
    txt = txt.replace("প", "c")
    txt = txt.replace("ফ", "d")
    txt = txt.replace("ব", "e")
    txt = txt.replace("ভ", "f")
    txt = txt.replace("ম", "g")
    txt = txt.replace("য", "h")
    txt = txt.replace("র", "i")
    txt = txt.replace("ল", "j")
    txt = txt.replace("শ", "k")
    txt = txt.replace("ষ", "l")
    txt = txt.replace("স", "m")
    txt = txt.replace("হ", "n")
    txt = txt.replace("ড়", "o")
    txt = txt.replace("ঢ়", "p")
    txt = txt.replace("য়", "q")
    txt = txt.replace("ৎ", "r")
    txt = txt.replace("০", "0")
    txt = txt.replace("১", "1")
    txt = txt.replace("২", "2")
    txt = txt.replace("৩", "3")
    txt = txt.replace("৪", "4")
    txt = txt.replace("৫", "5")
    txt = txt.replace("৬", "6")
    txt = txt.replace("৭", "7")
    txt = txt.replace("৮", "8")
    txt = txt.replace("৯", "9")
    txt = txt.replace("া", "v")
    txt = txt.replace("ি", "w")
    txt = txt.replace("ী", "x")
    txt = txt.replace("ু", "y")
    txt = txt.replace("ূ", "~")
    txt = txt.replace("ৃ", "…")
    txt = txt.replace("ে", "‡")
    txt = txt.replace("ৈ", "‰")
    txt = txt.replace("ৗ", "Š")
    txt = txt.replace("ং", "s")
    txt = txt.replace("ঃ", "t")
    txt = txt.replace("ঁ", "u")
    txt = txt.replace("ো", "ো").replace("ৌ", "ৌ")

    return txt