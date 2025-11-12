import pytest
from employee import Employee


@pytest.fixture
def employee():
    employee = Employee("Lara", "Croft", 100000)
    return employee


def test_give_default_raise(employee: Employee):
    employee.give_raise()
    assert employee.salary == 105000


def test_give_custom_raise(employee: Employee):
    employee.give_raise(17000)
    assert employee.salary == 117000
