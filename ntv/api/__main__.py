from werkzeug.serving import run_simple
from .app import make_app


def run():
    run_simple('localhost', 8000, make_app(), use_reloader=True)


if __name__ == '__main__':
    run()
