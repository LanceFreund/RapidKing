#!usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys
from urllib.request import urlopen
from lance_freund_task2_mod1_hw7 import printDigit

def fileup():
    """
    This function captures the data from 
    "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    and passes it into printDigit() that is imported
    from lance_freund_task2_mod1_hw7
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt") as rfile:
        perams = []
        for i in rfile:
            line = i.decode('utf-8')
            print(line)
            printDigit(line)


def main():
    fileup()

if __name__ == '__main__':
    main()
    
    exit(0)
