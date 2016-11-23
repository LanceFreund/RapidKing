#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys

def inputGet():
    """
    This function allows for user input
    so the user can provide a zipcode manually
    **This is very handy for testing purposes.
    """
    while True:
        print("Enter a zipcode: ")
        usrin = input()
        if len(usrin) != 5:
            print("ERROR!!!  A zip is 5 digits long:")
            #inputGet()
            main()
        elif usrin.isdigit() == False:
            print("ERROR!!! A zip code is only digits:")
        else:
            return usrin


def check_digit(k):
    """
    This function accepts a zipcode as parameter and
    caluclates the value of the checkdigit. Once
    calculated the function provides the pattern for
    the value and returns it.
    """
    chdig = 0
    digit0 = k[0]
    digit1 = k[1]
    digit2 = k[2]
    digit3 = k[3]
    digit4 = k[4]
    total = int(digit0) + int(digit1) + int(digit2) + int(digit3) + int(digit4)

    if total < 50 and total > 39:
        chdig = 50 - total
    elif total < 40 and total > 29:
        chdig = 40 - total
    elif total < 30 and total > 19:
        chdig = 30 - total
    elif total < 20 and total > 9:
        chdig = 20 - total
    else:
        chdig = 10 - total
    if chdig == '9':
        j = "|:|::"
    elif chdig == '8':
        j = "|::|:"
    elif chdig == '7':
        j = "|:::|"
    elif chdig == '6':
        j = ":||::"
    elif chdig == '5':
        j = ":|:|:"
    elif chdig == '4':
        j = ":|::|"
    elif chdig == '3':
        j = "::||:"
    elif chdig == '2':
        j = "::|:|"
        return j


def printBarCode(var):
    print('|'+var[0]+var[1]+var[2]+var[3]+var[4]+var[5]+'|')


def printDigit(x):
    """
    This function accepts input in the form of
    a zipcode and sets the pattern for 5 digits
    that are contained within the zipcode.
        - Calls check_digit() and provides the
        zipcode as a perameter and then appends
        the returned value to var[]
        - Calls printBarCode and passes it the
        zipcode to return the check digit pattern
    """
    var = []
    for i in x:
        if i == '9':
            j = "|:|::"
            var.append(j)
        elif i == '8':
            j = "|::|:"
            var.append(j)
        elif i == '7':
            j = "|:::|"
            var.append(j)
        elif i == '6':
            j = ":||::"
            var.append(j)
        elif i == '5':
            j = ":|:|:"
            var.append(j)
        elif i == '4':
            j = ":|::|"
            var.append(j)
        elif i == '3':
            j = "::||:"
            var.append(j)
        elif i == '2':
            j = "::|:|"
            var.append(j)
        elif i == '1':
            j = ":::||"
            var.append(j)
        else:
            j = "||:::"
            var.append(j)
    cd = check_digit(x)
    var.append(j)
    printBarCode(var)


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
