### Hexlet tests and linter status:
[![Actions Status](https://github.com/IDilettant/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/IDilettant/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7ca7a58ae374ae5ab91b/maintainability)](https://codeclimate.com/github/IDilettant/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7ca7a58ae374ae5ab91b/test_coverage)](https://codeclimate.com/github/IDilettant/python-project-lvl2/test_coverage)
![Actions Status](https://github.com/IDilettant/python-project-lvl2/workflows/tests%20and%20lints/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Description

The program is a cli-utility that allows to compare between JSON and/or YAML files.
And display the resulting difference in various presentation options

This is the second project implemented for educational purposes in the learning process on [the Hexlet](https://ru.hexlet.io) platform


## Quickstart
```bash
pip install git+https://github.com/IDilettant/python-project-lvl2.git
```


## Running
```bash
gendiff -f <format> <file1> <file2>
```
Where ```<file1>``` and ```<file2>``` is filepaths.

Available output formats: "stylish", "plain", "json"


## Demos

#### Stylish-style formatter for plain structure files:
[![asciicast](https://asciinema.org/a/fRr3HiS9NoFo0m45bayVNVvaa.svg)](https://asciinema.org/a/fRr3HiS9NoFo0m45bayVNVvaa)

#### Stylish-style formatter for nested structure files:
[![asciicast](https://asciinema.org/a/1J2DoAfr6nR1iwtf32DiCXm92.svg)](https://asciinema.org/a/1J2DoAfr6nR1iwtf32DiCXm92)

#### Plain-style formatter:
[![asciicast](https://asciinema.org/a/EBGsvQsuRz6xGrh86ttu0AnOc.svg)](https://asciinema.org/a/EBGsvQsuRz6xGrh86ttu0AnOc)

#### Json-style formatter:
[![asciicast](https://asciinema.org/a/jXEOqNH5UBtEMt2niAFQAzguF.svg)](https://asciinema.org/a/jXEOqNH5UBtEMt2niAFQAzguF)
