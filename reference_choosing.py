import sys
import os
import subprocess
from pathlib import Path

krakenrep = sys.argv[1]
refdir = Path(sys.argv[2])
query = sys.argv[3]
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
        if taxid in filename:
            if taxid not in filedict.keys():
                filedict.setdefault(taxid,[]).append(f"{refdir}/{filename}")
            else:
                if f"{refdir}/{filename}" not in filedict[taxid]:
                    filedict[taxid].append(f"{refdir}/{filename}")

mashdict = {}
for taxid,reffiles in filedict.items():
    mashdict[taxid] = []
    if len(reffiles) > 0:
        with open(f"{taxid}_mash.txt","w") as outfile:
            for single_reffile in reffiles:
                fullprocess = ["mash", "dist", "-p", str(threads),single_reffile, query]
                mashcommand = subprocess.run(fullprocess, stdout=subprocess.PIPE)
                mashdict[taxid].append(mashcommand.stdout.decode("utf8").replace("\n","").split("\t"))

os.mkdir(f"Chosen_fnas", 0o777)

for taxid,mashresults in mashdict.items():
    true_mashresults = [result for result in mashresults if float(result[3]) < 0.05]
    for fna in true_mashresults:
        filename = fna[0].split("\t")[-1]
        os.replace(fna[0],f"Chosen_fnas/{filename}")

