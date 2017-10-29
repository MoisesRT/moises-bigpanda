from flask import Flask
from random import choice
from mimetypes import guess_type
from flask import send_from_directory
from os import listdir

class endpoint:
    def __init__(self, imgs_path='./resources'):
        self.imgs_path = imgs_path
        self.imgs = listdir(self.imgs_path)

    def run(self):
        img = choice(self.imgs)
        return send_from_directory(self.imgs_path, img, mimetype=guess_type(img)[0])
app = Flask(__name__)
app.add_url_rule('/', view_func=endpoint().run, methods=[u'GET'])
if __name__ == '__main__':
    app.run(port='8081')