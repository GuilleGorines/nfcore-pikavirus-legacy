#!/usr/bin/env python

import sys
import os

mashresult = sys.argv[1]
refdir = sys.argv[2]
realpath = os.path.realpath(refdir)

with open(mashresult) as infile:
    infile = infile.readlines()

    # remove header 
    infile = [line.split() for line in infile if not line.startswith("#")]

    # get name amd remove extension of file if p-val < 0.10
    infile = [line[0].split()[0] for line in infile if float(line[2]) < 0.10]
    
# files without extension 
reference_dict = {item.split()[0]:[f"{realpath}/{item}",f"Final_fnas/{item}"] for item in os.listdir(refdir)}

os.mkdir(f"Final_fnas", 0o777)

for filename in infile:
    if filename in reference_dict.keys():
        os.symlink(reference_dict[filename][0],reference_dict[filename][1])


