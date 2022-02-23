"""rna.py

Alexander Craig
2022-02-22

ROSALIND | Transcribing DNA into RNA

Problem:
An RNA string is a string formed from the alphabet containing 'A',
'C', 'G', and 'U'.Given a DNA string $t$ corresponding to a coding
strand, its transcribed RNA string $u$ is formed by replacing all
occurrences of 'T' in $t$ with 'U' in $u$.

Given:
A DNA string $t$ having length at most 1000 nt.

Return:
The transcribed RNA string of $t$.

Sample Dataset:
GATGGAACTTGACTACGTAAATT

Sample Output:
GAUGGAACUUGACUACGUAAAUU
"""


import click
import os
import pyperclip

SAMPLE_DATASET = "GATGGAACTTGACTACGTAAATT"


@click.command()
@click.argument("file_name", required=False, default=None)
def rna(file_name):
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
    result = str_dataset.replace('T', 'U')

    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(f'{os.path.dirname(__file__)}/answer.txt', 'w') as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    rna()
