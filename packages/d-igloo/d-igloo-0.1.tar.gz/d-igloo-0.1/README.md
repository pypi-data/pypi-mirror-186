# igloo

A command line tool to archive and retrieve project's data to and from Amazon AWS S3 Glacier for D-ICE Engineering needs.

# Prerequisites

You need AWS credentials on your system to connect to D-ICE AWS account.

# Installation

igloo is packaged under D-ICE conda channel. Installation is to be done with

```chell
conda install -c d-ice igloo
```

# Usage

TODO

```shell
igloo
```





# A retirer


Utility to store project data to archive into S3 Glacier


Tou need at least credentials on your computer to access to Amazon Glacier:

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html


Pour la compression, on pourra utiliser la commande suivante:


tar --use-compress-program="pigz -k -6" -cf <archive>.tar.gz <folder>


Packaging follows the template given into this repository:

https://github.com/jrhawley/python-conda-package-template


Pas reussi a packager conda pour d'obscures raisons de cuda...

Pour la packaging pip, il faut faire:

python setup.py install
python setup.py sdist
twine upload dist/*