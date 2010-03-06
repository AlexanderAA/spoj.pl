#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
'''
The solution for the LAZYPROG problem (https://www.spoj.pl/problems/LAZYPROG/),

'''
from __future__ import division
import sys

__version__ = "February 9, 2010"
__author__ = ('Alexander Abushkevich, '
              'E: a.abushkevich@gmail.com, T: +375 29 5517082')

def main():
    '''Reads input data from stdin and calculates (writes to stdout) 
    the minimum sum of money which the director needs to pay extra 
    so that the programmer could perform all contracts in time. 
    
    No data validation and error checks. 
    
    Data should strictly meet the requirements:
    First line of the input contains an integer t (1 <= t <= 45), 
    equal to the number of testcases. Then descriptions of t testcases follow.
    First line of description contains the number 
    of contracts N (1 <= N <= 100000, integer). 
    Each of the next N lines describes one contract and 
    contains integer numbers ai, bi, di 
    (1 <= ai, bi <= 10000; 1 <= di <= 1000000000)
    separated by spaces.
    At least 90% of testcases will have 1 <= N <= 10000. 
    
    Returns:
        List of test cases. Every test case is a list of contracts.
        Every contact is a list, containing three integers: a_i, b_i, d_i
        Example:
        [
        [[20, 50, 100],[10, 100, 50]],
        [[20, 50, 100],[20, 50, 200],[20, 50, 300]]
        ]
        
    Raises:
        ValueError if input data is incorrect
        KeyboardInterrupt
        
    '''
    test_cases = []
    for test_case in xrange(int(sys.stdin.readline())):
        test_case = []
        sum_x = 0
        for contract in xrange(int(sys.stdin.readline())):
            a,b,d = map(int , sys.stdin.readline().split())
            if (b - a) > d:
                sum_x += (b - d)/a
        print "%.2f" % sum_x

if __name__ == "__main__":
    main()
