from __future__ import print_function
import subprocess
import sys

def main(ctype):

    if ctype == "git":
        script_path = "git.sh"
    elif ctype == "start":
        print("TBD")

    process = subprocess.Popen(script_path, shell=True, stdout=subprocess.PIPE)



if __name__ == "__main__":

    if len(sys.argv) > 1:

        main(sys.argv[1])

    else:

        help_message = """Missing arg string like:\n
        git; for git push\n
        start; for start ."""

        print(help_message)
