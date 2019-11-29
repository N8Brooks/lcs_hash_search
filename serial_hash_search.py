# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:55:06 2019

@author: Nathan
"""

from array import array
from zlib import crc32

# iterative hash function using previous hash as base
hash_function = lambda word, base: crc32(word.encode(), base)

def lcs(a: str, b: str):
    """
    Args:
        a (str): The first string to compute lcs of
        b (str): The second string to compute the lcs of
    
    Returns:
        int: the length of the lcs of a and b
        list: a list of longest common substrings between a and b
    """
    
    # returns if there is a common substring of length m with dictionary
    def found_common(set_a, set_b, m):
        set_a = {x:i for i, x in enumerate(set_a)}
        return any(x in set_a and a[set_a[x]:set_a[x]+m] == \
            b[i:i+m] for i, x in enumerate(set_b))
    
    # a should be smaller than b to minimize dictionary size in found_common
    len_a, len_b = len(a) + 1, len(b) + 1
    if len_a > len_b:
        len_a, len_b = len_b, len_a
        a, b = b, a
    
    # exponentially increase r until there are no substrings of len r
    l, r = 0, 1
    L_a = array('L', [0]*len_a)
    R_a = array('L', map(hash_function, a, L_a[1:]))
    L_b = array('L', [0]*len_b)
    R_b = array('L', map(hash_function, b, L_b[1:]))
    while r < len_a and found_common(R_a, R_b, r):
        L_a, R_a = R_a, array('L', map(hash_function, (a[i:i+r] \
            for i in range(r, len(a))), R_a[:-r]))
        L_b, R_b = R_b, array('L', map(hash_function, (b[i:i+r] \
            for i in range(r, len(b))), R_b[:-r]))
        l, r = r, r * 2
    
    # r cannot be more than the length of a (smaller text)
    r = min(r, len(a))
    
    # right-most binary search on if substring length is in both
    while l < r:
        m = (l + r) // 2
        d = m - l
        R_a = array('L', map(hash_function, (a[i:i+d] \
            for i in range(d, len(a))), L_a[:-d]))
        R_b = array('L', map(hash_function, (b[i:i+d] \
            for i in range(d, len(a))), L_b[:-d]))
        
        if found_common(R_a, R_b, m):
            l = m
            L_a, L_b = R_a, R_b
        else:
            r = m
    
    # get the longest common substrings using found_common algorithm
    set_a = {x:i for i, x in enumerate(L_a)}
    unique = list()
    for i, x in enumerate(L_b):
        if x in set_a and a[set_a[x]:set_a[x]+l] == b[i:i+l]:
            unique.append(a[set_a[x]:set_a[x]+l])
    
    # return integer length, return set of longest common substrings
    return l, unique








