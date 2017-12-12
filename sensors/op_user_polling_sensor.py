from st2reactor.sensor.base import PollingSensor
import requests
import polling
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://10.0.1.180:8080'

class UserSensor(PollingSensor):
    
    def __init__(self, sensor_service, config):
            super(UserSensor, self).__init__(sensor_service=sensor_service, config=config)
            self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
            
    def setup(self):
        pass

    def poll(self):
        self._logger.debug('UserSensor dispatching trigger...')
        payload = requests.get('http://10.0.1.180:8080/api/v3/users',auth=HTTPBasicAuth('apikey','dcd91d4f82d39ad0e743636e08e377d8264e20c7')),   
        if payload.status_code == 200:
            user_list = payload.json()
            last_updated_user = user_list['_embedded']['elements'][0]
            self.sensor_service.dispatch(trigger='op-st2-integration.polling_event',payload=last_updated_user)

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass