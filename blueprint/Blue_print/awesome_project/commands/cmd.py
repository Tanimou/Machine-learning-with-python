"""Awesome project - machine-learning-production

Usage:
    awesome-project-cli lorem <iterations> [--text-size=<text_size>]
    awesome-project-cli data <data-url> <data-location>
    awesome-project-cli (-h | --help)

Arguments:
    <data-location>         Location to save the data file
    <data-url>              Location of the data file to download
    <iterations>            Number of times the text will be repeated

Options:
    --text-size=<text_size>    Lorem ipsum text size. [default: 50]
    -h --help                   Show this screen.
"""

from awesome_project.operator.data import get_data
from awesome_project.operator.generator import generate
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    if arguments['lorem']:
        print(generate(arguments['<iterations>'], arguments['--text-size']))
    elif arguments['data']:
        get_data(arguments['<data-url>'], arguments['<data-location>'])


if __name__ == '__main__':
    main()
