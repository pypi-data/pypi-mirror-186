import jieba 

try:
    from .. import Re
    from .. import String
    from .CutSentenceStopWords import stopwords
except:
    import sys 
    sys.path.append("..")
    import Re
    import String
    from CutSentenceStopWords import stopwords

def __make_words(s:str) -> list[str]:
        ss = []
        last = ""
        for i in s:
            if last == " " and i == " ":
                continue 

            if String(i).HasChinese() or Re.FindAll("[0-9a-zA-Z]", i) or i == " ":
                ss.append(i)

                last = i 

        sss = []
        for i in jieba.cut(''.join(ss), cut_all=False):
            if len(i) == 1:
                continue 

            if i in stopwords:
                continue

            sss.append(i)
        
        return sss

def CutSentence(sentence:str, filter:bool=True) -> list[str]:
    if filter:
        return __make_words(sentence)
    else:
        return jieba.cut(sentence, cut_all=False)

