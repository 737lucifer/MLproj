from setuptools import setup, find_packages
from typing import List

Hypen_E_DOT='-e .'
def get_req(file_path:str)->List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
         
        if Hypen_E_DOT in requirments:
            requirments.remove(Hypen_E_DOT)
    return requirments
# the above function will return  a list of requirments

setup(
    name="MLProj",
    version="0.1",
    packages=find_packages(),
    install_requires=get_req('requirments.txt'),
    author="uma",
    description="My first file"
)