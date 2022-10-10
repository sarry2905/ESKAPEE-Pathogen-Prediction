import os
import gzip
from pathlib import Path


def readFastq(fh):  # function for reading and cleaning the raw clinical sequence.
    sequences = []  # It will store clean sequence.
    # with open(filename) as fh:  # opening clinical sequence
    while True:
        fh.readline()  # skip name line
        seq = fh.readline().rstrip()  # read base sequence
        fh.readline()  # skip placeholder line
        fh.readline()  # base quality line
        if len(seq) == 0:
            break
        sequences.append(seq)
    return sequences  # We want only clean sequence so returning only sequences.


def readFasta(fh):  # function for reading and cleaning the raw clinical sequence.
    sequences = []  # It will store clean sequence.
    # with open(filename) as fh:  # opening clinical sequence
    while True:
        fh.readline()  # skip name line
        seq = fh.readline().rstrip()  # read base sequence
        if len(seq) == 0:
            break
        sequences.append(seq)
    return sequences  # We want only clean sequence so returning only sequences.


def extract_sequence(gz_filepath):

    seq_path = 'sequence.fasta'
    
    with gzip.open(gz_filepath, 'rt') as f_in:
        if fileformat in fastq_formats:
            sequence = ' '.join([str(element) for element in readFastq(f_in)]).replace(',', "").replace(" ", "")
        else:
            sequence = ' '.join([str(element) for element in readFasta(f_in)]).replace(',', "").replace(" ", "")

    with open(seq_path, 'w') as f_out:
        f_out.write(sequence)

    return seq_path
