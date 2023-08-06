# d2ssect

![conda install test badge](https://github.com/iracooke/d2ssect/actions/workflows/conda_install.yml/badge.svg)

![linux install test badge](https://github.com/iracooke/d2ssect/actions/workflows/linux_install.yml/badge.svg)

A tool to calculate d2s scores using short fastq reads
This repo will test and benchmark the existing [alignment-free tools](https://github.com/chanlab-genomics/alignment-free-tools) and the improving versions.

The originally version of this pipeline including three big steps:
1. get jellyfish count results
2. calculate d2s using jellyfish dump results of every pair of samples
3. generate a matrix

Our goal is to integrate these three steps and try to increase the speed of d2s calculation.


## Installation

`d2ssect` relies heavily on [jellyfish](https://github.com/gmarcais/Jellyfish).  You need the jellyfish program and also the jellyfish libraries.  To check that jellyfish is installed you can do;
```bash
jellyfish --version
```
Which should return a version > 2. In addition, you need the jellyfish libraries and headers. If you installed jellyfish via `conda` or by compiling from source these will be present in the right locations.  If you installed it your linux package manager they probably won't be present. 

If you do not want to use `conda` we recommend installing Jellyfish from source.  Once done you should then be able to install `d2ssect` using pip

```bash
pip3 install d2ssect
```



## Usage

Lets say we have a collection of fasta files corresponding to sequencing reads from samples that we want to compare with `d2ssect`.  First count kmers in these files using `jellyfish`

```bash
for f in *.fasta;do jellyfish count -m 21 -s 10000000 $f -o ${f%.fasta}.jf ;done
```

Note that the command above will create a corresponding `.jf` file for every `.fasta` file in the current directory. By keeping the base names of the `jf` and `fasta` files identical we can then run `d2ssect` as follows;

```bash
python3 ../d2ssect/d2ssect/main.py -l *.jf -f *.fasta
```


## Building from source

```
CC=g++ pip install .
```