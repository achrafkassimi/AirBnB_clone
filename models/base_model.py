#!/usr/bin/python3
"""
Class BaseModel.
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Represents BaseModel of this project
    """

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], time_format)
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], time_format)

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Update updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance
        Includes the key/value pair __class__ representing
        the class name of the object
        """
        dit = self.__dict__.copy()
        dit["created_at"] = self.created_at.isoformat()
        dit["updated_at"] = self.updated_at.isoformat()
        dit["__class__"] = self.__class__.__name__
        return dit

    def __str__(self):
        """
        Return the representation of the BaseModel instance.
        """
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
