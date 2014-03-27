
__author__ = "Reuven Deray"

class PigLatin:
    def __init__(self):
        pass
    def pig_word(self, original):
        """converts word into Pig Latin"""
        word = original.lower()
        if word[0] in "aeiou":
            new_word = word + 'ay'
        else:
            new_word = word[1:] + word[0] + 'ay'
        return new_word

    def pig_sentence(self, sentence):
        """converts a word or sentence into Pig Latin"""
        if len(sentence) > 0:
            result = " ".join(self.pig_word(x) for x in sentence.split())
            return result
        else:
            return 'It looks like you entered nothing!'

def get_input():
    u_input = raw_input("please enter a word or sentence")
    f = PigLatin()
    return f.pig_sentence(u_input)

get_input()


