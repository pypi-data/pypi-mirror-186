import re

def FindAll(pattern:str, string:str, multiline=False) -> list[list[str]]:
    res = []

    pattern1 = ""
    lasti = ""
    for idx in range(len(pattern)):
        i = pattern[idx]
        pattern1 = pattern1 + i
        if i == "(" and lasti != "\\" and (pattern[idx+1] != "?" and pattern[idx+2] != ":"):
            pattern1 = pattern1 + "?:"
        lasti = i 

    if pattern != pattern1:
        if multiline:
            reres1 = re.findall(pattern1, string, re.MULTILINE)
            reres2 = re.findall(pattern, string, re.MULTILINE)
        else:
            reres1 = re.findall(pattern1, string)
            reres2 = re.findall(pattern, string)
            
        for idx in range(len(reres1)):
            r1 = reres1[idx]
            r2 = reres2[idx]

            if type(r1) == tuple and type(r2) == tuple:
                res.append(list(r1) + list(r2))
            elif type(r1) == tuple and type(r2) != tuple:
                t = list()
                t.append(r2)
                res.append(list(r1) + t)
            elif type(r1) != tuple and type(r2) == tuple:
                t = list()
                t.append(r1)
                res.append(t + list(r2))
            else:
                t = list()
                t.append(r1)
                t.append(r2)
                res.append(t)
    else:
        if multiline:
            reres = re.findall(pattern, string, re.MULTILINE)
        else:
            reres = re.findall(pattern, string)

        for i in reres:
            if type(i) == tuple:
                res.append(list(i))
            else:
                t = list()
                t.append(i)
                res.append(t)

    return res 

if __name__ == "__main__":
    print(FindAll("([a-z])([a-z])[0-9]+", "ac123bd456"))    # ==> [['ac123', 'a', 'c'], ['bd456', 'b', 'd']]
    print(FindAll("([a-z])[0-9]+", "c123d456"))             # ==> [['c123', 'c'], ['d456', 'd']]
    print(FindAll("[a-z][0-9]+", "c123d456"))               # ==> [['c123'], ['d456']]
    print(FindAll("(\\()[a-z][0-9]+", "(c123d456"))         # ==> [['(c123', '(']]
    print(FindAll("(?:[a-z])[0-9]+", "c123d456"))           # ==> [['c123'], ['d456']]
    print(FindAll("(111|222)-def", "111-def"))              # ==> [['111-def', '111']]
    print(FindAll("(111|222)-def", "222-def"))              # ==> [['222-def', '222']]