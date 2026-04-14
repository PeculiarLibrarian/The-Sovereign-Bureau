from setuptools import setup, find_packages

setup(
    name="sovereign-bureau",
    version="2.0.0",
    author="Samuel Muriithi Gitandu",
    author_email="samuel@thepeculiarlibrarian.tech",
    description="Operational implementation of the PADI Technical Standard.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rdflib>=6.0.0",
    ],
    python_requires='>=3.8',
    project_urls={
        "Source": "https://github.com/thebureau/padi-standard",
    },
)
