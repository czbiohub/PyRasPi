import setuptools

setuptools.setup(
    name="pyraspi",
    version="0.0.1",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Raspberry Pi related Python utilities.",
    url="https://github.com/czbiohub/bioe-python-common",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[
        "RPi.GPIO",
        "pymotors",
    ],
    test_suite="tests",
    classifiers=[
        "CZ Biohub :: Bioengineering",
    ],
)
