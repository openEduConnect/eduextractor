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
        sql_queries = os.listdir('./eduextractor/sis/powerschool/sql/')
        filenames = [f.replace('.sql', '.html') for f in sql_queries]
        
        # make the html pages. 
        [psa._create_html_page(f) for f in filenames]
        
        # Okay, Content time
        top_file = open('./eduextractor/sis/powerschool/html/top.html',
                        'r')
        bottom_file = open('./eduextractor/sis/powerschool/html/bottom.html',
                           'r')
        top = top_file.read()
        bottom = bottom_file.read()
        
        for query in sql_queries:
            page_name = query.replace('.sql', '.html')
            query_content_f = open('./eduextractor/sis/powerschool/sql/' + 
                                   query, 'r')
            query_content = query_content_f.read()
            content = top + query_content + bottom
            print content
            psa._publish_custom_page(page_name, content)

        # go to frontend
        psf.login()

if __name__ == '__main__':
    cli()
