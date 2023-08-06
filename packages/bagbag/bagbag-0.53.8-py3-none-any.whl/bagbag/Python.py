from typing import Iterable

def Range(startOrEnd:int, end:int=None) -> Iterable:
    """
    If the second argument is provided, return a range from the first argument to the second argument,
    otherwise return a range from 0 to the first argument.
    If the second argument is smaller than the first argument, the range will be reverse.
    
    :param startOrEnd: The first number in the range. If end is not specified, this is the last number
    in the range
    :type startOrEnd: int
    :param end: The end of the range
    :type end: int
    :return: A range object
    """
    if end != None:
        if startOrEnd > end:
            return range(startOrEnd, end, -1)
        else:
            # print(startOrEnd, end, -1)
            return range(startOrEnd, end)
    else:
        return range(0, startOrEnd)

if __name__ == "__main__":
    print([i for i in Range(10)])
    print([i for i in Range(20, 30)])
    print([i for i in Range(30, 25)])

