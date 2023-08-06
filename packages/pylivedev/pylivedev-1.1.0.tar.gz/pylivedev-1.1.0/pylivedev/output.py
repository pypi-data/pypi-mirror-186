# coding=utf8
""" Output

Output methods
"""

__author__		= "Chris Nasr"
__copyright__	= "Ouroboros Coding Inc."
__version__		= "1.0.0"
__email__		= "chris@ouroboroscoding.com"
__created__		= "2022-03-03"

# Python imports
import sys

# Pip imports
from termcolor import colored

def error(msg):
	"""Error

	Print bold red text to stderr

	Arguments:
		msg (str): The message to print

	Returns:
		None
	"""
	sys.stderr.write(
		colored(
			msg,
			color='red',
			attrs=['bold']
		)
	)

def color(color_, msg):
	"""Color

	Prints bold messages in a specific color

	Arguments:

		arg (str): The message to print

	Returns:
		None
	"""
	sys.stdout.write(
		colored(
			msg,
			color=color_,
			attrs=['bold']
		)
	)

def verbose(msg):
	"""Verbose

	Print bold white text to stdout

	Arguments
		msg (str): The message to print

	Returns:
		None
	"""
	sys.stdout.write(
		colored(
			msg,
			color='white',
			attrs=['bold']
		)
	)
