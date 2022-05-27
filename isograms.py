def is_isogram(string):
    string = string.lower()
    if not string:
        return True
    else:
        return len(string) == len(set(string.lower()))