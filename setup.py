from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from the given file.
    """
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present

    return requirements

setup(
    name='MLProject1',
    version='0.0.1',
    author='Praseetha',
    author_email='praseethaprakashvp@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)