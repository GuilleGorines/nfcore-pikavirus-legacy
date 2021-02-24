import sys

info_msg = f"Usage: \n extract_reference_assemblies.py kraken2_output NCBI_assembly_summary.txt. \n The assembly summary is available in ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/."
krakenout = sys.argv[1]
summary = sys.argv[2]

with open(krakenout) as krakenfile:
    krakenfile = krakenfile.readlines().split("\t")
    krakenfile = [col[3] for col in krakenfile if col[0]=="C"]

# Output:
#   0: C(lassified) / U(nclassified)
#   2: Taxid

# Report:
#   3: rank code (Unclass, Kingdom...)
#   4: taxID
#   6: scientific_name

with open(summary) as assembly_sum:
    assembly_sum = [line.split("\t") for line in assembly_sum.readlines() if not line.startswith("#")]
    assembly_sum = []

    # 0: assembly_accession
    # 4: refseq_category
    # 5: taxid ## EL DE RANGO MÁS BAJO QUE HAYA, STRAIN O SUBESPECIE SI SE PUEDE
    # 6: species_taxid ## LA ESPECIE
    # 7: scientific_name
    # 8: intraespecific_name (strain, breed, ecotype)
    # 11: assembly_level (complete genome, chromosome, scaffold, contig)
    # 13: genome_rep ()
    # 19: url
    