__author__ = 'DimpleSharma'

import os
import data_utils

def write_to_text_file(text, path):
    ''' Writes text to file, where text is a string. '''

    try:

        data_utils.set_working_dir(path)
        '''Gets file name from path'''
        filename = os.path.basename(path)
        feature = open(filename, 'w')
        feature.write(text)
        feature.close()
        return True
    except IOError:
        print 'An exception occurred while saving the file'

    return False
