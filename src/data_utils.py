__author__ = 'DimpleSharma'

''' This file implements functions for file location operations
    such as set working directory and file exist.'''

import os

def set_working_dir(file_path):
    ''' Sets directory of file_path as current working directory'''

    '''Get parent of current working directory '''
    current_src_path = os.path.dirname(__file__)
    parent = os.path.abspath(os.path.join(current_src_path, os.pardir))

    ''' Get directory of file path '''
    directory = os.path.dirname(file_path)

    # Verify whether dir exist before changing working directory
    path = os.path.normpath(os.path.join(parent, directory))

    '''Sets current working directory as directory of file in file_path,
    where the file can be found'''
    if os.path.exists(path):
        os.chdir(path)
    else:
        print 'Invalid path. {0}'% path

def file_exist(file_name):

    '''Get parent of current working directory '''
    current_src_path = os.path.dirname(__file__)
    parent = os.path.abspath(os.path.join(current_src_path, os.pardir))

    #print parent
    #print os.path.join(parent, file_name)
    #parent = os.path.abspath(os.path.pardir)

    path = os.path.normpath(os.path.join(parent, file_name))

    '''Verify whether the file exists'''
    if os.path.isfile(os.path.join(parent, file_name)):
        return True
    else:
        return False

def get_file_name_from_path(path):
    filename = ''
    try:
        filename = os.path.basename(path)
    except:
        print 'An error occurred while getting file name from path.'
    return filename

def write_to_text_file(word_dict, file_path):

    #filename =
    output = open(filename, 'w')
    output.write(str(word_dict))
