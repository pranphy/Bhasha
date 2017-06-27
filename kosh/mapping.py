#!/usr/bin/env python3

class Mapping():
    def __init__():
        pass

    def getMapping():
        mapdict = {"÷": "/", "v": "ख", "r": "च", "\"": "ू", "~": "ञ्", "z": "श", "ç": "ॐ", "f": "ा", "b": "द", "n": "ल", "j": "व", "×": "×", "V": "ख्", "R": "च्", "ß": "द्म", "^": "६", "Û": "!", "Z": "श्", "F": "ँ", "B": "द्य", "N": "ल्", "Ë": "ङ्ग", "J": "व्", "6": "ट", "2": "द्द", "¿": "रू", ">": "श्र", ":": "स्", "§": "ट्ट", "&": "७", "£": "घ्", "•": "ड्ड", ".": "।", "«": "्र", "*": "८", "„": "ध्र", "w": "ध", "s": "क", "g": "न", "æ": "“", "c": "अ", "o": "य", "k": "प", "W": "ध्", "Ö": "=", "S": "क्", "Ò": "¨", "_": ")", "[": "ृ", "Ú": "’", "G": "न्", "ˆ": "फ्", "C": "ऋ", "O": "इ", "Î": "ङ्ख", "K": "प्", "7": "ठ", "¶": "ठ्ठ", "3": "घ", "9": "ढ", "?": "रु", ";": "स", "'": "ु", "#": "३", "¢": "द्घ", "/": "र", "+": "ं", "ª": "ङ", "t": "त", "p": "उ", "|": "्र", "x": "ह", "å": "द्व", "d": "म", "`": "ञ", "l": "ि", "h": "ज", "T": "त्", "P": "ए", "Ý": "ट्ठ", "\\": "्", "Ù": ";", "X": "ह्", "Å": "हृ", "D": "म्", "@": "२", "Í": "ङ्क", "L": "ी", "H": "ज्", "4": "द्ध", "«": "+", "0": "ण्", "<": "?", "8": "ड", "¥": "र्‍", "$": "४", "¡": "ज्ञ्", ",": ",", "©": "र", "(": "९", "‘": "ॅ", "u": "ग", "q": "त्र", "}": "ै", "y": "थ", "e": "भ", "a": "ब", "i": "ष्", "‰": "झ्", "U": "ग्", "Q": "त्त", "]": "े", "˜": "ऽ", "Y": "थ्", "Ø": "्य", "E": "भ्", "A": "ब्", "M": "ः", "Ì": "न्न", "I": "क्ष्", "5": "छ", "´": "झ", "1": "ज्ञ", "°": "ङ्ढ", "=": ".", "Æ": "”", "‹": "ङ्घ", "%": "५", "¤": "झ्", "!": "१", "-": "(", "›": "द्र", ")": "०", "…": "‘", "Ü": "%","œ":"त्र्","́":"झ"}
        return mapdict
    
    def getExtraMap():
        mapdict = {'®':'र','“':'ँ'}
        return mapdict
    
    def getPreRex():
        rexary = [
            [r'l[ ]+','l'],[r'[\n ]+{',r'{'],
            [r' \] ',r'Σ'],
            [' \[ ',r'ί']
        ]
        
        return rexary
    
    def getRexArray():
        #
        rexary =[
        [r"्ा", r""], [r"(त्र|त्त)([^उभप]+?)m", r"\1m\2"], [r"त्रm", r"क्र"], [r"त्तm", r"क्त"], [r"([^उभप]+?)m", r"m\1"], [r"उm", r"ऊ"], [r"भm", r"झ"], [r"पm", r"फ"], [r"इ{", r"ई"], [r"ि((.्)*[^्])", r"\1ि"], [r"(.[ािीुूृेैोौंःँ]*?){", r"{\1"], [r"((.्)*){", r"{\1"], [r"{", r"र्"], [r"([ाीुूृेैोौंःँ]+?)(्(.्)*[^्])", r"\2\1"], [r"्([ाीुूृेैोौंःँ]+?)((.्)*[^्])", r"्\2\1"], [r"([ंँ])([ािीुूृेैोौः]*)", r"\2\1"], [r"ँँ", r"ँ"], [r"ंं", r"ं"], [r"ेे", r"े"], [r"ैै", r"ै"], [r"ुु", r"ु"], [r"ूू", r"ू"], [r"^ः", r":"], [r"टृ", r"ट्ट"], [r"ेा", r"ाे"], [r"ैा", r"ाै"], [r"अाे", r"ओ"], [r"अाै", r"औ"], [r"अा", r"आ"], [r"एे", r"ऐ"], [r"ाे", r"ो"], [r"ाै", r"ौ"],[r'[\n ]+ो',r'ो'],[r'[\n ]+([ेौौाःँृं])',r'\1'],
        [r'Σ',r' ] '],
        [r'ί',' [ '],[r'०ृ',r'० ['],[r'¦ँ',r'ुँ']
        ]
        return rexary
        

