def solution(s):
    newWord = ''
    for letter in s:
        if letter.islower() == True:
            newWord += letter
        else:
            newWord += ' '
            newWord += letter
    return newWord