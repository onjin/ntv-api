import morepath
import ntv.api

from webtest import TestApp as Client


def test_root():
    morepath.scan(ntv.api)
    morepath.commit(ntv.api.App)

    client = Client(ntv.api.App())
    root = client.get('/')

    assert root.status_code == 200
    assert len(root.json['greetings']) == 2
