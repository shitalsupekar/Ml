
from setuptools import setup, find_packages


from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "HYPHEN_E_DOT" in requirements:
            requirements.remove("HYPHEN_E_DOT")

    return requirements

setup(
    name='MlProject',
    version='0.0.1',
    author='Shital',
    author_email='shitalsupekar138@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
