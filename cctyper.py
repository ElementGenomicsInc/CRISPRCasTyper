import sys
import os

fna = sys.argv[1]
outdir = sys.argv[2]

if ".gz" in fna:
    renamed = fna.split(".")[0] + "_copy.fna"
    gzipped = renamed+".gz"
    os.system("cp {} {}".format(fna, gzipped))
    os.system("gunzip {}".format(gzipped))
    fna = renamed

os.system("conda run -n cctyper /CRISPRCasTyper/bin/cctyper --no_plot {} {}".format(fna, outdir))