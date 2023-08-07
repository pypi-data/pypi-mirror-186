from setuptools import setup
import sys , glob

setup(
    name='movie-search-lib',
    version='0.1.9',
    author='Jay Deiman',
    author_email='admin@splitstreams.com',
    url='',
    description='Get results of movie searches',
    long_description='',
    packages=['libms'],
    install_requires=['six>=1.10.0'],
    classifiers=[
        'Development Status :: 4 - Beta' ,
        'Environment :: Console' ,
        'Intended Audience :: System Administrators' ,
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)' ,
        'Natural Language :: English' ,
        'Topic :: Internet :: Name Service (DNS)' ,
        'Operating System :: POSIX' ,
        'Programming Language :: Python' ,
        'Topic :: System :: Systems Administration' ,
    ]
)

