class Table(): 
    """A representation a table. 
    has source and transformation methods. 

    Attributes
    name (str)
    html_source (netloc)
    headers (list of str)

    """
    def __init__(self, name, html_source, headers):
        self.name = name
        self.html_source = html_source
        self.headers = headers
    


