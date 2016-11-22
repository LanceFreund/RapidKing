#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys
from urllib.request import urlopen
import mod1



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

        """        
                LD = perams[1]
                RD = perams[3]
                CL = perams[5]
                ML = perams[7]
                LI = perams[9]
                LO = perams[11]
                RI = perams[13]
                RO = perams[15]
                GS = perams[17]

        """

def list_prep(perams):
    newList = []
    for i in perams:
        newList.append(i.split())
    for i in newList:
        #print(len(i))
        #for x in i:     

        #print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])

        LD = i[0]
        RD = i[1]
        CL = i[2]
        ML = i[3]
        LI = i[4]
        LO = i[5]
        RI = i[6]
        RO = i[7]
        GS = i[8]
        mod1.doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS)


def main():
    perams = fileup()
    list_prep(perams)



if __name__ == '__main__':
     main()

exit(0)
