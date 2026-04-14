from setuptools import setup, find_packages

setup(
    name="sovereign_bureau",
    version="2.0.0",
    author="The Peculiar Librarian",
    description="A deterministic validation engine based on the PADI Technical Standard.",
    packages=find_packages(),
    install_requires=[
        "rdflib>=6.0.0",
        "pydantic>=2.0.0",
    ],
    classifiers=[
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3.10",
    ],
)
