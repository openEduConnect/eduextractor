# eduextractor
Extraction-Transformation Tools for Education Data. 
![build-passing-status](https://travis-ci.org/openEduConnect/eduextractor.svg?branch=master)

## Supported Datasources 
* NWEA MAP Scores
* Powerschool
## Supported Backends
* CSV
* SQLAlchemy (There postgresql, mysql, sqlite, and more!)

## Config File
To configure the library, make sure to have a `~/.eduextractor.yml` stored in your home directory. Sample:

```
nwea_map:
  url: https://your-custom-admin.mapnwea.org
  username: yourusername@domain.com
  secret: your_secret_pw
  dest: '/tmp'
```

## Powerschool 
Custom page on Powerschool. 
