import setuptools

setuptools.setup(
    name="pyraspi",
    version="0.0.1",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Raspberry Pi related Python utilities.",
    url="https://github.com/czbiohub/PyRasPi",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[
        "RPi.GPIO",
        "pymotors @ http://github.com/czbiohub/PyMotors/tarball/master.tar.gz",
    ],
    test_suite="tests",
    classifiers=[
        "CZ Biohub :: Bioengineering",
    ],
)
