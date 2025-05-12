from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """
    This function will return list of requirements
    """
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
        for i,req in enumerate(requirements):
            requirements[i] = req.replace("\n","")
            
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
    name="House_price",
    version="0.0.1",
    author="Rupak",
    author_email="rupskarhade17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)


