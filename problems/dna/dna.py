"""dna.py

Alexander Craig
2022-02-22

ROSALIND | Counting DNA Nucleotides

Problem:
A string is simply an ordered collection of symbols selected from some
alphabet and formed into a word; the length of a string is the number
of symbols that it contains.An example of a length 21 DNA string
(whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is
"ATGCTTCAGAAAGGTCTTACG."

Given:
A DNA string $s$ of length at most 1000 nt.

Return:
Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in $s$.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
"""


import click
import os
import pyperclip

SAMPLE_DATASET = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


@click.command()
@click.argument("file_name", required=False, default=None)
def dna(file_name):
    """The main function

    Args:
        input_file: Takes the file path for the rosalind.info problem input
    Returns:
        void: Prints results to terminal, writes an answer.txt file,
        and also copies results to clipboard
    """

    str_dataset = ""
    result = ""

    # If a path to a input file is given, use that
    if file_name:
        with open(file_name, "r") as f:
            str_dataset = f.read()
            str_dataset = str_dataset.replace('\n', '')

    # Else, run the script on the provided sample data
    else:
        str_dataset = SAMPLE_DATASET
    # May need to do additional dataset cleaning (for instance: newlines)
    # or parse into an ideal data structure for each respective problem.

    # BEGIN IMPLEMENTATION BELOW:
    base_counts = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for base in str_dataset:
        base_counts[base] += 1

    result = f"{base_counts['A']} {base_counts['C']} {base_counts['G']} {base_counts['T']}"

    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/answer.txt', 'w') as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    dna()
