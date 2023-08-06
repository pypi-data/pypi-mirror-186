import json

def Dumps(obj, indent=4, ensure_ascii=False) -> str:
    """
    It takes a Python object and returns a JSON string
    
    :param obj: The object to be serialized
    :param indent: This is the number of spaces to indent for each level. If it is None, that
    will insert newlines but won't indent the new lines, defaults to 4 (optional)
    :param ensure_ascii: If True, all non-ASCII characters in the output are escaped with \\uXXXX
    sequences, and the result is a str instance consisting of ASCII characters only. If False, some
    chunks written to fp may be unicode instances. This usually happens because the input contains
    unicode strings or the, defaults to False (optional)
    :return: A string
    """
    return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii)

def Loads(s:str) -> list | dict:
    return json.loads(s)

def ExtraValueByKey(obj:list|dict, key:str) -> list:
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
                    
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

if __name__ == "__main__":
    j = Dumps({1: 3, 4: 5})
    print(j)

    d = Loads(j)
    print(d)

    print(type(d))