from setuptools import setup

with open('README.md', 'r') as oF:
	long_description=oF.read()

setup(
	name='pylivedev',
	version='1.1.0',
	description='PyLiveDev is used to keep track of files associated with your script so it can be re-started if any file is updated.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://ouroboroscoding.com/pylivedev',
	project_urls={
		'Source': 'https://github.com/ouroboroscoding/pylivedev',
		'Tracker': 'https://github.com/ouroboroscoding/pylivedev/issues'
	},
	keywords=['python','live', 'development'],
	author='Chris Nasr - OuroborosCoding',
	author_email='chris@ouroboroscoding.com',
	license='Apache-2.0',
	packages=['pylivedev'],
	install_requires=[
		'termcolor>=1.1.0',
		'watchdog>=2.1.2'
	],
	entry_points={
		'console_scripts': ['pylivedev=pylivedev.__main__:cli']
	},
	zip_safe=True
)
