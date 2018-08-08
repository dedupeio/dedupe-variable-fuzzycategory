try:
    from setuptools import setup
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-fuzzycategory',
    url='https://github.com/datamade/dedupe-variables-fuzzycategory',
    version='0.0.1',
    description='Fuzzy Categoy variable type for dedupe',
    packages=['dedupe.variables'],
    install_requires=['dedupe', 
	              'fuzzycategory>=0.0.4', 
                      'future'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )
