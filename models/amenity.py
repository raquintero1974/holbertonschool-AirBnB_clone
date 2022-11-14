#!/usr/bin/python3
"""class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class inherits from BaseModel"""

    name = ""

    def _init_(self, *args, **kwargs):
        """
        init
        """
        super()._init_(*args, **kwargs)
