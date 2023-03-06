"""
*********Converting Celcius to Fahrenheit and vice versa********:
from y = mx + c
The graph shows that :
y = fahrenheit value
x = corresponding celcius/centigrade value
gradient m = 9/5 = 1.8
intercept c = 32
.'. to convert from celcius to fahrenheit and vice versa, we use --> y = 1.8x + 32 == °f = 1.8°c + 32

**********Converting Celcius to Kelvin and vice versa***********:
from y = mx + c
The graph shows that :
y = kelvin value
x = corresponding celcius/centigrade value
gradient m = y2 - y1 / x2 - x1 = 100/100 = 1
intercept = 273.15
.'. to convert from celcius to kelvin and vice versa, we use ==> y = 1x + 273.15 == °k = °c + 273.15

************Converting Fahrenheit to Kelvin and vice versa************
recall that °f = 1.8°c + 32
also recall that °k = °c + 273.15
from that we can say that °c = (°f - 32) / 1.8 or °c = 5/9(°f - 32)
we can also say that °c = °k - 273.15
.'. °k = 5/9(°f - 32) + 273.15
also °f = 9/5(°k - 273.15) + 32
"""


class Temperature:

    @staticmethod
    def convert_celcius_to_fahrenheit(celcius: float or int) -> float:
        gradient, intercept = 9/5, 32
        return (gradient * celcius) + intercept

    @staticmethod
    def convert_celcius_to_kelvin(celcius: float or int) -> float:
        gradient, intercept = 1, 273.15
        return (gradient * celcius) + intercept

    @staticmethod
    def convert_fahrenheit_to_celcius(fahrenheit: float or int) -> float:
        gradient, intercept = 9/5, 32
        gradient_inverse = 1/gradient
        return gradient_inverse * (fahrenheit - intercept)

    @staticmethod
    def convert_fahrenheit_to_kelvin(fahrenheit: float or int) -> float:
        gradient, x_intercept, y_intercept = 9/5, 32, 273.15
        gradient_inverse = 1/gradient
        return (gradient_inverse * (fahrenheit - x_intercept)) + y_intercept

    @staticmethod
    def convert_kelvin_to_celcius(kelvin: float or int) -> float:
        gradient, intercept = 1, 273.15
        gradient_inverse = 1/gradient
        return gradient_inverse * (kelvin - intercept)

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin: float or int) -> float:
        gradient, x_intercept, y_intercept = 9/5, 32, 273.15
        return (gradient*(kelvin - y_intercept)) + x_intercept
