import codecs
import json
from collections import defaultdict, OrderedDict
import jieba
import jieba.posseg as pseg
import event
import dialog

def jieba_parse(text):
    original_sentense = text
    jieba.load_userdict('dict.txt')
    words = jieba.cut(original_sentense, cut_all=False)
    return_word=''
    for w in words:
        return_word = return_word+','+w
    return return_word

if __name__ == '__main__':
    text = codecs.open('白雪公主.txt', 'r', 'utf-8').read()
    text = text.replace("\r\n","").replace("\n","").strip().replace('．','')
    text_preview = '%.70s...' % text

    print('text_preview:')
    print(text_preview)
    parsing = jieba_parse(text)
    # print(parsing)

    nr = []  # characters
    ns = []  # locations
    t = []  # time

    word = pseg.cut(text)

    for w in word:
        if w.flag in ["nr"]:
            # print(w.word, w.flag)
            nr.append(str(w.word))
        if w.flag in ["ns"]:
            # print(w.word, w.flag)
            ns.append(str(w.word))
        if w.flag in ["t"]:
            # print(w.word, w.flag)
            t.append(str(w.word))
    nr = list(set(nr))
    ns = list(set(ns))
    t = list(set(t))

    print('characters: ')
    for c in nr:
        print(c)
    print('locations:')
    for c in ns:
        print(c)
    print('time:')
    for c in t:
        print(c)

    print('characters: ', nr)
    print('locations: ', ns)
    print('time: ', t)

    dialogs = dialog.get_dialog(text)
    print('dialogues:')
    for c in dialogs:
        print(c)

    print('dialogues:', dialogs)

    events = event.get_event(text)
    print('events:')
    for c in events:
        print(c)

    print(events)

    story_dict = {
        "title": "白雪公主",
        "contents": {
            "summarize":text,
            "characters": nr,
            "locations": ns,
            "time": t,
            "dialogue": dialogs,
            "events": events
        }
    }

    json_str = json.dumps(story_dict, indent=4, ensure_ascii=False)
    with open('白雪公主_output.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)
