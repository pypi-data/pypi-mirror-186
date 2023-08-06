"""Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""


import typing
import numpy as np
import nanosurf.lib.datatypes.sci_channel as ch

class SciStream:
    
    def __init__(self, 
        source: typing.Union[tuple, list[typing.Any, typing.Any], 
        ch.SciChannel, 'SciStream', None] = None, 
        channels: int = 1, stream_length: int = 0, 
        x_unit: str = ""):

        self.channels = [ch.SciChannel(array_length=stream_length) for d in range(channels)]
        self.x = ch.SciChannel(unit=x_unit)
        
        if isinstance(source, ch.SciChannel):
            self.x = ch.SciChannel(source)
            self.channels = [ch.SciChannel(np.zeros_like(source))]
        elif isinstance(source, SciStream):
            self.x = ch.SciChannel(source.x)
            self.copy_channels(source)
        elif source is not None:
            self.x = ch.SciChannel(source[0],unit=x_unit)
            self.channels = [ch.SciChannel(source[1])]

    def set_stream_length(self, length: int):
        if length != self.get_stream_length():
            if self.x.value.size > 0:       
                min = np.min(self.x.value)
                max = np.max(self.x.value)
            else:
                min = 0.0
                max = 1.0
            self.x.value = np.resize(self.x.value, length)
            self.define_stream_range(min, max)
            self._adjust_channel_length()

    def get_stream_length(self) -> int:
        return self.x.value.size

    def set_stream_range(self, range: typing.Union[ch.SciChannel, np.ndarray, list], unit: str = ""):
        if isinstance(range, ch.SciChannel):
            self.x = range
        else:
            self.x = ch.SciChannel(range, unit=unit)
        self._adjust_channel_length()

    def get_stream_range(self) -> ch.SciChannel:
        return self.x

    def define_stream_range(self, min: float, max: float, unit: str = ""):
        self.x.value = np.linspace(min, max, self.get_stream_length())
        if unit != "":
            self.x.unit = unit

    def get_stream_unit(self) -> str:
        return self.x.unit

    def set_stream_unit(self, unit: str):
        self.x.unit = unit

    def get_channel_count(self) -> int:
        return len(self.channels)
        
    def set_channel_count(self, channels: int):
        current_len = self.get_channel_count()
        if current_len < channels:
            self.channels.extend( [ch.SciChannel(array_length=self.get_stream_length()) for d in range(channels - current_len)])
        elif current_len > channels:
            self.channels = self.channels[:channels]

    def copy_channels(self, source: 'SciStream'):
        assert source.get_stream_length() == self.get_stream_length(), "SciStream: Streams must have equal length"
        self.channels = [ch.SciChannel(source.channels[stream_index]) for stream_index in range(source.get_channel_count())]    

    def get_channel(self, channel_index: int) -> ch.SciChannel:
        assert channel_index < len(self.channels), "SciStream: Channel index out of bound error"
        return self.channels[channel_index]

    def set_channel(self, channel_index: int, source: typing.Union[ch.SciChannel, np.ndarray, list], unit: str = ""):
        assert channel_index < len(self.channels), "SciStream: Channel index out of bound error"
        self.channels[channel_index] = ch.SciChannel(source, unit=unit)

    def get_channel_unit(self, channel_index: int) -> str:
        assert channel_index < len(self.channels), "SciStream: Channel index out of bound error"
        return self.channels[channel_index].unit

    def set_channel_unit(self, channel_index: int, unit: str):
        assert channel_index < len(self.channels), "SciStream: Channel index out of bound error"
        self.channels[channel_index].unit = unit

    def _adjust_channel_length(self):
        x_size = self.x.value.size
        for ch in self.channels:
            if ch.value.size != x_size:
                ch.value = np.resize(ch.value, x_size)