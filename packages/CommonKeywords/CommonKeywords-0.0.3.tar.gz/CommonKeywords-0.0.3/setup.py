""" common keywords library """
from setuptools import setup, find_packages


VERSION = '0.0.3'
DESCRIPTION = 'CommonKeywords'
LONG_DESCRIPTION = 'A package for common methods'

# Setting up
setup(
    name="CommonKeywords",
    version=VERSION,
    author="Ritika",
    author_email="ritika.kumar90@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'CommonKeywords', 'mathematics', 'python tutorial', 'Ritika kumar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)
