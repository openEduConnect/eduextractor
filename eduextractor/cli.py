import click
import eduextractor.sis.powerschool.powerschool_exporter
import eduextractor.sis.illuminate.illuminate_exporter
from .sis.powerschool.powerschool_exporter import PowerSchoolSQLInterface
from .sis.illuminate.illuminate_exporter import IlluminateSQLInterface
import os
import logging
from .config import _load_secrets

from pkg_resources import resource_stream

logger = logging.getLogger('eduextractor')

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(fmt)
logger.addHandler(ch)


@click.command()
@click.option('--sis', default='powerschool',
              help='which SIS extractor to use')
@click.option('--io', default='extract',
              help="""'extract' or 'download'""")
@click.option('--data', default='all',
              help="""Which file/query do you want to extract.  Defaults to 'all'.""")
@click.option('--config', default=None,
              help="""Location of the config file""")
def cli(sis, io, data, config):
    """
    The CLI inteface. Just powerschool extracts
    for now.
    """
    secrets = _load_secrets(config)

    if sis.lower() == 'powerschool':
        interface = PowerSchoolSQLInterface()
        interface.download_files()
    if sis.lower() == 'illuminate':
        interface = IlluminateSQLInterface()
        interface.download_files()

if __name__ == '__main__':
    cli()
