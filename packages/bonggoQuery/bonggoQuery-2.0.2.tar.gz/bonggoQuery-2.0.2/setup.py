from sys import version
from setuptools import setup

with open("README.md","r") as rd:
    l_des = rd.read()

setup(
name = "bonggoQuery",
version = "2.0.2",
description ="This is the package that can help you to find some operations.",
long_description =l_des,
long_description_content_type="text/markdown",
url="https://github.com/SudipBera083",
author="Sudip Bera",
author_email="sudipbera083@gmail.com",
packages =['bonggoQuery'],
classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
            ],

install_requires =["wolframalpha","pyttsx3","SpeechRecognition","wikipedia"],
python_requires='>=3.6',
)