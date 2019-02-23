import sys
import twint
import time, os
import networkx as nx

print("You have chosen the user",sys.argv[1],"as the root \n" )

username = sys.argv[1]

# A function that makes a breadth_first analysis on a twitter user
# first make a list of nodes
def main(root):
    #collet the initial followers of root
    followers_collect(root)


def deleteContent(filename):
    """delte the contents of the file"""
    with open(filename, "w"):
        pass

def followers_collect(username):
    tempfilename='temp.csv'

    # Configure
    c = twint.Config()
    c.Search = "#dkpol"
    c.Store_csv = True
    c.Output = tempfilename
    c.Format = "{tweet}"
    c.Since = "2010-01-01"

    #flush tempfile
    deleteContent(tempfilename)
    twint.run.Search(c)


def deleteContent(filename):
    """delte the contents of the file"""
    with open(filename, "w"):
        pass

def collect_followers(username,limit):
    import twint
    tempfilename='temp.csv'

    # Configure
    c = twint.Config()
    c.Search = "#dkpol"
    c.Store_csv = True
    c.Output = tempfilename
    c.Format = "{tweet}"
    c.Since = "2010-01-01"

    #flush tempfile
    deleteContent(tempfilename)
    twint.run.Search(c)

main(username)
