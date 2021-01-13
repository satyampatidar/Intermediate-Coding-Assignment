# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:21:04 2020

@author: Satyam Patidar (MCS20026)
Win Cartell
"""
import sympy
from sympy import *

def split(num):
        if sympy.isprime(num):
            prime.append(num)
        elif simplify(num).is_odd:
            odd.append(num)
        else:
            even.append(num)
        return odd, even, prime        
even = []
odd = []
prime = []
while True:
	a = input("Input an integer or q or Q to quit:")
	if a == 'q' or a == 'Q':
		print("List of Primes : ",prime)
		print("List of Odds : ",odd)
		print("List of Evens : ",even)
		break
	num = int(a)
	split(num)
