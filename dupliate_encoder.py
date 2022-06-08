
# Testing
# word = 'din'

def duplicate_encode(word):
    word = word.lower()
    nstring = ''
    for i in word:
        if word.count(i) > 1:
            nstring += ')'
        else:
            nstring += '('
    return nstring