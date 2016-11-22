#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys

def inputGet():
    """
    This function acts as an aid to test
    mod1 by providing a way to input values
    manually so the conditions in doorCheck()
    can be initially tested.
    """

    global LD
    LD = input("Left Dashboard switch (1/0) ?")
    print ("L.D. Swich = " + LD)
    print (" ")

    global RD
    RD = input("Right Dashboard switch (1/0) ?")
    print ("R.D. Swich = " + RD)
    print (" ")

    global CL
    CL = input("Child Lock switch (1/0) ?")
    print ("C.L. Swich = " + CL)
    print (" ")

    global ML
    ML = input("Master Unlock switch (1/0) ?")
    print ("M.L. Swich = " + ML)
    print (" ")

    global LI
    LI = input("Left Inside switch (1/0) ?")
    print ("L.I. Swich = " + LI)
    print (" ")

    global LO
    LO = input("Left Outside switch (1/0) ?")
    print ("L.O. Swich = " + LO)
    print (" ")

    global RI
    RI = input("Right Inside switch (1/0) ?")
    print ("R.I. Swich = " + RI)
    print (" ")

    global RO
    RO = input("Right Outside switch (1/0) ?")
    print ("R.O. Swich = " + RO)
    print (" ")

    global GS
    GS = input("Gear shift Position (P,N,D,1,2,3, or R) ?")
    print ("G.S. Swich = " + GS)
    print (" ")

    #return LD, RD, CL, ML, LI, LO, RI, RO, GS

def doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS):
    """
    This funciton accepts nine arguments and verifyies
    the conditions that are needed for the doors to
    open or remian closed.

    It also provides some error correction for the
    GS variable to ensure that only a valid gearshift
    option exists.
    """
    print("Left dashboard switch (0 or 1): ", LD)
    print("Right dashboard switch (0 or 1): ", RD)
    print("Child lock switch (0 or 1): ", CL)
    print("Master unlock switch (0 or 1): ", ML)
    print("Left inside handle (0 or 1): ", LI)
    print("Left outside handle (0 or 1): ", LO)
    print("Right inside handle (0 or 1): ", RI)
    print("Right outside handle (0 or 1): ", RO)
    print("Gear shift position (0 or 1): ", GS)
    print()

    if GS not in {'P', 'N', 'D', '1', '2', '3', 'R'}:
        print("Invalid Record: Both doors stay closed.")
        print(" ")
    else:
     
        if CL == '1' or ML == '0' or GS != 'P':
            print("Both doors stay closed.")
            print(" ")

        elif LD == '1' or LI == '1' or LO == '1':
            if RD == '0' or RI == '0' or RO == '0':
                print("Left door opens")
                print(" ")

        elif (RD == '1' or RI == '1' or RO == '1') and (LD == '0' or LI == '0' or LO == '0'):
            print("Right door opens")
            print(" ")

        elif RD == '1' or RI == '1' or RO == '1':
            if LD == '1' or LI == '1' or LO == '1':
                print("Both doors open.")
                print(" ")
        elif (RD == '0' or RI == '0' or RO == '0') and (LD == '0' or LI == '0' or LO == '0'):
            print("Both doors stay closed.")
            print(" ")
        

def main():
    inputGet()
    doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS)


if __name__ == '__main__':
    main()

    exit(0)
