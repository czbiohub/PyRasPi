import unittest
from unittest.mock import MagicMock, patch
from time import sleep

MockRPi = MagicMock()
modules = {
    "RPi": MockRPi,
    "RPi.GPIO": MockRPi.GPIO,
    "pymotors": MockRPi,
}
patcher = patch.dict("sys.modules", modules)
patcher.start()

from pyraspi import GpioOut, RPiOut, RPiTimedOut

class Test_GpioOut(unittest.TestCase):
    def setUp(self):
        self.pin_out = 12
        self.gpio = GpioOut(self.pin_out)
        self.gpio._setOutput = MagicMock()
        self.gpio._getOutput = MagicMock()

    def test_set_state_true(self):
        self.gpio.state = True
        self.gpio._setOutput.assert_called_with(True)

    def test_set_state_false(self):
        self.gpio.state = False
        self.gpio._setOutput.assert_called_with(False)

    def test_get_state(self):
        self.gpio._getOutput.side_effect = [True, False]
        self.assertTrue(self.gpio.state)
        self.assertFalse(self.gpio.state)

class Test_RPiOut(unittest.TestCase):
    def setUp(self):
        self.pin_out = 12
        self.gpio = RPiOut(self.pin_out)
        MockRPi.reset_mock()

    def test_get_output(self):
        self.gpio._getOutput()
        MockRPi.GPIO.input.assert_called_with(self.pin_out)

    def test_set_output(self):
        self.gpio._setOutput(True)
        MockRPi.GPIO.output.assert_called_with(self.pin_out, True)

    def test_init_conditions(self):
        gpio_low = RPiOut(self.pin_out, 'LOW')
        MockRPi.GPIO.setup.assert_called_with(self.pin_out, MockRPi.GPIO.OUT, initial=MockRPi.GPIO.LOW)

        gpio_high = RPiOut(self.pin_out, 'HIGH')
        MockRPi.GPIO.setup.assert_called_with(self.pin_out, MockRPi.GPIO.OUT, initial=MockRPi.GPIO.HIGH)

        gpio_float = RPiOut(self.pin_out)
        MockRPi.GPIO.setup.assert_called_with(self.pin_out, MockRPi.GPIO.OUT)


class Test_RPiTimedOut(unittest.TestCase):
    def setUp(self):
        self.pin_out = 12
        self.gpio = RPiTimedOut(self.pin_out)
        MockRPi.reset_mock()

    def tearDown(self):
        self.gpio.__del__()

    def test_start_no_timer(self):
        self.gpio.start()
        MockRPi.GPIO.output.assert_called_with(self.pin_out, True)
        self.assertEqual(self.gpio.timer, None)

    def test_stop_no_timer(self):
        self.gpio.stop()
        MockRPi.GPIO.output.assert_called_with(self.pin_out, False)

    def test_start_1s_timer(self):
        self.gpio.start(1)
        self.assertNotEqual(self.gpio.timer, None)

    def test_timer_auto_stop(self):
        self.gpio.start(.01)
        sleep(.02)
        MockRPi.GPIO.output.assert_called_with(self.pin_out, False)
