from setuptools import setup

from src.UC_Quantum_Lab import __version__
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='UC-Quantum-tools',
    version=__version__,
    author='Marek Brodke, with support from the University of Cincinnati',
    description='Provides functionaliy for UC-Quantum-Lab development tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='development',
    python_requires='>=3.8',
    license="MIT",
    author_email="brodkemd@mail.uc.edu",
    url="https://github.com/UC-Advanced-Research-Computing/UC-Quantum-tools",
    install_requires=[
        'qiskit>=0.39.0',
        'matplotlib'
    ]
)