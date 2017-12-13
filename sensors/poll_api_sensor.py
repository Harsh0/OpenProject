import eventlet
import requests
import polling
from st2reactor.sensor.base import PollingSensor

class PollAPISensor(PollingSensor):
    def __init__(self,sensor_service, config):
        super(PollAPISensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        # self._stop = False
    
    def setup(self):
        self._logger.debug("Setup block")

    def poll(self):
        response = requests.get("http://10.0.1.180:8081/")
        if response.status_code ==200:
            payload = response.json()
            self.sensor_service.dispatch(trigger="my_first_pack_st2.polling_done_event",payload=payload)

    def cleanup(self):
        self._logger.debug("POllAPISensor, cleaning up")
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass