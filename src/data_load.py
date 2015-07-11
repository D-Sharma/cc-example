__author__ = 'DimpleSharma'

''' This file contains functions to read data from file. '''

import data_utils
import sys

def read_file(input_file):
    '''
    Read a text file with filename as input_file.
    Return contents of file as string.
    '''
    try:
        if(data_utils.file_exist(input_file)):
            '''Sets current working directory to directory of
             input_file'''
            data_utils.set_working_dir(input_file)

            filename=data_utils.get_file_name_from_path(input_file)

            ''' Reads all data until EOF is reached,
            here bytes are returned as string object '''
            input = open(filename, 'r')
            return input.read()
    except IOError:
        print 'Error in opening or reading an input file'
        sys.exit()

def read_all_lines(input_file):

    '''
    Read a text file with filename as input_file.
    Return a list of lines of text in the file.
    '''
    try:
        if(data_utils.file_exist(input_file)):
            '''Sets current working directory to directory of
             input_file'''
            data_utils.set_working_dir(input_file)

            filename=data_utils.get_file_name_from_path(input_file)

            ''' Reads all data until EOF is reached,
            here bytes returned as string object '''
            input = open(filename, 'r')
            return input.readlines()
    except IOError:
        print 'Error in opening or reading an input file'
        sys.exit()