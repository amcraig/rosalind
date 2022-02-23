"""revc.py

Alexander Craig
2022-02-22

ROSALIND | Complementing a Strand of DNA

Problem:
In DNA strings, symbols 'A' and 'T' are complements of each other, as
are 'C' and 'G'.The reverse complement of a DNA string $s$ is the
string $s^{\textrm{c}}$ formed by reversing the symbols of $s$, then
taking the complement of each symbol (e.g., the reverse complement of
"GTCA" is "TGAC").

Given:
A DNA string $s$ of length at most 1000 bp.

Return:
The reverse complement $s^{\textrm{c}}$ of $s$.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""


import click
import os
import pyperclip

SAMPLE_DATASET = "AAAACCCGGT"


@click.command()
@click.argument("file_name", required=False, default=None)
def revc(file_name):
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
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    result = ''.join([complements[i] for i in str_dataset[::-1]])

    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(f'{os.path.dirname(__file__)}/answer.txt', 'w') as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    revc()
