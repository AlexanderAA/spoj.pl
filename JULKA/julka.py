#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
''' The solution for the JULKA problem 
(https://www.spoj.pl/problems/JULKA/),
'''
__version__ = "February 9, 2010"
__author__ = ('Alexander Abushkevich, '
              'E: a.abushkevich@gmail.com, T: +375 29 5517082')
import sys
import traceback

def main():
    '''Calculates and prints to stdout the number 
    of apples for Klaudia and Natalia. 
    
    Input data: exactly 10 test cases.
    Every test case consists of two lines. The first line says how many 
    apples both girls have together. The second line says how many more apples 
    Klaudia has. Both numbers are positive integers. 
    It is known that both girls have no more than 10100 (1 and 100 zeros) 
    apples together. As you can see apples can be very small. 
    '''
    for i in xrange(10): 
        try:
            count = long(raw_input().strip())
            difference = long(raw_input().strip())
            c_odd = count%2 
            d_odd = difference%2
            if (not c_odd and not d_odd):
                print long(count/2 + difference/2)
                print long(count/2 - difference/2)
            elif (c_odd and d_odd):
                print long(count/2 + difference/2 + 1)
                print long(count/2 - difference/2)
            else:
                print '\n' # we need a knife
                # Actually, this case was not mentioned in problem description.
                # As a result, it will not be included in solution
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
    main()