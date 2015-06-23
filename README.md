# eduextractor
Extraction-Transformation Tools for Education Data. 

## Supported Backends
* NWEA MAP Scores

## Config File
To configure the library, make sure to have a `~/.eduextractor.yml` stored in your home directory. Sample:

```
nwea_map:
  url: https://your-custom-admin.mapnwea.org
  username: yourusername@domain.com
  secret: your_secret_pw
  dest: '/tmp'
```
