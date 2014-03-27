
__author__ = "Reuven Deray"


def censor(text, word):
    """return text with word censored out

    returns string"""
    if text == '' or word == '':
        result = "Did you fill everything in?"
    else:
        result = ("*" * len(word)).join(text.split(word))
    return result

if __name__ == "__main__":
    my_text = raw_input("please enter the \
sentence you want censored:")
    my_word = raw_input('please enter the \
word or letter you want censored out (case sensitive)')
    f = open('C:\Users\Reuven\Desktop\slugs.txt', 'a')
    f.write('\n' + censor(my_text, my_word))
    f.close()