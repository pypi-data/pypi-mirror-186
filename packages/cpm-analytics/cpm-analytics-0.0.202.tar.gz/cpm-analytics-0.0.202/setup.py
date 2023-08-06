from pathlib import Path
from setuptools import setup

# package dependencies
dependencies = ["pandas==1.3.5",
                "matplotlib==3.5.0",
                "seaborn==0.11.2",
                # "plotly==5.1.0",
                "ppscore==1.3.0",
                "minepy==1.2.6",
                "feature-engine==1.4.0 ",
                "scikit-learn==1.1.1"
                ]

# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setup the package
setup(
    name='cpm-analytics',
    # packages=['src/cpm_analytics'],
    version='0.0.202',
    description='Investigate relationship on variables pairs in tabular datasets, based on Correlation, PPS and MIC scores.',
    author='Fernando Stefankevicius',
    author_email='fernando_doreto@hotmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=dependencies,
    setup_requires=['pytest-runner'],
)