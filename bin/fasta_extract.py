#!/usr/bin/python3
import sys

exitmsg1 = "\nThis script reads a multifasta file, and extracts only those sequences whose ID contain a string included in the IDs list file (non case-sensitive).\
\n2 arguments are needed: first the multifasta file and second the list of IDs to find inside the multifasta file. \
\n\nUSAGE: python fasta_extract.py multifasta.fasta IDs.txt > output.fasta\n\n"

exitmsg2 = "Could not read input files. Please make sure everything is OK."

if len(sys.argv) != 3:
    sys.exit(exitmsg1)

multifasta_file = str(sys.argv[1])
id_file = str(sys.argv[2])

try:
    with open(id_file) as id_list:
        id_list=set(map(lambda x: x.strip(),id_list))

    fasta = open(multifasta_file, "r")
    multifasta = (map(lambda x: x.strip(),fasta.readlines()))
except IOError:
    sys.exit(exitmsg2)

copy=False

for line in multifasta:
    if line.startswith(">"):
        for id in id_list:
            if id.lower() in line.lower():
                copy = True
                print(line)
                break
            else:
                copy = False
    else:
      if copy:
          print(line)

fasta.close()
exit 










