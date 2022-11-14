#!/usr/bin/python3
"""class State"""


from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherits from BaseModel """

    name = ""

    def _init_(self, *args, **kwargs):
        """
        init
        """
        super()._init_(*args, **kwargs)
