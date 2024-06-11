# we use this setup file for installing a local package in my virtual environment
from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    versions='0.0.1',
    author='Deepak Singh',
    author_email='ma23m006@smail.iitm.ac.in',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)