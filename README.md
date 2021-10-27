# Gendiff
[![Actions Status](https://github.com/IDilettant/gendiff/workflows/hexlet-check/badge.svg)](https://github.com/IDilettant/gendiff/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7ca7a58ae374ae5ab91b/maintainability)](https://codeclimate.com/github/IDilettant/gendiff/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7ca7a58ae374ae5ab91b/test_coverage)](https://codeclimate.com/github/IDilettant/gendiff/test_coverage)
![Actions Status](https://github.com/IDilettant/gendiff/workflows/tests%20and%20lints/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Description

Gendiff (GENerator of DIFFerences) - a program defining the difference between two data structures (JSON and/or YAML)
and generating new structure containing differences details (including unchanged).

This is the second project implemented for educational purposes in the learning process
on [the Hexlet](https://ru.hexlet.io) study platform


## Features

- Supported input formats: YAML, JSON
- Report generation as plain text, structured text and JSON
- Usage as CLI util or library function


## Quickstart
```bash
pip install git+https://github.com/IDilettant/python-project-lvl2.git
```


## Usage

### As library function

```python
from gendiff import generate_diff

diff = generate_diff(first_file_path, second_file_path, formatter)
```

### As CLI utility

```bash
$ gendiff -h
usage: gendiff [-h] [-f {json,plain,stylish}] first_file second_file

Generate difference of two JSON or YAML files.

positional arguments:
  first_file            first file to compare
  second_file           second file to compare

optional arguments:
  -h, --help            show this help message and exit
  -f {json,plain,stylish}, --format {json,plain,stylish}
                        set output format (default: 'stylish')
```


## Usage examples


#### Stylish formatter output (-f stylish):
[![asciicast](https://asciinema.org/a/1J2DoAfr6nR1iwtf32DiCXm92.svg)](https://asciinema.org/a/1J2DoAfr6nR1iwtf32DiCXm92)

#### Plain formatter output (-f plain):
[![asciicast](https://asciinema.org/a/EBGsvQsuRz6xGrh86ttu0AnOc.svg)](https://asciinema.org/a/EBGsvQsuRz6xGrh86ttu0AnOc)

#### Json formatter output (-f json):
[![asciicast](https://asciinema.org/a/jXEOqNH5UBtEMt2niAFQAzguF.svg)](https://asciinema.org/a/jXEOqNH5UBtEMt2niAFQAzguF)
