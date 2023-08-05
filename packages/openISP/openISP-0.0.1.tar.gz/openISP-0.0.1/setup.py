import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openISP",
    version="0.0.1",
    author="Kevin Ting-Kai Kuo",
    author_email="kaikaikaisquare@protonmail.com",
    description="An open-source software ISP pipelines package which is mainly based on cruxopen's original work openISP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kuo-TingKai/openISP/tree/kevin-branch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)