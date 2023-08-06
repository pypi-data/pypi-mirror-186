import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdcheckers",
    version="0.1",
    author="Luiz P.",
    author_email="umluiz@gmail.com",
    description="Investigate consistency and dirtiness of a pandas DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umLu/pdcheckers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="pandas dataframe dirty validation data cleaning",
    packages=setuptools.find_packages(),
    install_requires=["regex",
                      "pandas"],
    python_requires=">=3.6",
)
