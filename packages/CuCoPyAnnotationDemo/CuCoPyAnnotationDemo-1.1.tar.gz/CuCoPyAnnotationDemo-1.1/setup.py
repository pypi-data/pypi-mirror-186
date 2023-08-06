from setuptools import setup, find_packages
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name="CuCoPyAnnotationDemo",
    version="1.1",
    license="MIT",
    author="Julian Schoenau",
    author_email="j.schoenau@fz-juelich.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/FZJ-IEK3-VSA/CuCoPyAnnotationDemo",
    keywords="finance, conversion",
)