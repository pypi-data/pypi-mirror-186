from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'MathU Smart Pathways package'
LONG_DESCRIPTION = 'MathU Smart Pathways package which generates an array of pathway questions to be passed to Platypus'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="smartpathways", 
        version=VERSION,
        author="Luca Lohrentz",
        author_email="<luca@mathu.co.za>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)