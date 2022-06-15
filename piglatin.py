def pig_it(text):
    #split string based on spaces
    split_text = text.split(' ')
    new_sentence = ' '
    for word in split_text:
        if word in '!.%&?':
            new_sentence = new_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            new_sentence = new_sentence + pig_word + ' '
    return new_sentence.strip(' ') 