from enum import Enum


class Temperature_Constants(Enum):
    CELCIUS_UPPER_FIXED_POINT = 100
    CELCIUS_LOWER_FIXED_POINT = 0
    FAHRENHEIT_UPPER_FIXED_POINT = 212
    FAHRENHEIT_LOWER_FIXED_POINT = 32
    KELVIN_UPPER_FIXED_POINT = 373.15
    KELVIN_LOWER_FIXED_POINT = 273.15

    def __str__(self):
        return f"""
        {self.CELCIUS_UPPER_FIXED_POINT}
        {self.CELCIUS_LOWER_FIXED_POINT}
        {self.FAHRENHEIT_UPPER_FIXED_POINT}
        {self.FAHRENHEIT_LOWER_FIXED_POINT}
        {self.KELVIN_UPPER_FIXED_POINT}
        {self.KELVIN_LOWER_FIXED_POINT}
        """

    def __repr__(self):
        return f"""
        {self.CELCIUS_UPPER_FIXED_POINT}
        {self.CELCIUS_LOWER_FIXED_POINT}
        {self.FAHRENHEIT_UPPER_FIXED_POINT}
        {self.FAHRENHEIT_LOWER_FIXED_POINT}
        {self.KELVIN_UPPER_FIXED_POINT}
        {self.KELVIN_LOWER_FIXED_POINT}
        """
