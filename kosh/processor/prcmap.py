#!/usr/bin/env python3

class PrcMap():
    def __init__():
        pass

    def getPreRex():
        rexary = [
                [r'ट न ् ]',r'ट्ने'],
                [r'ट न ्',r'ट्न'],
                [r'सा ्रे',r'स्रो'],
                [r'क््र',r'क्र'],
                [r' डँी',r'ँडी'],
                [r'। ञ् ',r'।  ~'],
                [r'थ न ु',r'थुन'],
                [r' ́',r'झ'],
                [r'\nअस््ज्ञकबचयव्क्बदमपयकज्ऋजजब।उटछ\n.*[\n][णज्ञईघद्धछटठडढ]+\n',r' '],
                [r'\n+अस््ज्ञकबचयव्क्बदमपयकज्ऋजजब।उटछ\n[णज्ञईघद्धछटठडढ]+\n',r' '],
                #[r'\n',' '],
                [r'¦',r'ु'],
                [r'ु दँा',r'ुँदा'],
                #[r'',r''],
                [r'”',r'ँ'], #font bug
                
                #आकार इकार उकार च्न्द्रविन्दु आदिको अघिल्तिर स्पेस आउन सक्दैन, आयो भने हटाइदिने
                [r'[\ ]+([ँीाीुूेैोौ])',r'\1'],
                [r' डँी',r'ँडी'], #individual bug
                [r'त्रि०',r'क्रि०'], #individual bug
                
                #चन्द्रविन्दु र सिरिविन्दुलाई यूनिकोडमा टाइप गर्दा आकार इकार उकार को पछाडी राख्नु पर्छ
                [r'([ँं])([ािीुूेैोौ])',r'\2\1'], 
                
        ]
        return rexary
