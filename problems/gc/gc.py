"""gc.py

Alexander Craig
2022-02-23

ROSALIND | Computing GC Content

Problem:
The GC-content of a DNA string is given by the percentage of symbols
in the string that are 'C' or 'G'. For example, the GC-content of
"AGCTATAG" is 37.5%. Note that the reverse complement of any DNA
string has the same GC-content. DNA strings must be labeled when they
are consolidated into a database.  A commonly used method of string
labeling is called FASTA format.  In this format, the string is
introduced by a line that begins with '>', followed by some labeling
information. Subsequent lines contain the string itself; the first
line to begin with '>' indicates the label of the next string.In
Rosalind's implementation, a string in FASTA format will be labeled by
the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between
0000 and 9999.

Given:
At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return:
The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of
0.001 in all decimal answers unless otherwise stated; please see the
note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC >Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""


import click
import os
import pyperclip

SAMPLE_DATASET = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""


def calc_gc_content(sequence):
    at = 0
    gc = 0
    for base in sequence:
        if base in "AT":
            at += 1
        else:
            gc += 1
    return gc / (at + gc) * 100


@click.command()
@click.argument("file_name", required=False, default=None)
def gc(file_name):
    """The main function

    Args:
        input_file: Takes the file path for the rosalind.info problem input
    Returns:
        void: Prints results to terminal, writes an answer.txt file,
        and also copies results to clipboard
    """

    dataset = ""
    result = ""

    # If a path to a input file is given, use that
    if file_name:
        with open(file_name, "r") as f:
            dataset = f.read()
            # dataset = dataset.replace('\n', '')

    # Else, run the script on the provided sample data
    else:
        dataset = SAMPLE_DATASET
    # May need to do additional dataset cleaning (for instance: newlines)
    # or parse into an ideal data structure for each respective problem.

    # BEGIN IMPLEMENTATION BELOW:

    # An array of parsed fasta structs
    graded_fastas = []

    # Partition and grade each fasta chunk
    for fasta in dataset.split('>')[1:]:
        fasta_struct = {}
        split_fasta = fasta.split('\n')
        fasta_struct['id'] = split_fasta[0]
        fasta_struct['sequence'] = ''.join(split_fasta[1:]).strip()
        fasta_struct['gc_content'] = calc_gc_content(fasta_struct['sequence'])
        graded_fastas.append(fasta_struct)

    # Sort and take the highest
    highest_gc_fasta = sorted(graded_fastas, key = lambda x: x['gc_content'])[-1]

    result = f"{highest_gc_fasta['id']}\n{highest_gc_fasta['gc_content']}"

    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(
        f'{os.path.dirname(os.path.abspath(__file__))}/answer.txt', 'w'
    ) as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    gc()
