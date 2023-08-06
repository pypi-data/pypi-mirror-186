![image](docs/logo_name.png)

-------
FOTOTEX
-------

Fourier Transform Textural Ordination in Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://framagit.org/benjaminpillot/fototex/activity)
[![PyPI version](https://badge.fury.io/py/fototex.svg)](https://badge.fury.io/py/fototex)

Freely adapted from https://github.com/CaussesCevennes/FOTO.py

## List of authors
* Benjamin Pillot <benjamin.pillot@ird.fr>
* Dominique Lyszczarz <observatoire@causses-et-cevennes.fr>
* Claire Teillet <teillet.claire@hotmail.com>
* Pierre Couteron <pierre.couteron@ird.fr>
* Nicolas Barbier <nicolas.barbier@ird.fr>
* Philippe Verley <philippe.verley@ird.fr>
* Marc Lang <marc.lang@irstea.fr>
* Thibault Catry <thibault.catry@ird.fr>
* Laurent Demagistri <laurent.demagistri@ird.fr>
* Nadine Dessay <nadine.dessay@ird.fr>

## Tutorial
See [here](https://nbviewer.jupyter.org/urls/framagit.org/benjaminpillot/fototex/-/raw/master/tutorial/tutorial.ipynb)


## Description
FOTO (Fourier Textural Ordination) is an algorithm allowing texture
characterization and comparison, and is fully
described in _Textural ordination based on Fourier spectral 
decomposition: a method to analyze and compare landscape patterns_
(Pierre Couteron, Nicolas Barbier and Denis Gautier, 2006)

FOTOTEX is to date the most complete Python implementation of this 
algorithm. It is (really) fast and optimized to get the best of 
FOTO on any computer.


## Installation
Use `pip` in a terminal to install fototex:
```shell script
$ pip install fototex
```

### Note on GDAL
Installing GDAL through `pip` might be tricky as it only gets
the bindings, so be sure the library is already installed on 
your machine, and that the headers are located in the right
folder. Another solution may to install it through a third-party
distribution such as `conda`.

See [here](https://framagit.org/benjaminpillot/fototex/-/wikis/How-to-install-GDAL) for the steps 
you should follow to install GDAL/OGR and the [GDAL Python libraries](https://pypi.org/project/GDAL/) 
on your machine.

## Contributing

### Development and improvement

* Benjamin Pillot
* Dominique Lyszczarz
* Claire Teillet
* Pierre Couteron
* Nicolas Barbier
* Philippe Verley
* Marc Lang
* Thibault Catry
* Laurent Demagistri

### Conceptualization and Coordination

* Benjamin Pillot
* Thibault Catry
* Laurent Demagistri
* Nadine Dessay

### Scientific projects

* TOSCA APUREZA project, funded by CNES (TOSCA 2017-2020)
* TOSCA DELICIOSA project, funded by CNES (TOSCA 2020-2022)
* PCIA PROGYSAT project, funded by Interreg Amazon Cooperation Program (Urban axis) - (2021-2023)

<br/>

![image](docs/espace-dev-ird.png)
