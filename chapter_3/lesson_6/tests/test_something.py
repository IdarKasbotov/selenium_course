import pytest


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username(username):
    assert username == 'directly-overridden-username', f"Expected 'directly-overridden-username', got {username}"


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(other_username, username):
    print(111111111, username)
    assert other_username == 'other-directly-overridden-username-other', f"Expected 'other-directly-overridden-username-other', got {other_username}"
