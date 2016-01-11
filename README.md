# eduextractor
Extraction-Transformation Tools for Education Data.

![build-passing-status](https://travis-ci.org/openEduConnect/eduextractor.svg?branch=master)

[Docs](http://eduextractor.readthedocs.org/en/latest/)

## Installing cx_Oracle
[Because you have to](https://gist.github.com/thom-nic/6011715)

## Supported Datasources
* NWEA MAP Scores
* Powerschool

## Supported Backends
* CSV

## Configuration

You should create a file called .eduextractor.yml in your home directory.

You may change the location that eduextractor looks for the config file by
creating an envirnment variable called EDUEXTRACTOR\_CONFIG and setting it to
be the path to your config file as follows:

    $ export EDUEXTRACTOR_CONFIG=/path/to/my_eduextractor_config.yml

The contents of the .eduextractor.yml file should look like the following,
but with all of the blanks filled in:

    - ### PLACEHOLDER ###
    - ### PLACEHOLDER ###
