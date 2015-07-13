import click 
from eduextractor.sis.powerschool import PowerSchoolAdmin, PowerSchoolFrontend
import os


@click.command()
@click.option('--sis', default='powerschool', 
              help='which SIS extractor to use')
@click.option('--io', default='extract', 
              help='Do you want to extract, import do both.')
def cli(sis, io):
    """
    The CLI inteface. Just powerschool extracts
    for now. 
    """
    if sis.lower() == 'powerschool':
        psa = PowerSchoolAdmin()
        psf = PowerSchoolFrontend()

        # Login to Admin, upload HTML 
        psa.login()
        psa._go_to_custom_pages()
        # ps doesn't error if folder exists, so fine to run everytime
        psa._add_eduextractor_folder() 
        
        # Now let's prep our queries and files
        print os.getcwd()

        sql_queries = os.listdir('./eduextractor/sis/powerschool/sql/')
        filenames = [f.replace('.sql', '.html') for f in sql_queries]
        
        # make the html pages. 
        [psa._create_html_page(f) for f in filenames]
        # go to frontend
        psf

if __name__ == '__main__':
    cli()
