from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A command line tool to perform TOPSIS, a multi-criteria decision making technique'

with open("README.md", "r") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="Topsis-Amrita-102017017",
    version=VERSION,
    author="Amrita Bhatia",
    author_email="<nonie.bhatia@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis=src.topsis:main'
        ]
    },
    keywords=['python', 'TOPSIS', 'MCDM', 'MCDA', 'statistics', 'prescriptive analytics', 'cli'],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5'
)