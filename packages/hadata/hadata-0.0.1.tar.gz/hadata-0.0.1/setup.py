import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hadata",
    version="0.0.1",
    description="long description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psf/requests",  
	project_urls={
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
    packages=setuptools.find_packages()
)
