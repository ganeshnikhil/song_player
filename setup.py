from setuptools import setup, find_packages
setup(
    name='music player',
    version='1.0.0',
    description='it is simple terminal based music player',
    author='gaensh nikhil',
    author_email='ganeshnikhil124@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pynput',
        'pygame',
        'mutagen'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
