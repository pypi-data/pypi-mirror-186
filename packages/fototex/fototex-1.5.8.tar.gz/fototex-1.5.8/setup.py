from setuptools import setup, find_packages

import fototex

with open("README.md", 'r') as fh:
    long_description = fh.read()

with open("requirements.txt") as req:
    install_req = req.read().splitlines()

setup(name='fototex',
      version=fototex.__version__,
      description='Fourier Transform Textural Ordination',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://framagit.org/benjaminpillot/fototex',
      author='Benjamin Pillot <benjamin.pillot@ird.fr>, '
             'Dominique Lyszczarz <observatoire@causses-et-cevennes.fr>, '
             'Claire Teillet, <teillet.claire@hotmail.com>, '
             'Pierre Couteron <pierre.couteron@ird.fr>, '
             'Nicolas Barbier <nicolas.barbier@ird.fr>, '
             'Philippe Verley <philippe.verley@ird.fr>, '
             'Marc Lang <marc.lang@irstea.fr>, '
             'Thibault Catry <thibault.catry@ird.fr>, '
             'Laurent Demagistri <laurent.demagistri@ird.fr>, '
             'Nadine Dessay <nadine.dessay@ird.fr>',
      install_requires=install_req,
      python_requires='>=3',
      license='The MIT Licence',
      packages=find_packages(exclude=("tutorial",)),
      zip_safe=False)
