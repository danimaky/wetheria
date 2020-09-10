from logging import Handler, Formatter, WARNING


class WetheriaAlertHandler(Handler):
    FORMAT = Formatter('%(name)s - %(levelname)s - %(message)s')

    def __init__(self, level=WARNING):
        """
        Initializes the instance - basically setting the formatter to None
        and the filter list to empty.
        """
        super(WetheriaAlertHandler, self).__init__(level=level)
        self.setFormatter(self.FORMAT)

    def emit(self, record):
        print("*"*95 + " Custom Logger " + "*"*90)
        print(self.format(record))
        print("*"*200)
