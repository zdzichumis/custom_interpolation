from setuptools import setup, find_packages

setup(
    name="custom_interpolation",
    version="0.1.0",
    description="A package for interpolation using both Lagrange and spline methods with plotting capabilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Michalski",
    author_email="adammichalski@adres.pl",
    url="https://github.com/zdzichumis/custom_interpolation",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)