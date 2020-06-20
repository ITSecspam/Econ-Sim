#!/bin/python3
"""An economy game"""

#Import modules
import os
import sys
import argparse
import core

#Set up the arguments
parser = argparse.ArgumentParser(description='Parses the Arguments, what did you expect?')
parser.add_argument('--loadfrom', metavar='SAVEFILE', help='The Savefile to load from', required=False)
args = parser.parse_args()
#Generate starting interface
print("Hello {}, welcome to econ-sim".format(os.getenv('USER')))

UserInput = None
AnswerGiven = False
while not AnswerGiven and args.loadfrom == None:
    UserInput = input("Do you want to start a new company [Y/N]:")
    if UserInput == 'Y' or UserInput == 'y':
        AnswerGive = True
        Worldname = input("Please enter the world name: ")
        Companyname = input("PLease enter your companies name: ")
        GameWorld = core.world(Worldname, Companyname)
        break
    elif UserInput == 'N' or UserInput == 'n':
        print('Stopping the program, for more info use the arg --help')
        sys.exit()

if args.loadfrom != None:
    try:
        company = core.load_from_savefile(args.loadfrom)
    except (TypeError, ValueError, RuntimeError, IOError):
        print('Please specify a valid filepath or other error, QUITTING!')
        sys.exit()
print(GameWorld)
