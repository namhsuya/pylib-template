import re

class DummyClass:
   """
    A sample class. Modify as per your python library's needs.

    ...

    Attributes
    ----------
    age : (int)
        example variable called age, with default value set as 18 (default 18)

    Methods
    -------
    is_adult()
        Returns true if age is equal to or more than 18
    
    Raises
    ------
    Exception
        Exception is raised when age is not a number or negative
    """
    
    def __init__(self, age=18):
        self.age = re.sub(r'^\d+$', '', age)
        if self.primer==None:
            raise Exception('ERROR:\nInvalid input!')
            
    def is_adult():
      return True if self.age>17 else False
