# test = 'This is another test'
# spinWord = ''
# sentenceToList = list(test.split(' '))
# for word in sentenceToList:
#     if len(word) > 5:
#         reversedWord = word[::-1]
#         spinWord += " "
#         spinWord += reversedWord
#     else:
#         spinWord += " "
#         spinWord += word
# print(spinWord)
sentence = "This is a test sentence"
def spin_words(sentence):
    return " ".join([w[::-1] if len(w) >= 5 else w for w in sentence.split()])
