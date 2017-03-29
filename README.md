# infoscience-parser > README

## Overview

### What is this repository for?

This repository contains a parser for the Infoscience API of the EPFL. It creates Python objects representing publications and authors.  

### How do I get set up? ###

Just make sure you have python 2.7 or python 3 on your compouter, and run the script.

```
$ python parser.py -h
usage: parser.py [-h] [--display-records] [--debug] [--quiet] URL

Parse result from request on Infoscience

positional arguments:
  URL                The URL where to make the request

optional arguments:
  -h, --help         show this help message and exit
  --display-records  Print records fetched
  --debug            Set logging level to DEBUG (default is INFO)
  --quiet            Set logging level to WARNING (default is INFO)
 ```

 the URL is one of the Infoscience API

 
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017