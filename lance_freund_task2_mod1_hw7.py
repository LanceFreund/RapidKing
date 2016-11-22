#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys

def inputGet():
    print("Enter a zipcode: ")
    usrin = input()
    if len(usrin) != 5:
        print("ERROR!!!  A zip is 5 digits long:")
    elif usrin.isdigit() == False:
        print("ERROR!!! A zip code is only digits:")
    else:
        return usrin



def printDigit(x):
    var = []
    for i in x:
        #var.append(i)
        if i == '9':
            print("|:|::")
        elif i == '8':
            print("|::|:")
        elif i == '7':
            print("|:::|")


def main():
    """
    This main() function calls 
    the stack of functions in
    there orders.
    """

    usrin = inputGet()
    printDigit(usrin)


if __name__ == '__main__':
    main()

    exit(0)
