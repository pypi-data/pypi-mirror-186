"""Env module."""

import struct
from modi_plus.module.module import InputModule


class Env(InputModule):

    PROPERTY_ENV_STATE = 2

    PROPERTY_OFFSET_INTENSICY = 0
    PROPERTY_OFFSET_TEMPERATURE = 2
    PROPERTY_OFFSET_HUMIDITY = 4
    PROPERTY_OFFSET_VOLUME = 6

    @property
    def intensity(self) -> int:
        """Returns the value of intensity between 0 and 100

        :return: The environment's intensity.
        :rtype: int
        """

        offset = Env.PROPERTY_OFFSET_INTENSICY
        raw = self._get_property(Env.PROPERTY_ENV_STATE)
        data = struct.unpack("h", raw[offset:offset + 2])[0]
        return data

    @property
    def temperature(self) -> int:
        """Returns the value of temperature between -10 and 60

        :return: The environment's temperature.
        :rtype: int
        """

        offset = Env.PROPERTY_OFFSET_TEMPERATURE
        raw = self._get_property(Env.PROPERTY_ENV_STATE)
        data = struct.unpack("h", raw[offset:offset + 2])[0]
        return data

    @property
    def humidity(self) -> int:
        """Returns the value of humidity between 0 and 100

        :return: The environment's humidity.
        :rtype: int
        """

        offset = Env.PROPERTY_OFFSET_HUMIDITY
        raw = self._get_property(Env.PROPERTY_ENV_STATE)
        data = struct.unpack("h", raw[offset:offset + 2])[0]
        return data

    @property
    def volume(self) -> int:
        """Returns the value of volume between 0 and 100

        :return: The environment's volume.
        :rtype: int
        """

        offset = Env.PROPERTY_OFFSET_VOLUME
        raw = self._get_property(Env.PROPERTY_ENV_STATE)
        data = struct.unpack("h", raw[offset:offset + 2])[0]
        return data
