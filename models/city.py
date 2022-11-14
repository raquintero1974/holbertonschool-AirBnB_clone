#!/usr/bin/python3
"""class City"""


from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from BaseModel """

    state_id = ""
    name = ""

    def _init_(self, *args, **kwargs):
        """
        init
        """
        super()._init_(*args, **kwargs)
