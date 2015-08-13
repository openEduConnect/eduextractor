import click 
from eduextractor.sis.powerschool import PowerSchoolAdmin, PowerSchoolFrontend
import os
import logging

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
              help='Do you want to extract, import do both.')
@click.option('--data', default='all',
              help="""Which file/query do you want to extract. 
              Defaults to all.""")
def cli(sis, io, data):
    """
    The CLI inteface. Just powerschool extracts
    for now. 
    """
    if sis.lower() == 'powerschool':
        psa = PowerSchoolAdmin()
        psf = PowerSchoolFrontend()
        if io.lower() == 'extract':
            logger.info("Beginging PowerSchool Export")

            # Login to Admin, upload HTML 
            psa.login()
            psa._go_to_custom_pages()
            # ps doesn't error if folder exists, so fine to run everytime
            psa._add_eduextractor_folder() 
            
            # Now let's prep our queries and files
            sql_queries = os.listdir('./eduextractor/sis/powerschool/sql/')
            
            # Okay, Content time
            top_file = open('./eduextractor/sis/powerschool/html/top.html',
                            'r')
            bottom_file = open("./eduextractor/sis/powerschool/html/bottom.html",
                               'r')
            top = top_file.read()
            bottom = bottom_file.read()
            
            # Create the pages
            for query in sql_queries:
                page_name = query.replace('.sql', '.html')
                logger.info("Creating page " + page_name)
                psa._create_html_page(page_name)
                logger.info("Page " + page_name + " created.")

            # waiting for publishing
            prompt = "Please click Publish on every new page in /eduextractor."
            pub_status = raw_input(prompt)
            if not pub_status:
                logger.error("You haven't published anything yet. ")
            for query in sql_queries:
                page_name = query.replace('.sql', '.html')
                query_content_f = open('./eduextractor/sis/powerschool/sql/' + 
                                       query, 'r')
                query_content = query_content_f.read()
                content = top + query_content + bottom
                psa._publish_custom_page(page_name, content)
        elif io.lower() == 'download':
            if data.lower() == 'all':
                # go to frontend
                psf.login()
                logger.info('Downloading tables')
                psf._download_csvs_to_tmp()
            elif data:
                valid_fields = os.listdir("./eduextractor/sis/powerschool/sql")
                valid_fields = [x.replace('.sql', '') for x in valid_fields]
                if data.lower() in valid_fields:
                    print "Downloading %s" % data.lower()
                    psf.login()
                    psf._download_html_table(data.lower() + 
                                             '.html').to_csv('/tmp/' 
                                                             + data.lower() 
                                                             + '.csv')
            else:
                raise Exception("Table Not Found")


if __name__ == '__main__':
    cli()
