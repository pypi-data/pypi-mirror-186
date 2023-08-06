import setuptools
import os

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, "README.md")) as f:
    long_description = f.read()

__version__ = "Undefined"
for line in open(os.path.join("igloo", "__init__.py")):
    if line.startswith("__version__"):
        exec(line.strip())

# import igloo

setuptools.setup(
    name="d-igloo",
    version=__version__,
    description="A command line tool to archive and retrieve project's data to and from Amazon "
                "AWS S3 Glacier for D-ICE Engineering needs.",
    author="Francois Rongere",
    author_email="francois.rongere@dice-engineering.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "argparse",
        "boto3"
    ],
    url="https://d-ice.gitlab.host/common/igloo",
    # zip_safe=True,
    long_description=long_description,
    long_description_content_type="text/markdown",

    entry_points={
        'console_scripts': ['igloo=igloo.igloo_cli:main']
    }
)
