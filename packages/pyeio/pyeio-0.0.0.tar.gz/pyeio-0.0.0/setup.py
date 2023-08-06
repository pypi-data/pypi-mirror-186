from setuptools import setup, find_packages

setup(
    name="pyeio",
    description="Python library for easy input/output file operations.",
    version="0.0.0",
    author="Hart Traveller",
    author_email="hart@cephalon.io",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pathlib"],
)
