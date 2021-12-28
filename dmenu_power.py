#!/bin/python3
"""Simple Dmenu Power Options Dialog"""
from subprocess import Popen, PIPE
import subprocess
import sys
CHOICE: str
choices = {
    "shutdown": "systemctl poweroff",
    "reboot": "systemctl reboot",
    "suspend": "systemctl suspend",
    "hybrid sleep": "systemctl hybrid-sleep",
    "hibernate": "systemctl hibernate",
    "lock": "xset s activate",
    "logout": "qtile cmd-obj -o cmd -f shutdown"
}
args = ["dmenu"]
args.extend(sys.argv[1:])
with (Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE) as p):
    CHOICE = p.communicate(input="\n".join(choices.keys()).encode())[
        0].decode().strip()
if CHOICE != '':
    subprocess.run(choices[CHOICE].split(), check=False)
