from st2common.runners.base_action import Action

__all__ = [
    'OutputAction'
]

class OutputAction(Action):
    def run(self, firstName, status, email):
        print('payload',status,firstName,email)
        return True