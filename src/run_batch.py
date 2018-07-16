from __future__ import print_function
import subprocess
import sys

def main(ctype,msg):

    if ctype == "git":
        script_path = "git.sh"
    elif ctype == "start":
        script_path = "start.sh"

    print("path", script_path)#
    process = subprocess.Popen([script_path, msg], shell=True, stdout=subprocess.PIPE)



if __name__ == "__main__":

    if len(sys.argv) > 1:
        command_type = sys.argv[1]
        message = sys.argv[2] if len(sys.argv)>2 else "qxt changes"
        main(command_type, message)

    else:

        help_message = """Missing arg string like:\n
        git; for git push\n
        start; for start ."""

        print(help_message)
