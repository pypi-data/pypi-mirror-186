from setuptools import setup, find_packages
from pathlib import Path

setup(
    name = 'Testando o código para Ensalamento',
    version = 1.0,
    description = 'Ferramenta em teste',
    long_description=Path('README.md').read_text(),
    author = 'Flavio',
    author_email= 'professorflaviosoares@gmail.com',
    keyword = ['camera','video','processamento'],
    packages=find_packages()
)