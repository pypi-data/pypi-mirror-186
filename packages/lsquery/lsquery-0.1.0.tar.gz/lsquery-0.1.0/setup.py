from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lsquery',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'asyncio==3.4.3',
        'docker==6.0.1',
        'opengsq==1.4.3',
        'python-decouple==3.6',
        'pytz==2022.6',
        'websocket-client==1.4.2',
        'websockets==10.4',
    ],
    url='https://lanslide.com.au',
    license='GNU GPL',
    author='Brendon Taylor',
    author_email='nuke@lanslide.com.au',
    description='The project is used to spin up docker game servers',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
