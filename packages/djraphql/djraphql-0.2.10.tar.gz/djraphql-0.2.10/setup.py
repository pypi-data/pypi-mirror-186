import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.2.10"

setuptools.setup(
    name="djraphql",
    version=VERSION,
    author="Joel Gardner",
    author_email="joel@simondata.com",
    description="DjraphQL builds a flexible & performant GraphQL schema by examining your Django models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Radico/djraphql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "django",
        "graphene",
        "six",
    ],
    pypi={"name": "djraphql", "version": VERSION},
)
