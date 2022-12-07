from unittest import TestCase


import signals


class TestPacketDetector(TestCase):
    def test_detect(self):
        detector = signals.PacketDetector(4)
        signal_input = "ababcded"
        self.assertEqual(6, detector.detect(signal_input))
