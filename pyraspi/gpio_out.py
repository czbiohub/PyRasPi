"""Basic GPIO output pin control class."""
from threading import Timer
import RPi.GPIO as GPIO

class GpioOut():
    """Set GPIO output by assigning a boolean to the state property.

    Parameters
    ----------
    output_pin : int
        Pin number to be controlled.

    """
    def __init__(self, output_pin=None):
        self._output_pin = output_pin

    @property
    def state(self) -> bool:
        """Return current state of object."""
        return self._getOutput()

    @state.setter
    def state(self, activate: bool):
        """Set state of object."""
        self._setOutput(activate)

    def _setOutput(self, state):
        """Override with application specific method."""

    def _getOutput(self):
        """Override with application specific method."""


class RPiOut(GpioOut):
    """Initialize output pin with Broadcom numbering.

    Parameters
    ----------
    output_pin : int
        Broadcom pin number to be controlled.
    intitial_state : str
        State of pin upon initialization.

    """

    def __init__(self, output_pin=None, initial_state=None):
        GPIO.setmode(GPIO.BCM)
        if initial_state == 'LOW':
            GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
        elif initial_state == 'HIGH':
            GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
        else:
            GPIO.setup(output_pin, GPIO.OUT)

        super().__init__(output_pin)

    def __del__(self):
        GPIO.cleanup()

    def _getOutput(self) -> bool:
        return GPIO.input(self._output_pin)

    def _setOutput(self, state):
        GPIO.output(self._output_pin, state)


class RPiTimedOut(RPiOut):
    """Raise or lower a Raspberry Pi pin with an optional timer.

    Parameters
    ----------
    output_pin : int
        Broadcom pin number to be controlled.
    intitial_state : str
        State of pin upon initialization.

    """

    def __init__(self, pin=None, initial_state=None):
        self.timer = None
        super().__init__(pin, initial_state)

    def __del__(self):
        self.stop()
        if self.timer is not None:
            self.timer.join()
        GPIO.cleanup()

    def start(self, time_s=0):
        """Set the pin high for the duration specified."""
        self.state = True
        if time_s > 0:
            self.timer = Timer(time_s, self.stop)
            self.timer.start()

    def stop(self):
        """Set the pin low and cancel timers."""
        self.state = False
        if self.timer is not None:
            if self.timer.is_alive():
                self.timer.cancel()
