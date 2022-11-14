#!/usr/bin/python3
"""class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def _init_(self, *args, **kwargs):
        """
        init
        """
        super()._init_(*args, **kwargs)
