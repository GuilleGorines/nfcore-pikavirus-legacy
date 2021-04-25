#!/usr/bin/env python

import sys
import os
import shutil

mashresult = sys.argv[1]
refdir = sys.argv[2]

with open(mashresult) as infile:
    infile = infile.readlines()

    # remove header 
    infile = [line.split() for line in infile if not line.startswith("#")]

    # get name amd remove extension of file if p-val < 0.05
    infile = [line[0].split()[0] for line in infile if float(line[2]) < 0.05]

# files without extension 
reference_dict = {item.split()[0]:item for item in os.listdir()}

os.mkdir(f"Final_fnas", 0o777)

for filename in infile:
    if filename in reference_dict.keys():
        shutil.copyfile(f"{refdir}/{reference_dict[filename]}",f"Final_fnas/{reference_dict[filename]}")


