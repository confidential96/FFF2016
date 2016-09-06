#!/usr/bin/env python
#This program scripts various VM controls 
import pprint, time, sys
import subprocess
from subprocess import PIPE,Popen
import sys
import threading
import unicodedata
import os


if __name__ == "__main__": 
	f = open ('text.txt', 'w')
	directory = "./"
	for filename in os.listdir(directory):
		if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG"): 
			f.write("""<div data-p=\"144.50\" style="display: none;\">
	                <img data-u=\"image\" src=\"img/"""+filename+"""\" />
	                <img data-u=\"thumb\" src=\"img/"""+filename+"""\" />
	            </div>""")
			continue
		else:
			continue
