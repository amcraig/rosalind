"""start_problem.py

Alexander Craig
2022/02/22

Creates the templates and the neccesary file structure to start working on a
rosalind.info - Bioinformatics Armory problem.

It takes one CLI argument -- the rosalind problem ID and pulls down the problem
text, transforming it into a structured file docstring in the solution file.

Args:
    rosalind_id (str): The unique rosalind.info problem id

Returns:
    void: Creates the file structures and templates, prints to terminal
"""

import click
from matplotlib.pyplot import text
import requests
import textwrap
from bs4 import BeautifulSoup
from datetime import datetime

def sanitize_output(output):
    temp = output.replace('\n', ' ')
    temp = textwrap.fill(temp, width=80)
    return textwrap.indent(temp, '    ')


@click.command()
@click.argument('rosalind_id')
def start_problem(rosalind_id):

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
            problem_given = sanitize_output(problem_given)

        if "Return:" in problem_block[i].get_text():
            problem_return = problem_block[i].get_text()
            problem_return = problem_return.partition("Return: ")[2]
            problem_return = sanitize_output(problem_return)

        if "Sample Dataset" in problem_block[i].get_text():
            sample_dataset = problem_block[i+1].get_text()
            sample_dataset = sanitize_output(sample_dataset)

        if "Sample Output" in problem_block[i].get_text():
            sample_output = problem_block[i+1].get_text()
            sample_output = sanitize_output(sample_output)

    problem_disc = ''.join(
        [i.get_text() for i in problem_block[:idx_of_disc_end]]
    )
    problem_disc = sanitize_output(problem_disc)

    python_file = f"{rosalind_id}.py"
    start_timestamp = datetime.now().strftime("%Y-%m-%d")

    docstring_template = f"""{python_file}

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

    Args:

    Returns:

    """

    click.echo(docstring_template)


if __name__ == "__main__":
    start_problem()