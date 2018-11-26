#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:25:01 2018

@author: mathilde
"""



def is_prime(n) :
    if (not(type(n) is int)) :
        raise ValueError("n doit etre un entier")
    elif n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True

print(is_prime(3))
print(is_prime(15))