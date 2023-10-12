#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
module BaseModel
contains the class Basemodel
"""


class BaseModel:
    """
    Defines all common attributes/methods
    for other Classes
    """
    def __init__(self, *args, **kwargs):
        """
        initializes instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates instance updated_at with
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        prints classname, id, type
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """
        returns dictionarywith all key/value instances
        of __dict__ instances
        """
        dict_ = {}
        dict_["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                dict_[key] = value.isoformat()
            else:
                dict_[key] = value
        return dict_
