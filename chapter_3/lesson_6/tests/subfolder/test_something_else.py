# content of tests/test_something_else.py
def test_username(username):
    assert username == 'overridden-username', f"Expected 'overridden-username', got {username}"
