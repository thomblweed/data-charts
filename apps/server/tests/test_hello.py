"""Hello unit test module."""

from server.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello server"
