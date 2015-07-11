# example of program that calculates the total number of times each word has been tweeted.

'''
This program computes word frequency of tweets in
a text file.

For a given input text file, perform following operations:
    1. Read lines of text from input text file
    2. Split words on whole document using white space to split
    3. Count frequency of words in a dictionary with word
       as key and count as value.
    4. Sort word count list by ASCII code using merge sort

'''

import sys
import profile
import os
import data_utils
import data_save
import data_load


def get_words_from_large_text(text):
    '''
    Create a list of words from text
    Return a list of words.
    '''
    try:
        if text:
            word_list = text.split()
            return word_list
    except Exception as e:
        print 'An unexpected error occured'
        print e.message

def calculate_word_count(word_list):
    '''
    Return a list of tuple as (word, count) with frequency count of
    each word.
    '''
    word_dict = {}
    try:
        for word in word_list:
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
        return word_dict.items()
    except Exception as e:
        print 'An unexpected error occured'
        print e.message

def merge_sort(A):

    ''' Sorts elements of list A in ascending order of ASCII characters '''
    n = len(A)
    if n == 1:
        return A
    ''' Perform integer division using floor function,
    which maps a real number to largest previous integer '''
    mid = n//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])

    return merge(L,R)

def merge(L, R):

    ''' Merges two sorted lists, L and R, into a single sorted list '''
    i=0
    j=0
    sorted = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            sorted.append(L[i])
            i=i+1
        else:
            sorted.append(R[j])
            j=j+1
    ''' Append any remaining elements in list L to the sorted list '''
    if i<len(L):
        sorted.extend(L[i:])

    ''' Append any remaining elements in list R to the sorted list '''
    if j<len(R):
        sorted.extend(R[j:])
    return sorted

def save(result, path):
    '''Format text output in result list to a string and writes it to file. '''
    output='\n'.join(['%-25s %-10s'%s for s in result])
    return data_save.write_to_text_file(output, path)

def main():
    if(len(sys.argv) != 3):
        print 'Usage: words_tweeted.py input_filename output_filename'
        sys.exit()

    ''' Read data from given file name as string'''
    text = data_load.read_file(sys.argv[1])

    '''Using the string, create a list of words with
    white space as separator'''
    word_list = get_words_from_large_text(text)

    ''' Calculate word frequency for each word and store it as
     key value pair of word and counts in a dictionary'''
    word_count = calculate_word_count(word_list)

    '''Sort list of word and count in ascending order of words
     in ascii characters'''
    word_count = merge_sort(word_count)

    '''Save dictionary output in a file '''
    save(word_count,sys.argv[2])

    #print 'Successfully create a list of word counts for tweets'


if __name__ == '__main__':
    profile.run("main()")
