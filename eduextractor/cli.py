import click
from eduextractor.sis.powerschool import PowerSchoolAdmin, PowerSchoolFrontend
import os
import logging
from .config import _load_secrets
from six.moves import input

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
        psa = PowerSchoolAdmin(secrets)
        psf = PowerSchoolFrontend(secrets)

        sql_filenames = [
            "adhoc_studentemail.sql",
            "attendance.sql",
            "enrollments.sql",
            "grades.sql",
            "schools.sql",
            "students.sql",
            "k12studentenrollment.sql"
        ]

        if io.lower() == 'extract':
            logger.info("Beginging PowerSchool Export")

            # Login to Admin, upload HTML
            psa.login()
            psa._go_to_custom_pages()
            # ps doesn't error if folder exists, so fine to run everytime
            psa._add_eduextractor_folder()

            # Now let's prep our queries and files

            # Okay, Content time
            with resource_stream('eduextractor.sis.powerschool.html', 'top.html') as f:
                top = f.read()
            with resource_stream('eduextractor.sis.powerschool.html', 'bottom.html') as f:
                bottom = f.read()

            # Create the pages
            for sql_filename in sql_filenames:
                page_name = sql_filename.replace('.sql', '.html')
                logger.info("Creating page " + page_name)
                psa._create_html_page(page_name)
                logger.info("Page " + page_name + " created.")

            # waiting for publishing
            prompt = "Please click Publish on every new page in /eduextractor."
            pub_status = input(prompt)

            if not pub_status:
                logger.error("You haven't published anything yet. ")

            for sql_filename in sql_filenames:
                page_name = sql_filename.replace('.sql', '.html')

                with resource_stream('eduextractor.sis.powerschool.sql', sql_filename) as f:
                    query_content = f.read()

                content = top + query_content + bottom
                psa._publish_custom_page(page_name, content)

        elif io.lower() == 'download':
            if data.lower() == 'all':
                # go to frontend
                psf.login()
                logger.info('Downloading tables')
                psf._download_csvs_to_tmp()
            elif data:
                valid_fields = [x.replace('.sql', '') for x in sql_filenames]
                if data.lower() in valid_fields:
                    print("Downloading %s" % data.lower())
                    psf.login()
                    psf._download_html_table(data.lower() +
                                             '.html').to_csv('/tmp/'
                                                             + data.lower()
                                                             + '.csv')
            else:
                raise Exception("Table Not Found")


if __name__ == '__main__':
    cli()
