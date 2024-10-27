"""Hello unit test module."""

from server.start import start


def test_start():
    assert start() == "Hello server"
