from multiprocessing import Value
from flask import request


class SmartPanda:
    def __init__(self):
        self.counter = Value('i', 0)

    def run(self):
        if request.method == 'POST':
            with self.counter.get_lock():
                self.counter.value += 1
            return '', 204
        else:
            return str(self.counter.value)