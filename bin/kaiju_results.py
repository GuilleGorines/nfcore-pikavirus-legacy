#!/usr/bin/env python

import sys

outfile_name = sys.argvs[1]
file = sys.argvs[2]


# Extraer los datos de id, tamaño del contig y coverage
def process_node_data(input_string, classified = False):
    output_list = []
    
    for item in input_string:
        data = item[1].split("_")
        node_id, node_length, node_coverage = data[1], data[3], data[5]
        
        if classified == True:
            taxid = item[2]
            score = item[3]
            
            identifiers = item[4].split(",")
            identifiers = [n for n in identifiers if len(n) > 0]         
            
            accession_numbers = item[5].split(",")
            accession_numbers = [n for n in accession_numbers if len(n) > 0]
            
            organism_name = item[7]
            
        else:
            taxid = str()
            score = str()
            identifiers = str()
            accession_numbers=str()
            organism_name=str()
            
        output_list.append([node_id, node_length, node_coverage, taxid, score, identifiers, accession_numbers,organism_name])
            
    return output_list

def plot_coincidences(classified_list):
    import matplotlib.pyplot as plt
    
    plot_dict = {}
    
    for item in classified_list:
        if item[7] not in plot_dict.keys():
            plot_dict[item[7]] = 1
        else:
            plot_dict[item[7]] += 1
            
    plt.pie(plot_dict.values(),labels=plot_dict.keys())

plot_coincidences(process_node_data(classified,classified=True))


with open(file) as infile:
    infile = infile.readlines()
infile = [item for item in infile]
infile = [item.strip("\n").split("\t") for item in infile]

unclassified = [item for item in infile if item[0]=="U"]
classified = [item for item in infile if item[0]=="C"]


classified_treated = process_node_data(classified, classified=True)
unclassified_treated = process_node_data(unclassified)