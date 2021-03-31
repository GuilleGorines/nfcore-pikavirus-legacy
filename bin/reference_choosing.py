#!/usr/bin/env python

import sys
import os
import subprocess

krakenrep = sys.argv[1]
refdir = sys.argv[2]
query = sys.argv[3]
threads = sys.argv[4]

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

print(mashdict)
os.mkdir(f"Chosen_fnas", 0o777)

with open("mash_results.txt","w") as outfile:
    outfile.write("Taxid\tReference file\tMash-distance\tP-value\tMatching_hashes\tChosen\n")
    for taxid,mashresults in mashdict.items():
        for result in mashresults:
            if float(result[3]) < 0.05:
                chosen = "Yes"
            else:
                chosen = "No"
            out_line = f"{taxid}\t{result[0]}\t{result[2]}\t{result[3]}\t{result[4]}\t{chosen}\n"
            outfile.write(out_line)


        true_mashresults = [result for result in mashresults if float(result[3]) < 0.05]
        for fna in true_mashresults:
            filename = fna[0].split("\t")[-1].split("/")[1]
            os.symlink(fna[0],f"Chosen_fnas/{filename}")

