"""Implementation specific class for controlling a DC motor via RPi.GPIO."""
import RPi.GPIO as GPIO
from pyraspi import RPiOut
from pymotors import DcBase, DcArray


class RPiDc(DcBase):
    """Control a DC motor with a Raspberry Pi."""

    def __init__(self, fwd_pin=[], rev_pin=[]):
        f_pins = []
        r_pins = []
        for pin in fwd_pin:
            f_pins = f_pins + [RPiOut(pin, 'LOW')]
        for pin in rev_pin:
            r_pins = r_pins + [RPiOut(pin, 'LOW')]
        super().__init__(f_pins, r_pins)

    def _togglePins(self, set_dir: str):
        pins = self._toggle_dict[set_dir]
        for pin in pins[0]:
            pin.state = False
        for pin in pins[1]:
            pin.state = True


class RPiDcArray(DcArray):
    """Control an array of DC motors with a Raspberry Pi."""

    def __init__(self, dc_motors: list, pwm_p_f, pwm_p_r, pwm_duty, pwm_freq):
        super().__init__(dc_motors)
        self.pwm_duty = pwm_duty
        GPIO.setmode(GPIO.BCM)
        self.pwm_fwd = GPIO.PWM(pwm_p_f, pwm_freq)
        self.pwm_rev = GPIO.PWM(pwm_p_r, pwm_freq)

    def _activateFwd(self):
        self.pwm_rev.stop()
        self.pwm_fwd.start(self.pwm_duty)

    def _activateRev(self):
        self.pwm_fwd.stop()
        self.pwm_rev.start(self.pwm_duty)

    def _deactivate(self):
        self.pwm_fwd.stop()
        self.pwm_rev.stop()
        GPIO.cleanup()

    def setSpeed(self, value):
        """Change the PWM duty cycle for both directions."""
        self.pwm_duty = value
        self.pwm_fwd.ChangeDutyCycle(self.pwm_duty)
        self.pwm_rev.ChangeDutyCycle(self.pwm_duty)
