from setuptools import setup, find_packages

setup(
    name="CuCoPyAnnotationDemo",
    version="1.0",
    license="MIT",
    author="Julian Schoenau",
    author_email="j.schoenau@fz-juelich.de",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/FZJ-IEK3-VSA/CuCoPyAnnotationDemo",
    keywords="finance, conversion",
)