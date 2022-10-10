import os
import time
from itertools import product
import pandas as pd

def count_kmers(Sequence, kmer, kmin, kmax):
    n = len(Sequence)
    km = range(kmin, kmax + 1)
    counter = dict()
    for k in km:
        for i in range(0, n - k + 1, 1):
            mer = Sequence[i: i + k]
            counter[mer] = counter.get(mer, 0) + 1
    return [counter.get(key, 0) for key in kmer]


def sequence2kmer(seq_path: str) -> str:
    """
    The function takes a sequence file as input and generates kmers of length 6 and 7 (last 2000 each)
    for more info. refer the sample features csv file
    :param seq_path: Path to the sequence fasta file.
    :return: Last 2000 kmers of length 6 and 7 as a csv file.
    """

    m = 6
    n = 7

    kmer = generate_kmer(m, n) #generating the required kmers of length 6 and 7

    seq_path = 'sequence.fasta'

    df = pd.DataFrame(columns=kmer)
    

    time1 = time.perf_counter()

    with open(seq_path, 'r') as seq_file:
        sequence = seq_file.read()

    print(f"Generating Features.")
    df.loc[len(df)] = count_kmers(sequence, kmer, m, n)

    time2 = time.perf_counter()

    print(f"Saving Generated Features.")
    tot_time = round(time2 - time1)

    print(f'Time Taken for Feature Generation [HH:MM:SS]: {time_convert(tot_time)}')
    
    df.columns = kmer
    
    file_path = f'features.csv'
    df.to_csv(file_path, index=False)

    return file_path
