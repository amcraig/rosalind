"""fib.py

Alexander Craig
2022-02-23

ROSALIND | Rabbits and Recurrence Relations

Problem:
A sequence is an ordered collection of objects (usually numbers),
which are allowed to repeat.  Sequences can be finite or infinite. Two
examples are the finite sequence $(\pi, -\sqrt{2}, 0, \pi)$ and the
infinite sequence of odd numbers $(1, 3, 5, 7, 9, \ldots)$.  We use
the notation $a_n$ to represent the $n$-th term of a sequence.A
recurrence relation is a way of defining the terms of a sequence with
respect to the values of previous terms.  In the case of Fibonacci's
rabbits from the introduction, any given month will contain the
rabbits that were alive the previous month, plus any new offspring. A
key observation is that the number of offspring in any month is equal
to the number of rabbits that were alive two months prior.  As a
result, if $F_n$ represents the number of rabbit pairs alive after the
$n$-th month, then we obtain the Fibonacci sequence having terms $F_n$
that are defined by the recurrence relation $F_{n} = F_{n-1} +
F_{n-2}$ (with $F_1 = F_2 = 1$ to initiate the sequence).  Although
the sequence bears Fibonacci's name, it was known to Indian
mathematicians over two millennia ago.When finding the $n$-th term of
a sequence defined by a recurrence relation, we can simply use the
recurrence relation to generate terms for progressively larger values
of $n$. This problem introduces us to the computational technique of
dynamic programming, which successively builds up solutions by using
the answers to smaller cases.

Given:
Positive integers $n \leq 40$ and $k \leq 5$.

Return:
The total number of rabbit pairs that will be present after $n$
months, if we begin with 1 pair and in each generation, every pair of
reproduction-age rabbits produces a litter of $k$ rabbit pairs
(instead of only 1 pair).

Sample Dataset:
5 3

Sample Output:
19
"""


import click
import os
import pyperclip

SAMPLE_DATASET = "5 3"

# Memo for recursive relations speedup.
memo = {}


def rec_relation(n, k):
    """ A function illustrating the reccurence relation at place

    Args:
        n: number of months
        k: number of pairs of offspring in each litter
    Return:
        An integer of the total population pairs of rabbits
    """

    if n <= 2:
        return 1

    if n in memo.keys():
        return memo[n]

    ans = rec_relation(n-1, k) + k * rec_relation(n-2, k)
    memo[n] = ans
    return ans


@click.command()
@click.argument("file_name", required=False, default=None)
def fib(file_name):
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
            dataset = dataset.replace('\n', '')

    # Else, run the script on the provided sample data
    else:
        dataset = SAMPLE_DATASET
    # May need to do additional dataset cleaning (for instance: newlines)
    # or parse into an ideal data structure for each respective problem.

    # BEGIN IMPLEMENTATION BELOW:

    # n - number of months
    n = int(dataset.partition(" ")[0])

    # k - constant number of rabbit babies in litter
    k = int(dataset.partition(" ")[2])

    result = str(rec_relation(n, k))

    # Prints result to terminal, writes to answer.txt, and copies to clipboard
    # for ease of evaluation on rosalind.info

    click.echo(result)
    with open(
        f'{os.path.dirname(os.path.abspath(__file__))}/answer.txt', 'w'
    ) as f:
        f.write(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    fib()
