import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog

from TemperatureConverter.Dialog import Dialog
from TemperatureConverter.Temperature import Temperature


class Menu:
    app = QApplication(sys.argv)

    def __init__(self):
        self.temperature = Temperature()

    def display_welcome(self):
        self.message_box_code_reuse("WELCOME!!!")

    def main_menu(self):
        main_menu = """
        1 --> Convert Celcius to fahrenheit
        2 --> Convert Celcius to Kelvin
        3 --> Convert Celcius to rankine
        4 --> Convert Celcius to raemur
        5 --> Convert Celcius to newton
        6 --> Convert Fahrenheit to Celcius
        7 --> Convert Fahrenheit to Kelvin
        8 --> Convert Kelvin to Fahrenheit
        9 --> Convert Kelvin to Celcius
        10--> View recent conversions
        11 --> View all conversions
        12 --> Exit
        """

        Dialog.abdulmalik_message_display(main_menu)
        user_input, ok_pressed = QInputDialog.getText(None, "Converter Menu", main_menu)
        if ok_pressed & isinstance(user_input, str):
            match user_input[0]:
                case '1':
                    self.convert_celcius_to_fahrenheit()
                case '2':
                    self.convert_celcius_to_kelvin()
                case '3':
                    self.convert_celcius_to_rankine()
                case '4':
                    self.convert_celcius_to_raemur()
                case '5':
                    self.convert_celcius_to_newton()
                case '6':
                    self.convert_fahrenheit_to_celcius()
                case '7':
                    self.convert_fahrenheit_to_kelvin()
                case '8':
                    self.convert_kelvin_to_fahrenheit()
                case '9':
                    self.convert_kelvin_to_celcius()
                case '10':
                    self.view_recent_conversions()
                case '11':
                    self.view_all_conversions()
                case '12':
                    sys.exit(0)
                case _:
                    self.main_menu()

    def convert_celcius_to_fahrenheit(self):
        celcius_value, ok_pressed = QInputDialog.getInt(None, "Temperature Converter", "Enter the celcius value")
        if ok_pressed & isinstance(celcius_value, int):
            fahrenheit_value = self.temperature.convert_celcius_to_fahrenheit(celcius_value)
            Dialog.abdulmalik_message_display(str(fahrenheit_value))
            self.main_menu()

    def convert_celcius_to_kelvin(self):
        celcius_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the celcius value", 0, -2147483647, 2147483647, 1)
        if ok_pressed & isinstance(celcius_value, int):
            kelvin_value = self.temperature.convert_celcius_to_kelvin(celcius_value)
            Dialog.abdulmalik_message_display(str(kelvin_value))
            self.main_menu()

    def convert_celcius_to_rankine(self):
        celcius_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the celcius value", 0, -2147483647, 2147483647, 1)
        if ok_pressed & isinstance(celcius_value, int):
            rankine_value = self.temperature.convert_celcius_to_rankine(celcius_value)
            Dialog.abdulmalik_message_display(str(rankine_value))
            self.main_menu()

    def convert_celcius_to_raemur(self):
        celcius_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the celcius value", 0, -2147483647, 2147483647, 1)
        if ok_pressed & isinstance(celcius_value, int):
            raemur_value = self.temperature.convert_celcius_to_raemur(celcius_value)
            Dialog.abdulmalik_message_display(str(raemur_value))
            self.main_menu()

    def convert_celcius_to_newton(self):
        celcius_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the celcius value", 0, -2147483647, 2147483647, 1)
        if ok_pressed & isinstance(celcius_value, int):
            newton_value = self.temperature.convert_celcius_to_newton(celcius_value)
            Dialog.abdulmalik_message_display(str(newton_value))
            self.main_menu()

    # , "OK", "Cancel"
    def convert_fahrenheit_to_celcius(self):
        fahrenheit_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the fahrenheit value", 0, -2147483647, 2147483647, 1)
        if ok_pressed and isinstance(fahrenheit_value, int):
            celcius_value = self.temperature.convert_fahrenheit_to_celcius(fahrenheit_value)
            Dialog.abdulmalik_message_display(str(celcius_value))
            self.main_menu()

    def convert_fahrenheit_to_kelvin(self):
        fahrenheit_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the fahrenheit value", 0, -2147483647, 2147483647, 1)
        if ok_pressed and isinstance(fahrenheit_value, int):
            kelvin_value = self.temperature.convert_fahrenheit_to_kelvin(fahrenheit_value)
            Dialog.abdulmalik_message_display(str(kelvin_value))
            self.main_menu()

    def convert_kelvin_to_fahrenheit(self):
        kelvin_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter kelvin value", 0, -2147483647, 2147483647, 1)
        if ok_pressed and isinstance(kelvin_value, int):
            fahrenheit_value = self.temperature.convert_kelvin_to_fahrenheit(kelvin_value)
            Dialog.abdulmalik_message_display(str(fahrenheit_value))
            self.main_menu()

        pass

    def convert_kelvin_to_celcius(self):
        kelvin_value, ok_pressed = Dialog.abdulmalik_input_int("Temperature Converter", "Enter the kelvin value", 0, -2147483647, 2147483647, 1)
        if ok_pressed and isinstance(kelvin_value, int):
            celcius_value = self.temperature.convert_kelvin_to_fahrenheit(kelvin_value)
            Dialog.abdulmalik_message_display(str(celcius_value))
            self.main_menu()

    def view_recent_conversions(self):
        pass

    def view_all_conversions(self):
        pass

    def message_box_code_reuse(self, value):
        message_box = QMessageBox()
        message_box.setText(str(value))
        message_box.exec()
        self.main_menu()
