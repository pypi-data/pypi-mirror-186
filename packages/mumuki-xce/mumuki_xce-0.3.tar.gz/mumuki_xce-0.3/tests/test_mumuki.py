import pytest

from mumuki import Mumuki

def test_can_create_with_default_url():
    mumuki = Mumuki("token", "es")
    assert mumuki._url == "https://mumuki.io"

def test_can_create_with_custom_url():
    mumuki = Mumuki("token", "es", "http://localhost:3000")
    assert mumuki._url == "http://localhost:3000"

def test_not_offline_by_default():
    mumuki = Mumuki("token", "es")
    assert not mumuki._offline()

def test_can_register_plain_string():
    mumuki = Mumuki("token", "es")
    mumuki.register_solution("def foo(): pass")
    assert mumuki._solution == "def foo(): pass"

def test_can_register_function():
    def solution():
        def baz(): return 4 + 5

    mumuki = Mumuki("token", "es")
    mumuki.register_solution(solution)
    assert mumuki._solution == "def baz(): return 4 + 5\n"
