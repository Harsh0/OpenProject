from st2common.runners.base_action import Action

import requests

__all__ = [
    'OutputAction'
]

class OutputAction(Action):
    def run(self, url,body):
        print('payload',url, body)
        return True