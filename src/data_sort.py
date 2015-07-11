__author__ = 'DimpleSharma'

'''This file contains functions for two merge sort algorithms.
    First, classic merge sort which sorts a list in ascending order.
    Second, merge sort implemented to remove duplicates and sorts values in ascending order.
'''

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

def merge_sort_remove_dup(A):

    ''' Sorts elements of list A in ascending order of ASCII characters '''
    n = len(A)
    if n == 1:
        return A
    ''' Perform integer division using floor function,
    which maps a real number to largest previous integer '''
    mid = n//2
    L = merge_sort_remove_dup(A[:mid])
    R = merge_sort_remove_dup(A[mid:])

    return merge_remove_dup(L,R)

def merge_remove_dup(L, R):

    ''' Implements merge sort method to merge two sorted list - L and R - and remove duplicates,
    by combining sorting and remove duplicate operation'''
    i=0
    j=0
    sorted = []
    while i<len(L) and j<len(R):
        '''Perform remove duplicate operation.
        Verify whether two values are same and increment counters for both
         lists L and R respectively'''
        if L[i] == R[j]:
            sorted.append(L[i])
            i=i+1
            j=j+1
        else:
            '''Perform sorting operation '''
            ''' Compare values and append the smaller value to sorted list. '''
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

"""
def main():
    text = r.read_file('./tweet_input/tweets.txt')
    word_list = w.get_words_from_large_text(text)
    print w.calculate_word_count_dict(word_list)
    word_list_unique = merge_sort_remove_dup(word_list)
    print word_list_unique

if __name__ == '__main__':
    main()
"""