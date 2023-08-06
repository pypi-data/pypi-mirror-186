from setuptools import setup

setup(
	name='biorosetta',
	version='0.1.2',
	packages=[''],
	url='https://github.com/reemagit/biorosetta',
	author='Enrico Maiorino',
	author_email='enrico.maiorino@gmail.com',
	description='A package to convert gene names between different naming conventions',
    install_requires=['biothings_client','tqdm','pandas']
)
