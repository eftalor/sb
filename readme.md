# Overview

This is a python and docker based mini application which will accept text files and will output the most common words in each of the text files

# Rational
I have decided to keep things simple as possible while still maitaining some flexability

The applications is wrapped in docker-compose with a docker file.

For the logic of the script itself I have decided to make the loading of files seamless, so the script takes the 4 latest files in the directory and than processes them.

# How it works
A. One must clone this repository
B. Uses docker and docker-compose to run the application
C. Application is based on a Python 3.8 publicly available image
D. One invokes docker build which builds and run the application, and the output of the script is outputed to the screen

# How to run
## Prerequesits

In order to run the application you will need to have *docker* and *docker-compose* installed on your machine.

## how to run
docker-compose up --build
