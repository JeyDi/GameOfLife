class Cell:
    def __init__(self):
        self._status = False

    def set_alive(self):
        self._status = True

    def set_dead(self):
        self._status = False

    def check_status(self):
        return self._status

    def print_status(self):
        if self.check_status():
            return "*"
        else:
            return "0"
