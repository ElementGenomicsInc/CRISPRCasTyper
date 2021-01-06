fna=$1
outdir=$2

prefix=${fna%.fna.gz}
cp $fna ${prefix}_copy.fna.gz
gunzip ${prefix}_copy.fna.gz

conda run -n cctyper /CRISPRCasTyper/bin/cctyper --no_plot ${prefix}_copy.fna $outdir