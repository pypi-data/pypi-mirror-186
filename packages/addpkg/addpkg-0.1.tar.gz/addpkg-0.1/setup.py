from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Lorem ipsum..."

setup(
    name="addpkg",
    version=VERSION,
    author="Pierre BEJIAN",
    author_email="pierre.bejian@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy"],
    keywords=[],
    classifiers=[]
)
