#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
''' The solution for the TOANDFRO problem 
(https://www.spoj.pl/problems/TOANDFRO/)
'''
__version__ = "February 9, 2010"
__author__ = ('Alexander Abushkevich, '
              'E: a.abushkevich@gmail.com, T: +375 29 5517082')

import sys
import traceback

def decryption_vector(num_rows, num_columns):
    '''Generate vector (list of indexes) for decryption.
    
    Example:
        For matrix 3x3 (3 rows, 3 columns)
        | 0 3 6 |
        | 1 4 7 |
        | 2 5 8 |
        
        result will be:
        [1 4 6 7 5 2 3 6 8] 
        
    >>> decryption_vector(3, 3)
    [0, 3, 6, 7, 4, 1, 2, 5, 8]
    >>> decryption_vector(0, 0)
    []
    >>> decryption_vector(1, 3)
    [0, 1, 2]
    
    Args:
        num_rows: integer, num_rows >= 0
        num_columns: integer, num_columns >= 0
    
    Returns:
        list of integers, vector for decryption
        
    Raises:
        TypeError if argument type is not correct
        
    '''
    d_vect = []
    for j in xrange(num_rows):
        row = []
        for i in xrange(num_columns):
            row.append(num_rows*i + j)
        d_vect.extend(row[:: -1*(j%2) or 1])
    return d_vect

def decrypt(encrypted_string, decryption_vector):
    '''Decrypts encrypted string
    
    Examples:
    >>> decrypt("aexl", [0, 2, 3, 1])
    'alex'
    
    Args:
        decryption vector: list of integers
        encrypted string: basestring
        
    Returns:
        decrypted string (basestring)
    '''
    assert isinstance(encrypted_string, basestring)
    assert isinstance(decryption_vector, list)
    
    assoc = {}
    for i in xrange(len(decryption_vector)):
        assoc[decryption_vector[i]] = encrypted_string[i]
        
    decrypted_list = [str(assoc[i]) for i in xrange(len(assoc))]
    return ''.join(decrypted_list)

def main():
    '''Reads and decrypts the string from stdin.
    
    Input data format:
    Input will consist of two lines. The first line will contain an integer 
    in the range 2...20 indicating the number of columns used. 
    The next line is a string of up to 200 lower case letters. 
    The last input set is followed by a line containing a single 0, 
    indicating end of input.
    '''
    while True: 
        try:
            # reads number of columns from stdin
            num_columns = int(raw_input().strip())
            if num_columns ==0:
                # The last input set is followed by a line containing 
                #a single 0, indicating end of input.
                break
            # reads encrypted string from stdin
            encrypted_string = raw_input().strip()
            # simple validation
            if (num_columns > 0) and (len(encrypted_string) % num_columns == 0):
                num_rows = len(encrypted_string)/num_columns
            else:
                num_rows = 0
                num_columns = 0
                encrypted_string = ''
            # decryption vector calculation
            d_vect = decryption_vector(num_rows, num_columns)
            # output
            print decrypt(encrypted_string, d_vect)
        except KeyboardInterrupt:
            print 'Ctrl-C pressed. Exiting...'
            break
        except Exception:
            # report error
            sys.stderr.write("ERROR!")
            traceback.print_exc(file=sys.stderr)
            sys.stderr.write("Exiting...\n\n")
            break

if __name__ == "__main__":
##    import doctest
##    doctest.testmod()
    main()