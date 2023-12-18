from unittest import TestCase

from src.models.event_processing.device import Device
from src.models.event_processing.device_status import DeviceType


class GenerateHashTest(TestCase):

    def test_generate_hash_galaxy_two(self):
        hash_expected = "1241903bf6723e9c4c769070e38059db46fe3cc4a8189a742c99fbab383234c7"

        device: Device = Device(
            id="1234",
            device_type="nave",
            device_status=DeviceType.GOOD,
            device_age=1
        )

        hash_obtained = device.get_hash("12122023102202", "GalaxyTwo", "nave", "good")

        self.assertEqual(hash_obtained, hash_expected)
