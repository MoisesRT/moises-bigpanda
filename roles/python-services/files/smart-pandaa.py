from flask import Flask
from multiprocessing import Value
from flask import request

class endpoint:
    def __init__(self):
        self.counter = Value('i', 0)

    def run(self):
        if request.method == 'POST':
            with self.counter.get_lock():
                self.counter.value += 1
            return '', 204
        else:
            return str(self.counter.value)
app = Flask(__name__)
app.add_url_rule('/', view_func=endpoint().run, methods=[u'GET', u'POST'])
if __name__ == '__main__':
    app.run(port='8082')