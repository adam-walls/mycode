#!/usr/bin/env python3

# Let you copy, move, rename, and delete files on your local system, from your Python program
import shutil
# This module provides a portable way of using operating system dependent functionality
import os

# Always start in the home user directory
os.chdir("/home/student/mycode/")

# Copy file at path source to the folder at path destination (Copy fileA to fileB)
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# Will copy an entire folder and every folder and file contained in it (Copy dirA to dirB) 
# creates a new folder named 5g_research_backup with the same content as the original folder
shutil.copytree("5g_research/", "5g_research_backup/")

