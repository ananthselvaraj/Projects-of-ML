from setuptools import find_packages, setup
from typing import List

hper_e_dot = '-e .'
def get_library(filepath:str)->List[str]:

    requirments = []
    with open(filepath) as file_object:
        requirments = file_object.readlines()
        requirments = [req.replace('\n','') for req in requirments]

        if hper_e_dot in requirments:
            requirments.remove(hper_e_dot)
    return requirments
    

setup(

name='mlproject',
author='ananth',
author_email='ananthsa20@gmail.com',
packages=find_packages(),
install_requires = get_library('requirments.txt'),
version='0.0.1'
)
        


