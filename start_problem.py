"""start_problem.py

Alexander Craig
2022/02/22

Creates the templates and the neccesary file structure to start working on a
rosalind.info - Bioinformatics Armory problem.
"""

import click
import os
import requests
import textwrap
from bs4 import BeautifulSoup
from datetime import datetime


def string_formatter(output_str, indent=0):
    """String formatter to display python strings at 80 chars

    Args:
        output_str: String to format into block of wrapped 80 char width
        indent: An optional param to indent in the wrapped code block
    Returns:
        The output_str correctly formatted
    """
    temp = output_str.replace('\n', ' ')
    temp = textwrap.fill(temp, width=70)
    if indent > 0:
        temp = textwrap.indent(temp, indent * '    ')
    return temp


@click.command()
@click.argument('rosalind_id')
def start_problem(rosalind_id):
    """The main function

    Takes the rosalind problem ID and pulls down the problem text,
    transforming it into a structured file docstring in the solution file.

    Args:
        rosalind_id (str): The unique rosalind.info problem id

    Returns:
        void: Creates the file structures and templates, prints to terminal
    """

    rosalind_problem_url = f"https://rosalind.info/problems/{rosalind_id}/"

    r = requests.get(rosalind_problem_url)

    if r.status_code != 200:
        click.echo("Sorry I couldn't find the problem you were looking for.")

    # Begin parsing out response into text chunks:
    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.title.string

    problem_block = soup.find(class_="problem-statement")\
        .find(id="problem")\
        .find_next_siblings()

    problem_disc = ""
    problem_given = ""
    problem_return = ""
    sample_dataset = ""
    sample_output = ""

    idx_of_disc_end = None

    for i in range(len(problem_block)):
        # "Don't waste any effort"
        if not problem_block[i].get_text():
            continue

        if "Given:" in problem_block[i].get_text():
            # The "Given" portion of the problem block always comes directly
            # after the description regardless of its complexity.
            idx_of_disc_end = i
            problem_given = problem_block[i].get_text()
            # I'm pruning away the embedded "Given: " as to have more control
            # in the templating.
            problem_given = problem_given.partition("Given: ")[2]
            problem_given = string_formatter(problem_given)

        if "Return:" in problem_block[i].get_text():
            problem_return = problem_block[i].get_text()
            problem_return = problem_return.partition("Return: ")[2]
            problem_return = string_formatter(problem_return)

        if "Sample Dataset" in problem_block[i].get_text():
            sample_dataset = problem_block[i+1].get_text()
            sample_dataset = string_formatter(sample_dataset)

        if "Sample Output" in problem_block[i].get_text():
            sample_output = problem_block[i+1].get_text()
            sample_output = string_formatter(sample_output)

    problem_disc = ''.join(
        [i.get_text() for i in problem_block[:idx_of_disc_end]]
    )
    problem_disc = string_formatter(problem_disc)

    python_file = f"{rosalind_id}.py"
    start_timestamp = datetime.now().strftime("%Y-%m-%d")

    # Begin template creation:
    docstring_template = f"""\"\"\"{python_file}

Alexander Craig
{start_timestamp}

{title}

Problem:
{problem_disc}

Given:
{problem_given}

Return:
{problem_return}

Sample Dataset:
{sample_dataset}

Sample Output:
{sample_output}
\"\"\"


import click
import os
import pyperclip

SAMPLE_DATASET = \"{sample_dataset}\"


@click.command()
@click.argument("file_name", required=False, default=None)
def {rosalind_id}(file_name):
    \"\"\"The main function

    Args:
        input_file: Takes the file path for the rosalind.info problem input
    Returns:
        void: Prints results to terminal, writes an answer.txt file,
        and also copies results to clipboard
    \"\"\"

    str_dataset = ""
    result = ""

    # If a path to a input file is given, use that
    if file_name:
        with open(file_name, "r") as f:
            str_dataset = f.read()
            str_dataset = str_dataset.replace('\\n', '')

    # Else, run the script on the provided sample data
    else:
        str_dataset = SAMPLE_DATASET
    # May need to do additional dataset cleaning (for instance: newlines)
    # or parse into an ideal data structure for each respective problem.

    # BEGIN IMPLEMENTATION BELOW:


    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(f'{{os.path.dirname(__file__)}}/answer.txt', 'w') as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    {rosalind_id}()
"""

    if "problems" not in os.listdir(os.path.dirname(__file__)):
        os.mkdir("problems")

    # Create the problem directory if it doesn't exist
    if rosalind_id not in os.listdir(f"{os.path.dirname(__file__)}/problems/"):
        os.mkdir(f"{os.path.dirname(__file__)}/problems/{rosalind_id}/")

    # Write the template
    with open(
        f"{os.path.dirname(__file__)}/problems/{rosalind_id}/{rosalind_id}.py",
        'w'
    ) as f:
        f.write(docstring_template)

    click.echo(f"Directory and templates for {rosalind_id} have been created.")


if __name__ == "__main__":
    start_problem()
