#!/usr/bin/env python3

## We shall generate a script that will help us delete contents of a directory

import os, shutil

absolute_directory = input('Enter the absolute path to the directory you want to purge: ')

directory_contents = os.listdir(absolute_directory)
for items in directory_contents:
    abs_items_location = os.path.join(absolute_directory, items)
    
    if os.path.isfile(abs_items_location) or os.path.islink(abs_items_location):
        os.unlink(abs_items_location)
    elif os.path.isdir(abs_items_location):
        shutil.rmtree(abs_items_location)
        
        
