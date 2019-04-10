#-*- encoding:utf-8 -*-
#from __future__ import print_function
from ckippy import parse_tree
import re
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
1
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

dialog_sentence_delimiters = ['\n', '」']
def get_dialog(text):
    tr4s = TextRank4Sentence(delimiters=dialog_sentence_delimiters)
    tr4s.analyze(text=text, lower=True, source='all_filters')

    #print(tr4s.sentences)
    #for s in tr4s.sentences:
    #    print(s)

    sentences = [s for s in tr4s.sentences if '「' in s]

    dialog = [s.split('「') for s in sentences]

    speak = [s[1] for s in dialog]

    final_speak = []

    for i in range(len(speak)-1):
        if speak[i][-1] == '，':
            final_speak.append(speak[i]+speak[i+1])
            i += 1
        else:
            final_speak.append(speak[i])
    return final_speak

#text = codecs.open('小紅帽.txt', 'r', 'utf-8').read()
#print(get_dialog(text))