from flask import Flask, render_template


def url_builder(string: list):
    url = ''
    for item in string:
        url += f'{item}/'

    return url




def create_app():
    app = Flask(__name__)

    @app.route('/<path:subpath>')
    def home(subpath):
        if str(subpath).endswith('/'):
            subpath = str(subpath)[:-1]
        return render_template('/base.html', path=subpath, url_builder=url_builder, len=len)
    

    return app
