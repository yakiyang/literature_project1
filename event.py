#-*- encoding:utf-8 -*-
from __future__ import print_function
from ckippy import parse_tree
from pyhanlp import *
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

N_type = ['Na','Nb','Nc']
V_type = ['VA', 'VB', 'VC', 'VH', 'VL', 'VK', 'VE', 'VJ']
O_type = ['Head:P', 'Dba', 'Dc', 'Ta']


tr4s = TextRank4Sentence()

index_list = []
sentence_list = []
parse_list = []
events = []

def get_index(s):
    N_index = []
    V_index = []
    O_index = []
    index = []
    for t in N_type:
        N_index += [m.start() for m in re.finditer(t, s)]
    for t in V_type:
        V_index += [m.start() for m in re.finditer(t, s)]
    for t in O_type:
        O_index += [m.start() for m in re.finditer(t, s)]

    if len(V_index)!=0 and len(N_index)!=0:
        index = N_index + V_index + O_index

    return index

def get_event(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')

    for item in tr4s.get_key_sentences(num=len(tr4s.sentences)/2):
        if '說' not in item.sentence:
            index_list.append(item.index)
        #print(item.index, item.weight, item.sentence)
    index_list.sort()

    for i in index_list:
        #print(tr4w.sentences[i])
        sentence_list.append(tr4s.sentences[i])


    for i in index_list:
        s = tr4s.sentences[i]
        p = parse_tree(s)
        tmp_list = []
        for i in range(len(p)):
            if p[i][6] != 'N':
                tmp_list.append((p[i], s))
        parse_list.append(tmp_list)


    for list in parse_list:
        for s in list:
            index = get_index(s[0])
            index.sort()
            event = ''
            for i in index:
                for j in range(i, len(s[0])):
                    if s[0][j] == ':':
                        start = j+1
                    if s[0][j] == '|' or s[0][j] == ')':
                        end = j
                        break

                if s[0][start:end] != '說':
                    event += s[0][start:end]
            if len(event) != 0:
                events.append(event)

    return events

