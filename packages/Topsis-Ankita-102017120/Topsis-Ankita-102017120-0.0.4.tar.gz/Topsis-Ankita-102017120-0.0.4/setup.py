from setuptools import setup, find_packages
import codecs
import os

# with open("README.md", "r", encoding = "utf-8") as fh:
#     long_description = fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Topsis-Ankita-102017120 is a Python library for handling problems related to Multiple Criteria Decision Making(MCDM)'

# Setting up
setup(
    name="Topsis-Ankita-102017120",
    version=VERSION,
    license='MIT',
    author="Ankita Sharma",
    author_email="<ankitasharma102002@gmail.com>",
    description=DESCRIPTION,
    # long_description=long_description,
    # long_description_content_type="text/markdown"
    packages=find_packages(),
    keywords=['Topsis', 'MCDM'],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
         'Programming Language :: Python :: 3.4',
         'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)