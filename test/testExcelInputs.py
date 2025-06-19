import unittest
import os
from Angelin.main import run_secret_santa
from utils.file_handler import read_employees

import pandas as pd
import random

from models.Employee import Employee
from models.SecretSanta import SecretSanta


def test_return_employee_list():
    file_path = "test/input/Employee-List.xlsx"
    previous_santa_file_path = "input/Secret-Santa-Game-Result-2023.xlsx"

    employees = read_employees(file_path, previous_santa_file_path)

    assert len(employees) > 0, "Employee list should not be empty"

    for employee in employees:
        assert isinstance(employee, Employee), (
            "Each item in the employee list should be an Employee object"
        )
        assert employee.employee_name, "Employee name should not be empty"
        assert employee.employee_email, "Employee email should not be empty"
        assert employee.previous_santa, "Previous Santa should not be None"
