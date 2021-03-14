# import unittest
import os

def grep_start(x):

    os.system('/bin/grep' + x)
    #list_files = subprocess.run([" ", x])
    #print("The exit code was: %d" % list_files)

    return 1


def test_answer():
    grep_parameters = ' --help'
    print("\nstart grep")
    print("\nCMD: grep" + grep_parameters)
    assert grep_start(grep_parameters) == 1
