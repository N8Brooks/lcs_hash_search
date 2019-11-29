# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:50:03 2019

@author: Nathan
"""

import sys
import serial_hash_search
import parallel_hash_search

PARALLEL = False

# function to read in utf-8 txt file
def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == '__main__':
    """
    Command line arguments:
        str: the path to the text file to compute the lcs of
        str: the path to the second text file to compute the lcs of
    Prints:
        int: the length of the lcs
        list: a list of all longest common substrings
    """
    
    # read in command line arguments
    if len(sys.argv) is 3:
        # read in text files
        a = read_text(str(sys.argv[1]))
        b = read_text(str(sys.argv[2]))
    else:
        print('Please enter to txt file arguments to read.')
        exit()
    
    # grab parallel version if indicated
    lcs = parallel_hash_search.lcs if PARALLEL else serial_hash_search.lcs

    # get the length of lcs and list of longest common substrings
    length, substrings = lcs(a, b)
    if len(substrings) is 1:
        multiple = ['is', len(substrings), '']
    else:
        multiple = ['are', len(substrings), 's']
    
    # print
    print(f'The length of the longest common substring is: {length}')
    print('There {} {} longest common substring{}:'.format(*multiple))
    print('\n'.join(f'"{s}"' for s in substrings), end='')
