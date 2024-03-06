from setuptools import find_packages, setup
import shutil
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# This will install the required packages
setup(
    name='Real_estate_capstone_project',
    version='0.0.1',
    author='Atul',
    author_email='atulkumarsingh7810@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# Clean up the 'build' directory after the build process is complete
shutil.rmtree("build", ignore_errors=True)
