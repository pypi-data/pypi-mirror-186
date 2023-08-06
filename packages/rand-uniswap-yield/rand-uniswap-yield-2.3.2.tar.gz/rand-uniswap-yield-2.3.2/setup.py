from setuptools import setup

setup(
    # this will be my Library name.
    name="rand-uniswap-yield",
    # Want to make sure people know who made it.
    author="adradr",
    # also an email they can use to reach out.
    author_email="adrian@rand.network",
    # I'm in alpha development still, so a compliant version number is a1.
    # read this as MAJOR VERSION 0, MINOR VERSION 1, MAINTENANCE VERSION 0
    version="2.3.2",
    license="MIT license",
    # here is a simple description of the library, this will appear when someone searches for the library on https://pypi.org/search
    description="A python library for Uniswap yield startegies",
    # here is the URL you can find the code, this is just the GitHub URL.
    url="https://github.com/Rand-Network/yield-strategy-data",
    # there are some dependencies to use the library, so let's list them out.
    install_requires=[
        "backoff",
        "DateTime",
        "gql[requests]",
        "graphql-core",
        "numpy",
        "pandas",
        "python-dateutil",
        "requests",
        "requests-toolbelt",
        "yarl",
        "zope.interface",
        "plotly",
        "nbformat",
    ],
    # some keywords for my library.
    keywords="uniswap amm defi yield strategy backtest simulate",
    # here are the packages I want "build."
    packages=["backtest"],
    # I also have some package data, like photos and JSON files, so I want to include those too.
    include_package_data=True,
    # you will need python 3.7 to use this libary.
    python_requires=">=3.7",
)
