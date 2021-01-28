#!/usr/bin/python

# Imports
import sys
import matplotlib.pyplot as plt
import statistics

# Needed msgs (errors)
exitmsg1="\n2 files needed: blasn_filtered and coverage_table \n\n\
USAGE: graphs_coverage.py \n"

# Argument check
if len(sys.argv) != 3:
    sys.exit(exitmsg1)

sampleCoverageDir = sys.argv[1]
sampleName = sys.argv[2]
fileName = f"{sampleCoverageDir}/{sampleName}_genome_coverage.txt"


try:
    with open(fileName) as file:
        file = [slot for slot in file.readlines().split("\t")]

except IOError:
    sys.exit()


## HAY QUE ARREGLAR LO DEL CUMSUM, no se hace así
cov=sorted(
    ([[element[0], element[1], element[4], 1-cumsum(element[4])] for element in file]),
    key=lambda x: (x[1],x[2])
    )

new_cov=[["gnm", "covMean", "covMin", "covMax", "covSD", "covMedian"]]

for uniq_genome in [set([element[0] for element in cov].sort())]:
    coincidences = [genome in cov if cov[0]== uniq_genome]
        covMean = sum([grouped_genomes[1]*grouped_genomes[2] for grouped_genomes in coincidences])
        covMin = min([grouped_genmaxCov=500 # Value chosen for aesthetic reasons
omes[1] for grouped_genomes in coincidences])
        covMax = max([grouped_genomes[1] for grouped_genomes in coincidences])
        covSD = sum([grouped_genomes[1]*(grouped_genomes[2]-covMean)² for grouped_genomes in coincidences])
        covMedian = statistics.median([grouped_genomes[1] for grouped_genomes in coincidences])
        new_cov.append([uniq_genome,covMean, covMin, covMax, covSD, covMedian])

summary_cov=[["gnm","x1-x4","x5-x9","x10-x19",">x20","total"]]

cov_frac_threshold_by_name=[["covThreshold","fracAboveThreshold"]]

for uniq_genome in [set([element[0] for element in cov].sort())]:
    coincidences = [genome in cov if cov[0]== uniq_genome]
    cov_threshold.append([element[4], element[] for element in coincidences])
    # Me quedo con una lista que contiene los datos de lo que comparte gnm
    y0=sum([ element[4] for element in coincidences if coincidences[2] => 1 and coincidences[2] < 5 ])
    y1=sum([ element[4] for element in coincidences if coincidences[2] => 5 and coincidences[2] < 10 ])
    y2=sum([ element[4] for element in coincidences if coincidences[2] => 10 and coincidences[2] < 20 ])
    y3=sum([ element[4] for element in coincidences if coincidences[2] >= 20 ])
    y4=y0+y1+y2+y3

    summary_cov.append([y0,y1,y2,y3,y4])

cov_def = [new_cov[i].extend(i for i in cov_threshold_by_sample_name).extend(summary_cov[i][1-5] for i in range(len(summary_cov)) if new_cov[i][1] != 0])


maxCov=500 # Chosen for aesthetic reasons
threshold_pass= [element for element in cov_def if element[1] != 0 and element[6] < maxCov]
for genome in threshold_pass:
    x_axis=[ element[6] for element in threshold_pass ]
    y_axis=[ element[]*100 for element in threshold_pass ]
    plt.plot(x_axis,y_axis)
    plt.ylabel("Depht of coverage")
    plt.xlabel("Percentage of coverage")
    plt.title("Genome coverage")
    plt.show()
    filename=f'{element[0]}_coverage_graph.pdf'
    plt.savefig(filename)

    