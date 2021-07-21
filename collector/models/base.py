"""
Base representation of model
"""

class BaseModel:
    """
    Base model
    """
    def json(self):
        """
        Model as json data
        """
        raise NotImplementedError("json() not implemented")