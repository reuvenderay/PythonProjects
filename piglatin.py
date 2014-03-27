
__author__ = "Reuven Deray"


def pig_word(original):
    """converts word into Pig Latin"""
    word = original.lower()
    if word[0] in "aeiou":
        new_word = word + 'ay'
    else:
        new_word = word[1:] + word[0] + 'ay'
    return new_word


def pig_sentence():
    """converts a word or sentence into Pig Latin"""
    sentence = raw_input("please enter a word or sentence")
    if len(sentence) > 0:
        return " ".join(pig_word(x) for x in sentence.split())
    else:
        return 'It looks like you entered nothing!'

print pig_sentence()


