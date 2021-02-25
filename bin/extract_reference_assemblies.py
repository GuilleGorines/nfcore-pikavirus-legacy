import sys
import csv

info_msg = f"Usage: \n extract_reference_assemblies.py kraken2_report NCBI_assembly_summary.txt. \n The assembly summary is available in ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/."
krakenrep = sys.argv[1]
summary = sys.argv[2]
name_end = sys.argv[3]

with open(krakenrep) as krakenfile:
    krakenfile = krakenfile.readlines().split("\t")
    krakenfile = [col[4] for col in krakenfile if col[3]=="S"]
    taxid_list = set(krakenfile)

# Report:
#   3: rank code (Unclass, Kingdom...)
#   4: taxID
#   6: scientific_name

with open(summary) as assembly_sum:
    assembly_sum = [line.split("\t") for line in assembly_sum.readlines() if not line.startswith("#")]

assembly_sum = [col[7], col[6], col[0], col[11], col[4], col[13], col[19] for col in krakenfile if col[6] in taxid_list]
    
# 0: assembly_accession
# 4: refseq_category
# 5: taxid
# 6: species_taxid
# 7: scientific_name 
# 8: intraespecific_name
# 11: assembly_level 
# 13: genome_rep
# 19: url
# full info: ftp://ftp.ncbi.nlm.nih.gov/genomes/README_assembly_summary.txt

header=["Scientific_name", "Species_Taxonomic_ID", "Assembly_accession_chosen", "Assembly_level", "Refseq_category", "Representation", "Assembly_url"]
assembly_sum.insert(0,header)

namefile = f"chosen_assemblies_data_{name_end}.tsv"
with open(namefile, "w") as chosen_assemblies:
    chosen_assemblies_tsv = csv.writer(chosen_assemblies, delimiter = "\t")
    chosen_assemblies_tsv.writerow(assembly_sum)