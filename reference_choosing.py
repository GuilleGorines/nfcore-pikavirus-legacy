import sys
import os
import subprocess
from pathlib import Path

krakenrep = sys.argv[1]
refdir = Path(sys.argv[2])
query = sys.argv[3]
threads = sys.argv[4]

if not threads:
    threads = 1

with open(krakenrep) as krakenreport:
    krakenreport = [line.split("\t") for line in krakenreport.readlines()]
    idlist = []
    for line in krakenreport:
        if line[3] == "S":
            idlist.append(line[4])

    if len(idlist) == 0:
        print(f"No species were identified in the kraken report.")
        sys.exit(2)    
# Report:
#   3: rank code (Unclass, Kingdom...)
#   4: taxID
#   5: scientific_name (indented)

filedict = {}

for taxid in idlist:
    for filename in os.listdir(refdir):
        if speciesname in namelist:
            if speciesname not in filedict.keys():
                dirdict[speciesname]=[filename]
            else:
                dirdict[speciesname].append[filename]

for taxid,reffiles in filedict.items():
    fullprocess = ["mash","dist","-p",threads,"-l",reffiles,query]
    process_result = subprocess.check_output(fullprocess, stdout = outfile)
    print(process_result)

