import logging
import datetime
import requests

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

class Orange(NeuronModule):
	def __init__(self, **kwargs):
        super(Orange, self).__init__(**kwargs)
		
		# get the command
		self.action = kwargs.get('action', None),
        self.num_chaine = kwargs.get('numero_chaine', 1)
		
		if self.action == "on":
			r = requests.get('http://dcodeurtv4-1.home:8080/remoteControl/cmd?operation=01&key=164&mode=0')
	
	def _is_parameters_ok(self):
		if self.action is None:
			raise InvalidParameterException("An action is require")
	

	@staticmethod
    def _start_tv(state):
        r = requests.get('http://dcodeurtv4-1.home:8080/remoteControl/cmd?operation=01&key=164&mode=0')
        return True