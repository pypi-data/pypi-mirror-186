from setuptools import setup, find_namespace_packages

PROJECT = "kerenor"

setup(
    name=PROJECT,
    version='0.0.0',
    description=PROJECT,
    author=PROJECT,
    packages=find_namespace_packages(include=[f"{PROJECT}*"])
)
