"""
This module contains the implementation for KeyboardInterface.
"""
import uinput
import logging

from interfaces.base import BaseInterface


LOGGER = logging.getLogger(__name__)


class KeyboardInterface(BaseInterface):
    """The Keyboard interface definition for translating idrive controller inputs to key strokes."""

    __interface_name__ = 'keyboard'

    def __init__(self, controller):
        """
        Initializes a keyboard service to emulate key strokes.

        Arguments
        ---------
            controller : controllers.base.BaseController
                the parent controller that is instantiated this interface

        """
        super(KeyboardInterface, self).__init__()
        self.controller = controller
        self.client_sock = None
        self.client_info = None
        self.rfcomm_channel = None
        self.service_name = self.get_setting('service_name')
        self.service_uuid = self.get_setting('service_uuid')
        self.server_sock = None
        self.thread = None
        self.keyboard = uinput.Device([uinput.KEY_E, uinput.KEY_H, uinput.KEY_L, uinput.KEY_O])
        # map the inputs to the function blocks
        # TODO: trial and error, map controller messages to keys
        self.keyoptions = 
        {
            0 : uinput.KEY_H,
            1 : uinput.KEY_E,
            4 : uinput.KEY_E,
            9 : uinput.KEY_E,
            2 : uinput.KEY_E,
            3 : uinput.KEY_E,
            5 : uinput.KEY_E,
            7 : uinput.KEY_E,
        }
        
    def send(self, data):
        """
        Sends data via Keyboard

        Arguments
        ---------
            data : basestring
                the data to be sent via this interface

        """

        try:
            printf(data)
            printf(keyoptions[data])
            keyboard.emit_click(keyoptions[data])
            
            
        except Exception:
            LOGGER.exception('bluetooth send exception')
            
