import pytest as pytest

from main.message import Message


@pytest.fixture
def me():
    return Message("me")


def test_show_hey(me: Message):
    assert me.show_hey() == "me hey"


def test_show_hey_hey(me: Message):
    assert me.show_hey_hey() == "me hey hey"
