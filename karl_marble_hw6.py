#!/usr/bin/env python3
import sys
from urllib.request import urlopen
import re
import operator


def top_errors(file):
    """
    Opens an Apache server error log file and finds the top 25 errors.
    Args:
        file: input file
    Returns:
        top 25 error counts and their page
    """
    err_dict = {}
    log_data = urlopen(file)
    m = re.compile(r"(/[\w.~]+){1,10}")

    # parse through the provided url line by line while changing the lines from byte code into strings
    # search the strings for a list of values
    for line in log_data:
        sline = line.decode("utf-8")
    # check for the word error in the list values
        if "error" in sline:
            sp_line = m.search(sline)
            if sp_line is not None:
                err = sp_line.group()
    # if there is an error and it isn't in the dictionary already add it
    # if it is then increment it
                if not err in err_dict:
                    err_dict[err] = 1
                else:
                    err_dict[err] += 1

    # sort dict into
    sort_err_dict = sorted(err_dict.items(), key=operator.itemgetter(1), reverse=True)

    # print list
    for k, v in sort_err_dict[:25]:
        print("Count: ", v,"    Page: ", k)

def help():
    """
    Displays usage text.
    """
    print("usage is: ./karl_marble_hw6.py <url of input file> ")


#main function
def main():
    """
    Test function
    """
    if len(sys.argv) > 1:
        file = sys.argv[1]
        top_errors(file)
    else:
        help()
    
if __name__ == "__main__":
    #Call Main
    main()

    exit(0)

