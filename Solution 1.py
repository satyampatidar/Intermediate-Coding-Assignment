# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:41:17 2020

@author: Satyam Patidar
Win Cartell
"""
dictName = {}

def task():
    while True:
      nname1 = input("Give the nick name of your friend:")
      if ("q" == nname1 or "Q" == nname1):
        print("Ok Bye")
        break
      for key, value in dictName.items():
             if nname1 == value:
                print("Your friend's full name is:",key)
                break
    
while True:
    k=input("Please input full name: ")
    if(k == 'q' or k == 'Q'):
        print("You quit")
        task()
        break
    v=input("Please input nick name: ")
    dictName[k] = v
    

    