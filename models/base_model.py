#!/usr/bin/python3

"""
Write a class BaseModel that defines all common
attributes/methods for other classes:
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class BaseModel Hbnb project
    """

    def __init__(self, *args, **kwargs):
        """
        init a new BaseModel
        """
        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def save(self):
        """
        Public instance attribute updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Dictionary representation of an instance (method to_dict())
        """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
