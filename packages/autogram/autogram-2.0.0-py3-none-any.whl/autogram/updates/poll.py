from . import UpdateBase
from typing import Dict, Callable

class Poll(UpdateBase):
    name = 'poll'

    def __init__(self, update: Dict):
        self.autogram.logger.debug(f'Poll: {update}')

    @classmethod
    def addHandler(cls, handler: Callable):
        cls.handler = handler
        cls.subscribed_updates.add(cls.name)

