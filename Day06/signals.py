"""
Allister MacLeod - Advent of Code 2022
Day 6 - Communicator signals

"""


class PacketDetector(object):
    def __init__(self, marker_width: int):
        self.width = marker_width
        self.buffer = []

    def detect(self, input_signal: str) -> int:
        """
        Detect the first occurrence of a packet marker. Packet markers
        are defined by containing distinct characters for the whole
        width of the marker.

        :param input_signal:  full stream of input characters.
        :return:  quantity of characters consumed before detecting marker.
        """
        consumed = 0
        for c in input_signal:
            consumed += 1
            self.buffer.append(c)
            if len(self.buffer) > self.width:
                self.buffer.pop(0)
            if self.qualified(self.buffer):
                return consumed
        raise IndexError(f'No packet marker found in {input_signal}')

    def qualified(self, buffer: list[str]) -> bool:
        return len(buffer) == self.width and len(set(buffer)) == self.width
