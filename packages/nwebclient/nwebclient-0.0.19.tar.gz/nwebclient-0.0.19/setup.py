import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nwebclient",
    version="0.0.19",
    author="Bjoern Salgert",
    author_email="bjoern.salgert@hs-duesseldorf.de",
    description="NWebClient via HTTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bsnx.net/4.0/group/pynwebclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["usersettings>=1.0.7"]
)
