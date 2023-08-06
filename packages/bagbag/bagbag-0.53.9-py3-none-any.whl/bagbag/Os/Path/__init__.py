import os

def Basedir(path:str) -> str:
    return os.path.dirname(path)

def Join(*path) -> str:
    return os.path.join(*path)

def Exists(path:str) -> bool:
    return os.path.exists(path)

def NotExists(path:str) -> bool:
    return not os.path.exists(path)

def Uniquify(path:str) -> str:
    """
    If the file exists, add a number to the end of the file name until it doesn't exist
    
    :param path: The path to the file you want to uniquify
    :type path: str
    :return: The path of the file with a number appended to the end of the file name.
    """
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "." + str(counter) + extension
        counter += 1

    return path

def IsDir(path:str) -> bool:
    return os.path.isdir(path)

def Basename(path:str) -> str:
    return os.path.basename(path)

def Suffix(path:str) -> str:
    return os.path.splitext(path)[1]

if __name__ == "__main__":
    print(Join("a", "b"))