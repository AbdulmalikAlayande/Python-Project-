from TemperatureConverter.Menu import Menu


class Temperature_Main:

    @staticmethod
    def main():
        tmm = Menu()
        tmm.display_welcome()


if __name__ == '__main__':
    tm = Temperature_Main()
    tm.main()
