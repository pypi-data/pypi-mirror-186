from setuptools import setup, find_packages
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as file:
        install_requires = file.read().splitlines()

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="deutsche-bahn-api",
    version="1.0.2",
    author="Tutorialwork",
    author_email="mail@manuelschuler.dev",
    description="A small package to work with the Deutsche Bahn timetables api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tutorialwork/deutsche_bahn_api",
    packages=find_packages(),
    install_requires=["mpu", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)