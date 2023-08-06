from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='negpipi_ceu',
    version='0.0.1',
    license='MIT License',
    author='Sidemar',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='sidmar.88@hotmail.com',
    keywords='neceu',
    description=u'isso é apenas um teste',
    packages=['negpipi_ceu'],)