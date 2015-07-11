__author__ = 'DimpleSharma'


def get_words_from_large_text(text):
    '''
    Create a list of words from text
    Return a list of words.
    '''
    word_list = text.split()
    return word_list

def calculate_word_count(word_list):
    '''
    Return a list of tuple as (word, count) with frequency count of
    each word.
    '''
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return word_dict.items()
