from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt and returns a list of dependencies.
    Automatically removes the '-e .' line used for editable installs.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Demandcast',
    version='0.1.0',
    author='Divyanshu',
    author_email='immadivyansh@gmail.com',
    description='A production-ready machine learning system for forecasting hourly bike rental demand to support dynamic pricing and fleet optimization.',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.8',
)
