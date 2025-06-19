import pandas as pd
import random

from models.SecretSanta import SecretSanta
from utils.excelUtils import return_employee_list

"""
    This code reads an Excel file containing employee names and emails, creates Employee objects, and assigns Secret Santas among them.
    It raises exceptions for missing columns, empty files, and insufficient employees.
    The previous year's Secret Santa assignments are also read from another Excel file to ensure no one gets the same Secret Santa as last year.
    The results are printed and saved to a new Excel file.
"""


def main():
    file_path = "input/Employee-List.xlsx"
    previous_santa_file_path = "input/Secret-Santa-Game-Result-2023.xlsx"
    employees = return_employee_list(file_path, previous_santa_file_path)

    print("EMPLOYEES:", employees)

    secret_santa_manager = SecretSanta(employees)

    secret_santa_manager.assign_secret_santa()

    print(
        "           ******       Current (2024) Secret Santa assignments:        ****** \n"
    )
    for employee in secret_santa_manager.employees:
        print(
            f"{employee.employee_name} ({employee.employee_email}) -> {employee.secret_santa.employee_name} ({employee.secret_santa.employee_email})"
        )
    print("\n\n")

    df = pd.DataFrame(
        {
            "Employee_Name": [
                emp.employee_name for emp in secret_santa_manager.employees
            ],
            "Employee_EmailID": [
                emp.employee_email for emp in secret_santa_manager.employees
            ],
            "Secret_Child_Name": [
                emp.secret_santa.employee_name for emp in secret_santa_manager.employees
            ],
            "Secret_Child_EmailID": [
                emp.secret_santa.employee_email
                for emp in secret_santa_manager.employees
            ],
        }
    )

    import os

    if not os.path.exists("output"):
        os.makedirs("output")

    output_file_path = "output/Secret-Santa-Game-Result-2024.xlsx"
    df.to_excel(output_file_path, index=False)
    print(f"Secret Santa assignments saved to {output_file_path}")


if __name__ == "__main__":
    main()
