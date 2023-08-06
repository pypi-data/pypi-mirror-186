# coding=utf8
""" Imports

Handles looking for and loading imports recursively
"""

__author__		= "Chris Nasr"
__copyright__	= "Ouroboros Coding Inc."
__version__		= "1.0.0"
__email__		= "chris@ouroboroscoding.com"
__created__		= "2021-06-05"

# Python imports
import ast
import os

# Local imports
from . import output

def exists(name, folder=None):
	"""Exists

	Checks if a given import name exists as a local file. If it does, a string
	with the filename is returned, else False

	Arguments:
		name (str): The name of the import to check

	Returns
		bool|str
	"""

	# If we have a local folder and it doesn't end in /
	if folder and folder[-1:] != '/':
		folder = '%s/' % folder

	# Init the parts
	lParts = []

	# If we have a name
	if name:

		# Init the . count
		iDots = 0
		while name[iDots] == '.':
			iDots += 1

		# Add .. folders for each dot (we ignore the first one)
		for i in range(1, iDots):
			lParts.append('..')

		# Split the name by .
		lParts.extend(name.lstrip('.').split('.'))

	# While we have a count to the parts
	while len(lParts):

		# Generate the project filename
		sFile = '%s.py' % '/'.join(lParts)

		# Does it exist locally from the parent?
		if folder:

			# Generate the local filename
			sLocalFile = '%s%s' % (folder, sFile)

			# Does the file exist in it
			if os.path.exists(sLocalFile):
				return sLocalFile

		# Does it exist off the project
		if os.path.exists(sFile):
			return sFile

		# Does it exist as an __init__?
		sInit = '%s/__init__.py' % '/'.join(lParts)
		if os.path.exists(sInit):
			return sInit

		# Still doesn't exist? Let's take a piece off the parts and try again
		lParts = lParts[0:-1]

	# Nothing found, return False
	return False

def find(file, file_list):
	"""Find

	Looks through the file for import statements and if the files are local,
	adds them to the list

	Arguments:
		file (str): The name of the file to open and parse looking for imports
		file_list (list): The unique list of existing files as well as where new
							files will be added

	Returns:
		None
	"""

	# Open the file
	with open(file) as oF:

		# Get the abstract syntax tree for the file
		try:
			oAST = ast.parse(oF.read(), file)

			# Go through each node in the tree
			for oNode in ast.iter_child_nodes(oAST):

				# If the instance is an import
				if isinstance(oNode, ast.Import):

					# Go through each name found
					for oName in oNode.names:

						# Look for a file
						mFile = exists(oName.name, os.path.dirname(file))

						# If the file exists
						if mFile:

							# If it doesn't exist already in the list
							if mFile not in file_list:

								# Add it
								file_list.append(mFile)

								# And recurse
								find(mFile, file_list)

				# If the instance is a from
				elif isinstance(oNode, ast.ImportFrom):

					# If there's no module
					if not oNode.module:
						mFile = exists('__init__', os.path.dirname(file))
					else:
						mFile = exists(oNode.module, os.path.dirname(file))

					# If the file exists
					if mFile:

						# If it doesn't exist already in the list
						if mFile not in file_list:

							# Add it
							file_list.append(mFile)

							# And recurse
							find(mFile, file_list)

					# Go through each name found
					for oName in oNode.names:

						# Look for a file
						mFile = exists(
							'%s.%s' % (oNode.module is not None and oNode.module or '', oName.name),
							os.path.dirname(file)
						)

						# If the file exists
						if mFile:

							# If it doesn't exist already in the list
							if mFile not in file_list:

								# Add it
								file_list.append(mFile)

								# And recurse
								find(mFile, file_list)

		# Catch syntax errors from broken code
		except SyntaxError as e:
			output.error('Syntax Error parsing "%s" at line %d, column %d\n' % (
				file,
				e.args[1][1],
				e.args[1][2]
			))
