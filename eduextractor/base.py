from eduextractor import secrets


class RemoteSource():
    """A remote source of data, 
    the fundamental abstraction of the project.
    """
    def __init__(self,name):
        self.name = name

class TestSource(RemoteSource):
    """A subclass representing test score data
    """
    def __init__(self):
        pass
class MAPSource(TestSource):
    """The Source for NWEA Map test scores
    """
    def __init(self):
        pass
def toSQL(file,table):
    """Converts a CSV file into a SQL table. 
    Should be a flag or something.
    """
    pass
