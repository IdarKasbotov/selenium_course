"""
https://stepik.org/lesson/237257/step/7?unit=209645
pytest ./chapter_3/lesson_4/test_step_7/test_step_7.py -vs, где -v - это verbose, -s для того, чтобы видеть принты
"""
import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print(111111111111111111)

    def test_second_smiling_faces(self, prepare_faces):
        assert False, "kek"
