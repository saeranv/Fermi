# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

def print_progress(iteration, total, prefix='', suffix='', bar_length=50):
    """
    This is a modified version from:
    https://gist.github.com/aubricus/f91fb55dc6ba5557fbab06119420dd6a
    https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/34325723#34325723

    Call in a loop to create terminal progress bar
        iteration   - Required  : current iteration (int)
        total       - Required  : total iterations (int)
        prefix      - Optional  : prefix string (str)
        suffix      - Optional  : suffix string (str)
        bar_length  - Optional  : character length of bar (int)
    """

    str_format = "{0:." + str(1) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '|' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write("\r{} |{}| {}{} {}".format(prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')

    sys.stdout.flush()


if __name__ == "__main__":
    from time import sleep

    # A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)

    # Sample Output
    #Progress: |█████████████████████████████████████████████-----| 90.0% Complete
