#!/usr/bin/env python3

# Shell Utility module
import shutil
# This module provides a portable way of using operating system dependent functionality
import os

# Start in home user directory
os.chdir('/home/student/mycode/')

# shutil.move(source, destination); Move the file or folder at the path source to 
# the path destination and will return a string of the absolute path of the new location.
shutil.move('raynor.obj', 'ceph_storage/')

# Prompt user for new name for kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')
# Rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


