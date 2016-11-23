#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys
from urllib.request import urlopen
import burak_deniz_task1_mod1_hw7



def fileup():

    #mod1.doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS)
    
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as rfile:


        perams = []
        for i in rfile:
            line = i.decode('utf-8')
            #data_clean = (line.split())
 
            if line[0] is "R":
                line = line.replace(",","" )
                line = line.strip('R1')
                line = line.strip('\n')
                perams.append(line)
        return perams


def list_prep(perams):
    x = 1
    newList = []
    for i in perams:
        newList.append(i.split())
    for i in newList:
        LD = i[0]
        RD = i[1]
        CL = i[2]
        ML = i[3]
        LI = i[4]
        LO = i[5]
        RI = i[6]
        RO = i[7]
        GS = i[8]
        print("Reading Record: ", x)
        burak_deniz_task1_mod1_hw7.doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS)
        x+=1


def main():
    perams = fileup()
    list_prep(perams)



if __name__ == '__main__':
     main()

exit(0)
