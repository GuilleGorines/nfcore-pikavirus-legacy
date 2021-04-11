#!/usr/bin/python

# Imports

import sys
import re

# Needed msgs (error, header)

exitmsg1="\n2 files needed: blasn_filtered and coverage_table \n\n\
USAGE: summary_tables.py blasn_filtered_file coverage_table_file\n"

exitmsg2="Could not read input files. Please make sure everything is OK"

header=["Genome\tBlastScore\tContigLength\tContig\%Mapped\tContigName\
\tcovMean\tcovSD\tcovMedian\tx1-x4\tx5-x9\tx10-x19\t>x20\ttotal\n"]

# Initial checks (n args, able to open files)

if len(sys.argv) != 3:
    sys.exit(exitmsg1)

blastfile = sys.argv[1]
coveragefile = sys.argv[2]
outfile = sys.argv[1]+"_filtered.blast_summary.tsv"

try:
    with open(blastfile) as infile:
        infile=infile.readlines()

    with open(coveragefile) as coverage:
        coverage=coverage.readlines()

except IOError:
    sys.exit(exitmsg2)

coverdict={}

for line in coverage:
    line.rstrip().replace("\"","")
    item = line.split("\t")[0]
    coverdict[item] = line

lastfile = open(outfile,"w+")
lastfile.write(header)

for line in infile:
    line=line.rstrip().split("\t")
    genome=line[0]
    contig=line[2]
    blast_score=line[3]
    contig_len=line[1].replace()
    contig_percentage=int(line[4]/contig_len*10000)/100

    if contig_percentage > 90:
        data=f"{genome}\t{blast_score}\t{contig_len}\t{contig_percentage}\t{coverdict[{contig}]}\n"
        lastfile.write(data)

exit