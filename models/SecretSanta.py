import random

class SecretSanta:
    def __init__(self, employees=None):
        self.employees = employees if employees is not None else []

    
    def assign_secret_santa(self):
        self.check_employees()

        unassigned = self.employees[:]
        for employee in self.employees:
            valid_choices = [
                e for e in unassigned
                if e != employee and e != employee.previous_santa
            ]
            if not valid_choices:
                raise ValueError("Unable to assign Secret Santas without conflicts. Please retry.")
            
            chosen = random.choice(valid_choices)
            employee.secret_santa = chosen
            unassigned.remove(chosen)

        self.check_employees(True)

        
    def check_employees(self, postAssignment=False):
        if len(self.employees) < 2:
            raise ValueError("At least two employees are required to assign Secret Santas.")
        
        if not self.employees:
            raise ValueError("Employee list is empty. Please add employees before assigning Secret Santas.")

        if postAssignment and any(employee.secret_santa is None for employee in self.employees):
            raise ValueError("Not all employees have been assigned a Secret Santa. Please check the assignments.")
        
        if postAssignment and any(employee.previous_santa is employee.secret_santa for employee in self.employees):
            raise ValueError("An employee cannot get their previous year's Secret Santa. Run the program again to retry assignments.")
        
        if postAssignment and any(employee.previous_santa is employee.employee_name for employee in self.employees):
            raise ValueError("An employee cannot be their own Secret Santa. Run the program again to retry assignments.")
        