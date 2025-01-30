import pytest

from employee import Employee


@pytest.fixture
def employee():
    employee = Employee("Caleb", "Pauline", 60000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 65000

def test_give_custom_raise(employee):
    employee.give_raise(1000)
    assert employee.annual_salary == 61000