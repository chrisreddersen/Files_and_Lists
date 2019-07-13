#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:00:13 2018

@author: chris
"""

import os
listings = []# created an empty list
filename = input('Choose file:  ')

def main():               # main function
    print('YOUR LIST')
    
    enter_file()
    
def enter_file():
    
    menu =  "[A]dd [Q]uit: "
    if not filename in os.listdir("."):
        f = open(filename,'w+')
        print('**no items in this list**')
        menu_choice = input(menu)
        if menu_choice == 'A'or 'a':
            add_item()
        else:
            print('buh bye')
    else:
        with open(filename,'r+') as f:
            for item in f:
                listings.append(item)
            print('these items are in your list')
            print(listings)
            add_item()
            
def add_item():
    add_items= input("Add item: ")
    listings.append(add_items)
    
    print(listings)
    next_menu_choice = input('[A]dd [Q]uit [S]ave: ')
    for choice in next_menu_choice:
        if choice == 'a':
                add_item()
        elif choice ==  's':
            for item in listings:
                save_item()
                
        elif choice == 'q':
                print('buh bye')
                
        else:
            print('not a valid choice')
            add_item()
            
def save_item():# could not figure out how to save multiple items at once
    
        
        filename = input('Choose file to save too:  ')
        with open(filename,'w+') as f:
            for item in listings:
                f.writelines(item)
        f.close()    
        print(listings)
        print('your item(s) are saved')
            
        
        
            
main()