# coding=utf8
""" CLI

Used for shim to run the program from the command line
"""

from __future__ import print_function

__author__		= "Chris Nasr"
__copyright__	= "Ouroboros Coding Inc."
__version__		= "1.0.0"
__email__		= "chris@ouroboroscoding.com"
__created__		= "2022-02-24"

# Python imports
from argparse import ArgumentParser
import json
import sys

# Local imports
from . import main

def cli():
	"""CLI

	Called from the command line to load a config file and run pylivedev

	Returns:
		uint
	"""

	# Setup the argument parser
	oArgParser = ArgumentParser(description='Python Live Development')
	oArgParser.add_argument('-c', '--config', nargs=1, default='.pylivedev', help='The configuration file to load')

	# Parse the arguments
	mArgs = oArgParser.parse_args()

	# Attempt to load the config file
	try:
		with open(mArgs.config, 'r') as oF:

			# If it's opened, decode the JSON inside
			oConf = json.load(oF)

			# Pass the JSON to the module and close with whatever status it returns
			sys.exit(
				main(oConf) == False and 1 or 0
			)

	except IOError as e:
		print(e)

# Only run if main
if __name__ == '__main__':
	cli()
