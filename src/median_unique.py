
''' This program calculates median number of unique words per tweet.
'''


import data_utils
import data_load
import word_count
import data_sort
import data_save
import sys
import profile

def process_tweets(tweet_list):
    ''' Gets unique words from tweet as they stream and calculates their median.
    In real world scenario, the tweets will come in as streams
    '''
    tweet_word_count_list = []
    median_list = []

    try:
        for tweet in tweet_list:
            '''Create a list of words for each tweet with
            white space as separator'''
            word_list = word_count.get_words_from_large_text(tweet)
            '''Remove duplicate words from the list'''
            unique_word_list = data_sort.merge_sort_remove_dup(word_list)

            tweet_word_count_list.append(len(unique_word_list))
            median_list.append(median(tweet_word_count_list))
    except ValueError as e:
            print 'Usage: Expected a list of tweets. Error {0}: {1}'.format(e.errno, e.strerror)
    except Exception as e:
            print 'An unexpected error occurred while processing tweets.'
            print e.message
    return median_list

def median(word_count):
    ''' Calculates median for a given list.
     For calculating median, word_count list is sorted using merge sort.
     Median is calculated by getting the middle value of the list.'''
    try:
        n = len(word_count)
        if n == 1:
            return word_count[0]
        '''Median formula for odd number of terms in list'''
        if n%2 == 1:
            mid = (n+1)/2
            sorted_list=data_sort.merge_sort(word_count)
            return sorted_list[--mid]
        else:
            '''Median formula for even number of terms in list'''
            mid_1 = (n)/2    #To get (n/2)th term
            mid_2 = n/2 + 1  #To get n/2 + 1 th term
            sorted_list=data_sort.merge_sort(word_count)
            return (sorted_list[mid_1-1] + sorted_list[mid_2-1])/2.
    except ValueError:
        print 'Expected a string list of unique words in a tweets'
    except Exception as e:
            print 'An unexpected error occurred while calculating median.'
            print e.message

def save(result, path):
    '''Converts list of integers in result to a string and writes it to file. '''
    output = '\n'.join(map(str,result))
    return data_save.write_to_text_file(output, path)


def main():
    if len(sys.argv) != 3:
        print 'Usage: median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt'
        sys.exit()

    ''' Read data from given file name as string'''
    tweet_list = data_load.read_all_lines(sys.argv[1])
    ''' Calculate median number for unique words '''
    median_list = process_tweets(tweet_list=tweet_list)

    '''Save median to a text file.'''
    save(result=median_list, path=sys.argv[2])


if __name__ == '__main__':
    print '-----median_unique.py----------'
    profile.run("main()")